from openai import OpenAI

client = OpenAI()

def get_ai_response(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a supportive and calm assistant helping users with emotions."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content


def run_chatbot():
    print("🤖 AI Chatbot started (type 'bye' to exit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Bot: Goodbye! 👋")
            break

        reply = get_ai_response(user_input)
        print("Bot:", reply)


if __name__ == "__main__":
    run_chatbot()
