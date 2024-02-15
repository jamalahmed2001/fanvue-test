from openai import OpenAI
client = OpenAI(api_key="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")



mentioned_preferences = set()
def extract_preferences(message):
    global mentioned_preferences
    response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": f"Extract personal preferences and details from this message: \"{message}\". List each detail with a star emoji at the beginning."}],
    stream=True,
    )

    reply = ''
    for chunk in response:
        
        if chunk.choices[0].delta.content is not None:
            detail = chunk.choices[0].delta.content.strip()
            # print(chunk.choices[0].delta.content, end="")
            reply+= detail + ' '
    reply = reply.strip('.')
    if ' '.join(reply.split(' ')[-2:]) in mentioned_preferences:
        print('No new details')
    else:
        print(reply)
        mentioned_preferences.add(' '.join(reply.split(' ')[-2:]))

while True:
    msg = input('Enter message: ')
    (extract_preferences(msg))


