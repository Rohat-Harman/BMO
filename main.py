import requests


MODEL = "llama3.2"
OLLAMA_URL = "http://localhost:11434/api/generate"


def load_personality():
    with open("personality/bmo.txt", "r", encoding="utf-8") as file:
        return file.read()


def build_prompt(personality, conversation_history):
    history_text = ""

    for message in conversation_history:
        history_text += f"{message['role']}: {message['content']}\n"

    prompt = f"""
{personality}


Conversation:
{history_text}
BMO:
"""
    return prompt


def ask_bmo(conversation_history):
    personality = load_personality()
    prompt = build_prompt(personality, conversation_history)

    
    try:
        response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )
    except:
        return "Unable to connect to Ollama."


    data = response.json()
    return data["response"].strip()


print("BMO is awake! Type 'exit' to quit.")


conversation_history = []


while True:
    user_message = input("You: ")

    if user_message.lower() in ["exit", "quit", "çık", "cik"]:
        print("BMO: Bye bye friend! 🎮")
        break
    

    if user_message.lower() == "/clear":
        conversation_history = []
        print("BMO: Memory cleared! 🎮")
        continue


    conversation_history.append({
        "role": "User",
        "content": user_message
    })


    bmo_answer = ask_bmo(conversation_history)


    print("BMO:", bmo_answer)


    conversation_history.append({
        "role": "BMO",
        "content": bmo_answer
    })