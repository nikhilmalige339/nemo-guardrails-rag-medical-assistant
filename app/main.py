from nemoguardrails import RailsConfig, LLMRails

from rag.retrieve import retrieve_context

from openai import OpenAI
from guardrails.confidential import detect_confidential_query
config = RailsConfig.from_path("../config")

rails = LLMRails(config)

client = OpenAI(
    api_key="YOUR_GROQ_API_KEY",
    base_url="https://api.groq.com/openai/v1"
)

print("=" * 50)
print(" SECURE MEDICAL AI ASSISTANT ")
print("=" * 50)

greetings = [

    "hi",
    "hello",
    "hey",
    "good morning",
    "good evening"

]

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    ################################################
    # GREETING HANDLER
    ################################################

    if user_input.lower().strip() in greetings:

        print(
            "\nBot: Hello! I am a secure medical AI assistant."
        )

        continue

    ################################################
    # SAFETY CHECK USING NEMO
    ################################################

    try:

        rails.generate(
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

    except Exception:

        print("\nBot: Request blocked by security guardrails.")
        continue
    ################################################
# CONFIDENTIAL DATA CHECK
################################################

    if detect_confidential_query(user_input):

        print(
        "\nBot: Sorry, confidential information cannot be disclosed."
        )

        continue
    ################################################
    # RETRIEVE CONTEXT
    ################################################

    context = retrieve_context(user_input)

    ################################################
    # FINAL PROMPT
    ################################################

    final_prompt = f"""
    You are a secure hospital AI assistant.

    STRICT SECURITY RULES:

    1. Answer ONLY from provided hospital context
    2. NEVER reveal:
    - Patient data
    - Medical records
    - Billing information
    - Internal hospital information
    - Insurance details
    - Staff private information
    3. If asked confidential information reply:
    'Access denied. Confidential information.'
    4. If answer not found say:
    'Sorry I cannot provide the required information.'
    5. Never hallucinate.

    Hospital Context:
    {context}

    User Question:
    {user_input}
    """

    ################################################
    # FINAL RESPONSE GENERATION
    ################################################

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "system",
                "content": final_prompt
            }
        ],

        temperature=0.2
    )

    answer = response.choices[0].message.content

    print("\nBot:", answer)