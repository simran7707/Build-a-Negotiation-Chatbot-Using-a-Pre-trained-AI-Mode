import random

def negotiate(user_input, bot_response, state):
    
    base_price = 100
    discount_threshold = 10
    
    
    proposed_price = extract_price_from_input(user_input)
    
    
    if proposed_price:
        state.user_proposed_price = proposed_price
    
    
    if state.user_proposed_price:
        if state.user_proposed_price >= base_price - discount_threshold:
            
            state.counteroffer_made = False
            return f"Deal accepted at ${state.user_proposed_price}!"
        else:
            
            state.counteroffer_made = True
            counteroffer = base_price - random.randint(5, discount_threshold)
            state.user_proposed_price = counteroffer
            return f"Our counteroffer is ${counteroffer}. Does that work for you?"
    else:
       
        if "discount" in user_input.lower():
            return "We can offer you a 10% discount. Does that sound good?"
        else:
            return "Could you please provide a proposed price or ask for a discount?"

def extract_price_from_input(user_input):
    
    words = user_input.split()
    for word in words:
        if word.startswith('$') and word[1:].isdigit():
            return int(word[1:])
        elif word.isdigit():
            return int(word)
    return None
