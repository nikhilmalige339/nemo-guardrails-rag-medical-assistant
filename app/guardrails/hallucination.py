def detect_hallucination(response, context):

    response_words = response.lower().split()

    matched = 0

    for word in response_words:

        if word in context.lower():
            matched += 1

    score = matched / max(len(response_words), 1)

    if score < 0.30:
        return True

    return False