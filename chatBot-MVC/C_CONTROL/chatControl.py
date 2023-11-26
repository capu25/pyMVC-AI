from M_MODEL.chatBot import chat


def askQuestion(message):
    response = chat(message)
    return response
