from flask import Flask, request, jsonify
import random

app = Flask(__name__)

responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm just a bot, but I'm here to help!", "Doing great, thanks for asking!"],
    "bye": ["Goodbye!", "See you soon!", "Take care!"]
}

@app.route("/chat", methods=["GET"])
def chatbot():
    message = request.args.get("message", "").lower()
    for key in responses:
        if key in message:
            return jsonify({"response": random.choice(responses[key])})
    return jsonify({"response": "I'm not sure how to respond to that."})

if __name__ == "__main__":
    from os import environ
    app.run(host="0.0.0.0", port=int(environ.get("PORT", 5000)))