import os
from dotenv import load_dotenv
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma  # Το νέο πακέτο της Chroma

load_dotenv()


base_dir = r"ceid_chatbot\data_final"

files_config = [
    {
        "path": os.path.join(base_dir, "administration.md"),
        "headers": [("#", "Header 1"), ("##", "Header 2"), ("####", "Header 4"),]
    },
    {
        "path": os.path.join(base_dir, "building_instructions.md"),
        "headers": [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3"),] 
    },
    {
        "path": os.path.join(base_dir, "general.md"),
        "headers": [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3"), ("####", "Header 4"), ("######", "Header 5"), ("#######", "Header 6"),]
    },
    {
        "path": os.path.join(base_dir, "modified_extracted_fixed_odigos_spoudwn_info.md"),
        "headers": [("##", "Header 2"), ("###", "Header 3"),]
    },
    {
        "path": os.path.join(base_dir, "modified_extracted_katalogos_mathimatwn_2025_2026_new_formatted_by_instructor.md"),
        "headers": [("#", "Header 1"), ("###", "Header 3"),]
    },
    {
        "path": os.path.join(base_dir, "modified_extracted_katalogos_mathimatwn_2025_2026_new_formatted.md"),
        "headers": [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3"),]
    },
    {
        "path": os.path.join(base_dir, "sectors_and_professors.md"),
        "headers": [("#", "Header 1"), ("##", "Header 2"), ("####", "Header 4"),]
    },
    {
        "path": os.path.join(base_dir, "sectors_and_teaching_staff.md"),
        "headers": [("#", "Header 1"), ("##", "Header 2"), ("####", "Header 4"),]
    },
    {
        "path": os.path.join(base_dir, "selective_courses_associated_with_K.md"),
        "headers": [("###", "Header 3"),]
    },
    {
        "path": os.path.join(base_dir, "selective.md"),
        "headers": [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3"), ("####", "Header 4"), ("#####", "Header 5"),]
    },
    {
        "path": os.path.join(base_dir, "sectors_and_labs.md"),
        "headers": [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3"),]
    }
]

text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)

all_splits = []

output_dir = "chunks"
os.makedirs(output_dir, exist_ok=True)
print(f"=== Εντοπίστηκε/Δημιουργήθηκε ο φάκελος '{output_dir}' για τα txt αρχεία ===\n")

print("=== ΞΕΚΙΝΑΕΙ Η ΑΝΑΓΝΩΣΗ ΑΡΧΕΙΩΝ ===")
for file_info in files_config:
    file_path = file_info["path"]
    headers_to_split_on = file_info["headers"]
    
    if not os.path.exists(file_path):
        print(f"⚠️ Προσοχή: Το αρχείο {file_path} δεν βρέθηκε. Ελέγξτε τη διαδρομή.")
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
        
    print(f"Διαβάζεται: {file_path}")
    
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    
    md_header_splits = markdown_splitter.split_text(md_text)
    
    final_splits = text_splitter.split_documents(md_header_splits)
    
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    
    for i, split in enumerate(final_splits):
        split.metadata['source'] = file_path.replace("\\", "/") 
        

        header_keys = sorted(
            [k for k in split.metadata.keys() if str(k).startswith("Header")],
            key=lambda x: int(str(x).split()[-1]) if str(x).split()[-1].isdigit() else 0 
        )
        
        headers_string = " > ".join([str(split.metadata[k]) for k in header_keys])
        
        if headers_string:
            split.page_content = f"{headers_string}\n{split.page_content}"
        
        filename = os.path.join(output_dir, f"{base_name}_chunk_{i+1}.txt")
        with open(filename, "w", encoding="utf-8") as text_file:
            text_file.write("=== METADATA ===\n")
            text_file.write(f"{split.metadata}\n\n")
            text_file.write("=== CONTENT ===\n")
            text_file.write(split.page_content)
            
    all_splits.extend(final_splits)
    print(f"  └─ Δημιουργήθηκαν και αποθηκεύτηκαν {len(final_splits)} chunks σε μορφή txt.\n")

print(f"Συνολικά δημιουργήθηκαν {len(all_splits)} chunks κειμένου.\n")

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vectorstore = Chroma.from_documents(
    documents=all_splits, 
    embedding=embeddings, 
    persist_directory="./db"
)