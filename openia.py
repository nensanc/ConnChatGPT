from openai import OpenAI

client = OpenAI(api_key='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')
GPT_MODEL = "gpt-4-1106-preview" #"gpt-3.5-turbo-1106"

chat_history = []

while True:
    prompt = input("Enter a prompt: ")
    if prompt == "exit":
        break
    else:
        chat_history.append({"role": "user", "content": prompt})

        response = client.chat.completions.create(
            model=GPT_MODEL,
            messages=chat_history,
            max_tokens=150,
        )

        full_reply_content = response.choices[0].message.content  # extract the message

        chat_history.append({"role": "assistant", "content": full_reply_content})
        # print the time delay and text received
        print(f"GPT: {full_reply_content}")