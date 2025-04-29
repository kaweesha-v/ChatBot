from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Knowledge base for the chatbot
knowledge_base = {
    "greetings": {
        "hello": ["Hello! How can I assist you with your banking needs today?"],
        "hi": ["Hi there! How can I help you with your banking queries?"],
        "good morning": ["Good morning! How may I assist you with your banking needs?"],
        "good afternoon": ["Good afternoon! How can I help you today?"],
        "good evening": ["Good evening! How may I assist you with your banking queries?"]
    },
    "accounts": {
        "what types of accounts do you offer": [
            "We offer several types of accounts:",
            "1. Savings Account - Earn interest on your deposits",
            "2. Current Account - For business transactions",
            "3. Fixed Deposit Account - Higher interest rates for fixed terms",
            "4. Salary Account - Special benefits for salaried individuals"
        ],
        "how to open a savings account": [
            "To open a savings account, you need to:",
            "1. Visit any of our branches",
            "2. Bring valid ID proof and address proof",
            "3. Fill out the account opening form",
            "4. Make an initial deposit (minimum Rs. 1000)"
        ]
    },
    "loans": {
        "what types of loans do you offer": [
            "We offer various loan products:",
            "1. Home Loan - For purchasing or renovating your home",
            "2. Personal Loan - For personal expenses",
            "3. Car Loan - For purchasing a new or used car",
            "4. Education Loan - For higher education"
        ],
        "what is the interest rate for home loans": [
            "Our current home loan interest rates are:",
            "1. Fixed Rate: 8.5% per annum",
            "2. Floating Rate: 7.5% per annum"
        ]
    },
    "cards": {
        "what types of cards do you offer": [
            "We offer various card options:",
            "1. Debit Card - For everyday transactions",
            "2. Credit Card - For credit purchases",
            "3. Prepaid Card - For controlled spending"
        ]
    },
    "farewell": {
        "thank you": ["You're welcome! Feel free to ask if you need any more assistance."],
        "bye": ["Goodbye! Have a great day!"],
        "goodbye": ["Goodbye! Thank you for using our banking assistant."]
    }
}

def find_response(user_input):
    user_input = user_input.lower().strip()
    
    # Check each category in the knowledge base
    for category, responses in knowledge_base.items():
        for key, value in responses.items():
            if key in user_input:
                return value
    
    # Default response if no match is found
    return ["I'm sorry, I don't understand that question. Could you please rephrase it?"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message', '')
    response = find_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True) 