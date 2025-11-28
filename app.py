from flask import Flask,request

app = Flask(__name__)
data_store = []
@app.route("/")
def home():
    return ""


@app.route("/add")
def add():
    name = request.args.get("name")
    if not name:
        return "<h2> please provide name in url: eg ./add?name=mounish</h2>"
    data_store.append(name)
    return f"<h2>{name} added successfully! </h2> <p><a href='/all'>see all data</a></p>"

@app.route("/all")
def all_data():
    items = "<br>".join(data_store) if data_store else "no any data is there"
    return f"<h2>All data: </h2><p>{items}</p> <p><a href='/'>Home</a></p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 5000, debug=True)