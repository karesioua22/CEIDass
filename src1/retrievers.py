import os
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma


embeddings = OpenAIEmbeddings(model="text-embedding-3-small")


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))

persist_directory = os.path.join(ROOT_DIR, "db")
if not os.path.exists(persist_directory):
    print(f"ΠΡΟΣΟΧΗ: Ο φάκελος της βάσης '{persist_directory}' δεν βρέθηκε. Έχεις τρέξει το ingest.py;")

vectorstore = Chroma(
    persist_directory=persist_directory, 
    embedding_function=embeddings
)

def search_expert_knowledge(query: str, source_file: str, k: int = 10) -> str:
    """
    Αναζητά τα πιο σχετικά κομμάτια κειμένου (chunks) για μια ερώτηση,
    περιορίζοντας την αναζήτηση ΑΥΣΤΗΡΑ στο αρχείο του εκάστοτε ειδικού.
    Χρησιμοποιεί MMR για να εξασφαλίσει ότι τα αποτελέσματα έχουν ποικιλομορφία.
    """
    
    results = vectorstore.max_marginal_relevance_search(
        query=query, 
        k=k,                
        fetch_k=k * 3,      
        lambda_mult=0.5,   
        filter={"source": source_file}
    )
    

    if not results:
        return "Δεν βρέθηκαν σχετικές πληροφορίες στα έγγραφα της αρμοδιότητάς μου."
    
    context_parts = []
    
    for doc in results:
       
        header_keys = sorted([k for k in doc.metadata.keys() if str(k).startswith("Header")])
        
        headers_string = " > ".join([str(doc.metadata[k]) for k in header_keys])
        
        chunk_text = ""
        if headers_string:
            chunk_text += f"[ΚΑΤΗΓΟΡΙΑ/ΤΙΤΛΟΣ: {headers_string}]\n"
            
        chunk_text += doc.page_content
        
        context_parts.append(chunk_text)
        
    formatted_context = "\n\n--- ΕΠΟΜΕΝΟ ΑΠΟΣΠΑΣΜΑ ---\n\n".join(context_parts)
    
    return formatted_context