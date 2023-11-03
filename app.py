from flask import Flask, render_template, request, jsonify

app = Flask(__name)

# Define a simple chatbot response function
def chatbot_response(user_message):
    # Replace with your chatbot logic
    return "Hello! I'm a chatbot."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json['message']
    bot_response = chatbot_response(user_message)
    return jsonify({'message': bot_response})

if _name_ == '_main_':
    app.run(debug=True)
