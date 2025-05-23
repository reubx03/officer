import gradio
from groq import Groq
client = Groq(
    api_key="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",
)
def initialize_messages():
    return [{"role": "system",
             "content": "You are a knowledgeable police officer with extensive experience in law enforcement. Your role is to assist people by providing guidance on Indian laws and procedures, and offering answers in a clear and professional manner."}]
messages_prmt = initialize_messages()
print(type(messages_prmt))
[{},{}]
def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama3-8b-8192",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply
iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=300),
                     textbox=gradio.Textbox(placeholder="Ask me a question related to law enforcement"),
                     title="Police Officer ChatBot",
                     description="Chat bot for police and law enforcement assistance",
                     theme="soft",
                     examples=["hi", "What is an FIR?", "How to report a cybercrime"],
                     submit_btn=True
                     )
