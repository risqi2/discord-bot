import random

def handle_message(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'hey there'
    
    if p_message == 'roll':
        return str(random.randint(1,6))
    
    if p_message == '!help':
        return "This is help message"
    