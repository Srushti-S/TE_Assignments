import random

greetings = ['Hello!', 'Hi!', 'Hey there!', 'Greetings!', 'Nice to see you!']
goodbyes = ['Goodbye!', 'See you later!', 'Bye!', 'Take care!']
help_responses = ['How may I assist you?', 'What can I do for you?', 'How can I help?']
problem_responses = ['I\'m sorry to hear that. Can you please tell me more about the problem?', 'Let me see if I can help. What seems to be the issue?', 'I\'ll do my best to help you. What\'s the problem?']
thankyou_responses = ['You are welcome!', 'No problem!', 'It was my pleasure!', 'Glad to help!']

def chatbot():
    print('Chatbot: ' + random.choice(greetings))
    while True:
        user_input = input('User: ')
        if 'hello' in user_input.lower() or 'hi' in user_input.lower() or 'hey' in user_input.lower():
            print('Chatbot: ' + random.choice(greetings))
        elif 'bye' in user_input.lower() or 'goodbye' in user_input.lower() or 'see you' in user_input.lower():
            print('Chatbot: ' + random.choice(goodbyes))
            break
        elif 'help' in user_input.lower() or 'support' in user_input.lower():
            print('Chatbot: ' + random.choice(help_responses))
        elif 'problem' in user_input.lower() or 'issue' in user_input.lower() or 'error' in user_input.lower():
            print('Chatbot: ' + random.choice(problem_responses))
        elif 'thank you' in user_input.lower() or 'thanks' in user_input.lower() or 'thankyou' in user_input.lower():
            print('Chatbot: ' + random.choice(thankyou_responses))
        else:
            print('Chatbot: I\'m sorry, I don\'t understand. Can you please rephrase your request?')

chatbot()
