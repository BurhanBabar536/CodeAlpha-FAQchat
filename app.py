from flask import Flask, request, jsonify, render_template
from matcher import get_best_answer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').strip()

    if not user_message:
        return jsonify({'reply': 'Please enter a question.', 'score': 0.0})

    answer, score = get_best_answer(user_message)
    return jsonify({'reply': answer, 'score': score})

if __name__ == '__main__':
    app.run(debug=True)