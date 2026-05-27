import re

def detect_pii(text):

    patterns = [

        r"\b\d{12}\b",
        r"\b\d{16}\b",
        r"\S+@\S+\.\S+",
        r"\b\d{10}\b"

    ]

    for pattern in patterns:

        if re.search(pattern, text):
            return True

    return False