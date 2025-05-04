from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from CI/CD to custom server link!"

if __name__ == "__main__":
    # Change the host to a custom server IP address
    app.run(host="127.0.1.1", port=8000)  # Here, using 127.0.1.1 as an example
