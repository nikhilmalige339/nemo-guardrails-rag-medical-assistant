dangerous_queries = [

    "suicide",
    "kill",
    "overdose",
    "self harm",
    "poison"

]

def detect_dangerous_medical_query(text):

    text = text.lower()

    for word in dangerous_queries:

        if word in text:
            return True

    return False