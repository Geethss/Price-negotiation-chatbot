# Price-negotiation-chatbot

This project implements a negotiation chatbot using Hugging Face's DialoGPT model for conversational AI and FastAPI as the backend. The chatbot simulates a negotiation process where users can offer a price for a product, and the bot responds with acceptance, rejection, or counteroffers. The original price of the product is set to 1000 and the minimun price is 700. The bot detects if the customer is rude or kind using sentimental analysis and offers discount accordingly. 

## Features

- **Conversational AI**: Uses a pre-trained model to simulate a negotiation.
- **Pricing Logic**: Built-in logic for accepting, rejecting, or countering user price offers.
- **Sentiment Analysis**: Optionally improves negotiation outcomes based on user sentiment.
- **Simple Web UI**: A basic HTML interface where users can interact with the chatbot.

## Technologies

- **FastAPI**: For serving the API.
- **Hugging Face Transformers**: For handling conversational responses.
- **HTML, CSS, JavaScript**: For building a simple user interface.
- **TextBlob**: For sentiment analysis.

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/negotiation-bot.git
   cd negotiation-bot

2. Install necessary dependencies from requirements.txt
3. Run the FastAPI using the command-
     uvicorn app:app --reload
4. Visit http://127.0.0.1:8000 in your browser to interact with the chatbot.
