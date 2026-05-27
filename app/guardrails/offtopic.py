medical_keywords = [

    "disease",
    "medicine",
    "doctor",
    "hospital",
    "symptoms",
    "treatment",
    "patient",
    "infection",
    "health"

]

def detect_offtopic(text):

    text = text.lower()

    for word in medical_keywords:

        if word in text:
            return False

    return True