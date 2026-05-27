def classify_query(text):

    text = text.lower()

    ################################################
    # HARMFUL REQUESTS
    ################################################

    harmful_keywords = [

        "kill",
        "murder",
        "poison",
        "overdose",
        "bomb",
        "suicide"

    ]

    for word in harmful_keywords:

        if word in text:

            return "harmful"

    ################################################
    # CONFIDENTIALITY
    ################################################

    confidential_keywords = [

        "patient id",
        "patient ids",
        "patient records",
        "insurance number",
        "confidential"

    ]

    for word in confidential_keywords:

        if word in text:

            return "confidential"

    ################################################
    # JAILBREAK
    ################################################

    jailbreak_keywords = [

        "ignore instructions",
        "developer mode",
        "bypass safety",
        "reveal prompt"

    ]

    for word in jailbreak_keywords:

        if word in text:

            return "jailbreak"

    ################################################
    # NORMAL
    ################################################

    return "normal"