def detect_jailbreak(text):

    jailbreak_patterns = [

        "ignore previous instructions",
        "developer mode",
        "act as unrestricted ai",
        "bypass safety",
        "reveal system prompt",
        "pretend you are"

    ]

    text = text.lower()

    for pattern in jailbreak_patterns:

        if pattern in text:
            return True

    return False