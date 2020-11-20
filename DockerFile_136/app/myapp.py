from flask import Flask

app = Flask(__name__)

@app.route("/")
def test():
    return "<h1>Server working!></h1>"


if __name__ == "__main__":
    # application port inside the container is 8080
    app.run(host="0.0.0.0", port=int("8080"), debug=True)