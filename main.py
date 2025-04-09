from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def webhook():
    signal = request.args.get("signal") or request.json.get("signal")
    with open("signal.txt", "w") as f:
        f.write(signal)
    return f"Received: {signal}"

app.run(host="0.0.0.0", port=8080)
