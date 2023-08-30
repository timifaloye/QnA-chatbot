import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
    question = input("\033[34mWhat is your question?\n\033[0m")

    if question.lower() == "exit":
        print("\033[31mGoodbye!\033[0m")
        break

    completion = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions."},
            {"role": "user", "content": question}
        ]
    )
    response = completion.choices[0].message["content"]
    print("\033[32m" + response + "\n")
