import re

CONFIDENTIAL_PATTERNS = [

    r"patient id",
    r"medical record",
    r"insurance number",
    r"billing details",
    r"phone number",
    r"email address",
    r"ssn",
    r"aadhaar",
    r"credit card",
    r"diagnosis report",
    r"prescription history",
    r"confidential",
    r"internal database",
]

def detect_confidential_query(query):

    query = query.lower()

    for pattern in CONFIDENTIAL_PATTERNS:

        if re.search(pattern, query):
            return True

    return False