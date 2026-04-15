from langchain_core.tools import tool
from retrievers import search_expert_knowledge 

@tool
def search_administration(query: str) -> str:
    """Χρησιμοποιήστε αυτό το εργαλείο για να βρείτε πληροφορίες σχετικά με τη διοίκηση του τμήματος, όπως ο πρόεδρος, ο αντιπρόεδρος, ο γραμματέας και οι αρμοδιότητές τους. 
    Αυτό το εργαλείο δεν παρέχει πληροφορίες για μαθήματα, στοιχεία επικοινωνίας (αριθμούς τηλεφώνου, email) ή γενικές πληροφορίες για το τμήμα και το κτίριο, τη γραμματεία, τους καθηγητές/διδακτικό προσωπικό (σύντομα βιογραφικά) και πώς το τμήμα χωρίζεται σε τομείς και τι εργαστήρια διαθέτουν."""
    return search_expert_knowledge(query, "ceid_chatbot/data_final/administration.md")

@tool
def search_building_instructions(query: str) -> str:
    """Χρησιμοποιήστε αυτό το εργαλείο ΜΟΝΟ για να βρείτε πληροφορίες σχετικά με τις οδηγίες για το κτίριο του τμήματος, όπως χωρητικότητα και οδηγίες μετάβασης σε αίθουσες και γραφεία."""
    return search_expert_knowledge(query, "ceid_chatbot/data_final/building_instructions.md")

@tool
def search_general_info(query: str) -> str:
    """Χρησιμοποιήστε αυτό το εργαλείο για να βρείτε γενικές πληροφορίες του τμήματος, όπως κανονισμούς, εγγραφές, δομή προγράμματος σπουδών, φοιτητικές και ερευνητικές ομάδες, επιτροπές, μεταπτυχιακές σπουδές, erasmus, διδακτορικά, πλατφόρμες και δραστηριότητες. 
    Αυτό το εργαλείο δεν παρέχει πληροφορίες για μαθήματα, στοιχεία επικοινωνίας (αριθμούς τηλεφώνου, email) ή πληροφορίες για το κτίριο, τη διοίκηση, τη γραμματεία, τους καθηγητές/διδακτικό προσωπικό (σύντομα βιογραφικά) και πώς το τμήμα χωρίζεται σε τομείς και τι εργαστήρια διαθέτουν."""
    return search_expert_knowledge(query, "ceid_chatbot/data_final/general.md")

@tool
def search_communication_info(query: str) -> str:
    """Χρησιμοποιήστε αυτό το εργαλείο για να βρείτε στοιχεία επικοινωνίας (αριθμούς τηλεφώνου, email) 
    ΜΗΝ κάνετε αναζήτηση χρησιμοποιώντας γενικούς όρους όπως 'καθηγητής μαθηματικών'. Αν δεν γνωρίζετε το ακριβές όνομα, χρησιμοποιήστε πρώτα ένα άλλο εργαλείο για να το βρείτε!"""
    return search_expert_knowledge(query, "ceid_chatbot/data_final/modified_extracted_fixed_odigos_spoudwn_info.md")

@tool
def search_core_courses(query: str) -> str:
    """Χρησιμοποιήστε αυτό το εργαλείο για να βρείτε πληροφορίες σχετικά με τα μαθήματα , και το πώς τα μαθήματα κατανέμονται σε εξάμηνα, καθώς και τις απαιτούμενες ώρες διδασκαλίας."""
    return search_expert_knowledge(query, "ceid_chatbot/data_final/modified_extracted_katalogos_mathimatwn_2025_2026_new_formatted.md")

@tool
def search_teaching_courses(query: str) -> str:
    """Χρησιμοποιήστε αυτό το εργαλείο για να βρείτε πληροφορίες σχετικά με τα μαθήματα που διδάσκει κάθε καθηγητής ή κάθε διδακτικό προσωπικό καθώς το σύνολο των απαιτούμενων ώρων διδασκαλίας."""
    return search_expert_knowledge(query, "ceid_chatbot/data_final/modified_extracted_katalogos_mathimatwn_2025_2026_new_formatted_by_instructor.md")


@tool
def search_sectors_and_labs(query: str) -> str:
    """Χρησιμοποιήστε αυτό το εργαλείο για να βρείτε πληροφορίες σχετικά με το πώς το τμήμα χωρίζεται σε τομείς και τι εργαστήρια διαθέτουν καθώς και τους διευθυντές των εργαστηρίων. 
    Αυτό το εργαλείο δεν παρέχει πληροφορίες για μαθήματα, στοιχεία επικοινωνίας (αριθμούς τηλεφώνου, email) ή γενικές πληροφορίες για το τμήμα και το κτίριο, τη διοίκηση, τη γραμματεία, τους καθηγητές/διδακτικό προσωπικό (σύντομα βιογραφικά)."""
    return search_expert_knowledge(query, "ceid_chatbot/data_final/sectors_and_labs.md")

@tool
def search_sectors_and_professors(query: str) -> str:
    """Χρησιμοποιήστε αυτό το εργαλείο για να βρείτε πληροφορίες σχετικά με το πώς το τμήμα χωρίζεται σε τομείς και ποιός καθηγητής ανήκει σε κάθε τομέα μαζί με ένα σύντομο βιογραφικό.διαθέτει επίσης και τους διευθυντές των τομέων. 
    Αυτό το εργαλείο δεν παρέχει πληροφορίες για μαθήματα, στοιχεία επικοινωνίας (αριθμούς τηλεφώνου, email) ή γενικές πληροφορίες για το τμήμα και το κτίριο, τη διοίκηση, τη γραμματεία και για  το διδακτικό προσωπικό (σύντομα βιογραφικά)."""
    return search_expert_knowledge(query, "ceid_chatbot/data_final/sectors_and_professors.md")

@tool
def search_sectors_and_teaching_staff(query: str) -> str:
    """Χρησιμοποιήστε αυτό το εργαλείο για να βρείτε πληροφορίες σχετικά με το πώς το τμήμα χωρίζεται σε τομείς και ποιός  ΕΔΙΠ (Εργαστηριακό Διδακτικό Προσωπικό) ανήκει σε κάθε τομέα μαζί με ένα σύντομο βιογραφικό. 
    Αυτό το εργαλείο δεν παρέχει πληροφορίες για μαθήματα, στοιχεία επικοινωνίας (αριθμούς τηλεφώνου, email) ή γενικές πληροφορίες για το τμήμα και το κτίριο, τη διοίκηση, τη γραμματεία και για τους καθηγητές."""
    return search_expert_knowledge(query, "ceid_chatbot/data_final/sectors_and_teaching_staff.md")



@tool
def search_selective(query: str) -> str:
    """Χρησιμοποιήστε αυτό το εργαλείο για να βρείτε πληροφορίες ΜΟΝΟ σχετικά με το πώς τα μαθήματα επιλογής χωρίζονται σε κατευθύνσεις,ποιές κατευθύνσεις υπάρχουν,ποιές ομάδες επιλογής υπάρχουν, τι περιλαμβάνουν και πως μπορώ να επιλέξω μαθήματα συνδυαστικά από αυτές.
    Αυτό το εργαλείο δεν παρέχει πληροφορίες για μαθήματα, στοιχεία επικοινωνίας (αριθμούς τηλεφώνου, email) ή γενικές πληροφορίες για το τμήμα και το κτίριο, τη διοίκηση, τη γραμματεία, τους καθηγητές/διδακτικό προσωπικό (σύντομα βιογραφικά) και πώς το τμήμα χωρίζεται σε τομείς και τι εργαστήρια διαθέτουν."""
    return search_expert_knowledge(query, "ceid_chatbot/data_final/selective.md")

@tool
def search_selective_K(query: str) -> str:
    """Χρησιμοποιήστε αυτό το εργαλείο για να βρείτε ΜΟΝΟ πληροφορίες όπως σε ποιές  κατευθύνσεις και ομάδες ανήκει ένα μαθήματα επιλογής!
    Αυτό το εργαλείο δεν παρέχει πληροφορίες για μαθήματα, στοιχεία επικοινωνίας (αριθμούς τηλεφώνου, email) ή γενικές πληροφορίες για το τμήμα και το κτίριο, τη διοίκηση, τη γραμματεία, τους καθηγητές/διδακτικό προσωπικό (σύντομα βιογραφικά) και πώς το τμήμα χωρίζεται σε τομείς και τι εργαστήρια διαθέτουν.
    """
    return search_expert_knowledge(query, "ceid_chatbot/data_final/selective_courses_associated_with_K.md")



university_tools = [search_administration, search_building_instructions, search_general_info, search_communication_info, search_core_courses, search_teaching_courses, search_sectors_and_labs, search_sectors_and_professors, search_sectors_and_teaching_staff, search_selective, search_selective_K
]