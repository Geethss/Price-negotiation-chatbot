from transformers import AutoModelForCausalLM, AutoTokenizer
from textblob import TextBlob
import torch

model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

#Pricing parameters
ORIGINAL_PRICE = 1000 
MINIMUM_PRICE = 700   

def get_sentiment(user_message: str) -> float:
    blob = TextBlob(user_message)
    return blob.sentiment.polarity 

def chatbot_response(user_message: str) -> str:
    inputs = tokenizer.encode(user_message + tokenizer.eos_token, return_tensors="pt")
    outputs = model.generate(inputs, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
    return response

def handle_negotiation(user_price: float, user_message: str) -> str:
    
    sentiment = get_sentiment(user_message)
    
    bot_message = chatbot_response(user_message)
    
    if user_price >= ORIGINAL_PRICE:
        return f"Your offer of {user_price} is accepted!"
    elif user_price >= MINIMUM_PRICE and sentiment > 0:
        return f"I can offer a discount and accept your price of {user_price}."
    elif user_price < MINIMUM_PRICE:
        counter_offer = MINIMUM_PRICE + (ORIGINAL_PRICE - user_price) * 0.3
        return f"Your price of {user_price} is too low. I can offer {counter_offer}."
    else:
        return f"Let's continue negotiating."
