from flask import Flask, request
from googlesearch import search
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=["POST"])
def bot():
    try:
        # User input from the incoming message
        user_msg = request.values.get('Body', '').lower()

        # Creating object of MessagingResponse
        response = MessagingResponse()

        # Formulating the search query (e.g., limiting to a specific site)
        q = f"{user_msg} site:geeksforgeeks.org"

        # Searching and storing URLs (limited to top 3 results)
        search_results = list(search(q, num_results=3))

        # If no results are found
        if not search_results:
            response.message("Sorry, I couldn't find any results for your query.")
        else:
            # Building the response message
            response.message(f"--- Top 3 results for '{user_msg}' ---")
            for result in search_results:
                response.message(result)

    except Exception as e:
        # Error handling
        response.message("Oops! Something went wrong. Please try again later.")
        print(f"Error: {e}")  # Log the error for debugging

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
