import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from tools import university_tools

load_dotenv()

llm = ChatOpenAI(model="gpt-5o", temperature=0) 
llm_with_tools = llm.bind_tools(university_tools)

system_prompt = SystemMessage(content="""
Είσαι ο Βοηθός του Τμήματος Μηχανικών Η/Υ του Πανεπιστημίου Πατρών.
Αν χρειάζεσαι πληροφορίες, χρησιμοποίησε τα εργαλεία σου. 
Μπορείς να χρησιμοποιήσεις πολλαπλά εργαλεία στη σειρά αν η ερώτηση είναι σύνθετη.
Απάντα ΠΑΝΤΑ στα Ελληνικά, με σαφήνεια και χρησιμοποιώντας bullet points όπου ταιριάζει.
ΜΗΝ υποθέτεις πληροφορίες. Βασίσου αυστηρά σε αυτά που σου επιστρέφουν τα εργαλεία.
                        
ΚΑΝΟΝΕΣ ΑΥΣΤΗΡΗΣ ΑΠΑΝΤΗΣΗΣ (CRITICAL):
1. Απάντα ΑΚΡΙΒΩΣ σε αυτό που ρωτάει ο χρήστης και ΤΙΠΟΤΑ ΠΑΡΑΠΑΝΩ. 
2. Να είσαι απόλυτα λακωνικός και στοχευμένος.
""")

def run_chatbot():
    print("\n" + "="*60)
    print("🎓 CEIDass Πανεπιστημιακός Βοηθός")
    print("Πληκτρολογήστε 'quit', 'exit' ή 'q' για έξοδο.")
    print("="*60)
    
    chat_history = [system_prompt]
    
    while True:
        user_input = input("\n👤 Εσύ: ")
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\nΤερματισμός συστήματος. Καλή συνέχεια!")
            break
            
        if not user_input.strip():
            continue
            
        chat_history.append(HumanMessage(content=user_input))
        
        print("\n ...")
        
        while True:
            response = llm_with_tools.invoke(chat_history)
            chat_history.append(response)
            
            if not response.tool_calls:
                print(f"\n🤖 AI Τελική Απάντηση:\n{response.content}")
                break
                
            for tool_call in response.tool_calls:
                tool_name = tool_call["name"]
                tool_args = tool_call["args"]
                
            
                
                selected_tool = next(t for t in university_tools if t.name == tool_name)
                
                tool_result = selected_tool.invoke(tool_args)
                
                chat_history.append(ToolMessage(
                    content=str(tool_result),
                    tool_call_id=tool_call["id"]
                ))

if __name__ == "__main__":
    run_chatbot()