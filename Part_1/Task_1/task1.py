from openai import OpenAI
client = OpenAI(api_key="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")


def extract_preferences(message):
    response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": f"Extract personal preferences and details from this message: \"{message}\". List each detail with a star emoji at the beginning."}],
    stream=True,
    )

    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
        else:
            print("\n no new details.")

while True:
    msg = input('Enter message: ')
    (extract_preferences(msg))





