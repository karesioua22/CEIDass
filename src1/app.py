import streamlit as st
import os
import sys
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage, AIMessage

# --- ΕΠΙΛΥΣΗ ΔΙΑΔΡΟΜΩΝ (PATH FIX) ---
# Επειδή το app.py είναι μέσα στο φάκελο src/, λέμε στην Python 
# να προσθέσει τον "γονικό" φάκελο (root) στις διαδρομές αναζήτησης.
# Έτσι θα βρίσκει κανονικά τον φάκελο 'tools' και την βάση 'db'.
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ROOT_DIR)

# Τώρα μπορούμε να κάνουμε import με ασφάλεια!
from tools import university_tools 

load_dotenv()

# --- 1. Διαμόρφωση Σελίδας ---
st.set_page_config(page_title="CEIDass", page_icon="💻", layout="centered")


image_path = os.path.join(ROOT_DIR, "ceid.jpg") 

if os.path.exists(image_path):
    st.image(image_path, width=400)
else:
    st.warning(f"Η εικόνα δεν βρέθηκε στη διαδρομή: {image_path}")
# --------------------------------------------------

st.title("💻 CEIDass ")
st.caption("Γειά σας είμαι ο CEID Assistant✌🏼, ο ψηφιακός βοηθός για το Τμήμα Μηχανικών Η/Υ και Πληροφορικής του Πανεπιστημίου Πατρών! Ρωτήστε με για μαθήματα, καθηγητές, αίθουσες και κανονισμούς του ΤΜΗΥΠ!")

@st.cache_resource 
def get_llm():
    llm = ChatOpenAI(model="gpt-5", temperature=0)
    return llm.bind_tools(university_tools)

llm_with_tools = get_llm()


if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="""
        Είσαι ο Βοηθός του Τμήματος Μηχανικών Η/Υ του Πανεπιστημίου Πατρών.
        Αν χρειάζεσαι πληροφορίες, χρησιμοποίησε τα εργαλεία σου. 
        Μπορείς να χρησιμοποιήσεις πολλαπλά εργαλεία στη σειρά αν η ερώτηση είναι σύνθετη.
        Απάντα ΠΑΝΤΑ στα Ελληνικά και με επαγγελματικό αλλά φιλικό τόνο.
        ΜΗΝ υποθέτεις πληροφορίες. Βασίσου αυστηρά σε αυτά που σου επιστρέφουν τα εργαλεία.
                      
        ΚΑΝΟΝΕΣ ΑΥΣΤΗΡΗΣ ΑΠΑΝΤΗΣΗΣ (CRITICAL):
        1. Απάντα ΑΚΡΙΒΩΣ σε αυτό που ρωτάει ο χρήστης και ΤΙΠΟΤΑ ΠΑΡΑΠΑΝΩ. 
        2. Να είσαι απόλυτα λακωνικός και στοχευμένος.
        """)
    ]


for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user", avatar="👤"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage) and msg.content: 
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(msg.content)

user_input = st.chat_input("Πληκτρολογήστε την ερώτησή σας εδώ...")

if user_input:
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_input)
    
    st.session_state.messages.append(HumanMessage(content=user_input))

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Αναζήτηση στη βάση δεδομένων..."):
            
            while True:
                response = llm_with_tools.invoke(st.session_state.messages)
                st.session_state.messages.append(response)
                
                if not response.tool_calls:
                    st.markdown(response.content)
                    break
                    
                for tool_call in response.tool_calls:
                    tool_name = tool_call["name"]
                    tool_args = tool_call["args"]
                    
                    selected_tool = next(t for t in university_tools if t.name == tool_name)
                    tool_result = selected_tool.invoke(tool_args)
                    
                    st.session_state.messages.append(ToolMessage(
                        content=str(tool_result),
                        tool_call_id=tool_call["id"]
                    ))