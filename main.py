import openai
import os
from negotiation import negotiate 
import time


openai.api_key = ''# API 


class NegotiationState:
    def __init__(self):
        self.user_proposed_price = None
        self.counteroffer_made = False

def chat_with_bot(user_input, state):
    
    prompt = f"User: {user_input}\nBot:"
    
   
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use 'gpt-3.5-turbo'
            messages=[{"role": "user", "content": user_input}],
            max_tokens=150,
            temperature=0.9,
        )
        return response.choices[0].message['content'].strip()
    except openai.error.RateLimitError as e:
        print("Rate limit exceeded. Please wait and try again later.")
        time.sleep(60)  # Wait for 60 seconds before retrying
        return "Sorry, I am currently experiencing high traffic. Please try again in a minute."

def main():
    state = NegotiationState()
    print("Welcome to the negotiation chatbot!")
    print("You can start by proposing a price or asking for a discount.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        
        bot_response = chat_with_bot(user_input, state)
        
       
        negotiation_response = negotiate(user_input, bot_response, state)
        
        print("Bot:", negotiation_response)

if __name__ == "__main__":
    main()
