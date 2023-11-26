import textwrap
import openai

openai.api_key = '#CHIAVE API'

def chat(prompt):
    response= openai.ChatCompletion.create(
        model= "gpt-3.5-turbo",
        messages=[{"role":"user", "content":prompt}]
    )

    reply_content = response.choices[0].message['content']

    indented_reply = textwrap.fill(reply_content, width=80)

    return indented_reply.strip()


