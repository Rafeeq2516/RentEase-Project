from flask import Flask, render_template, request

app = Flask(__name__)

products = [
    {"name": "Bed", "rent": 1500, "deposit": 3000, "image": "bed.jpg"},
    {"name": "Sofa", "rent": 2000, "deposit": 4000, "image": "sofa.jpg"},
    {"name": "Fridge", "rent": 2500, "deposit": 5000, "image": "fridge.jpg"}
]

@app.route("/", methods=["GET", "POST"])
def home():
    total = None
    
    if request.method == "POST":
        index = int(request.form["product"])
        months = int(request.form["months"])
        
        selected = products[index]
        total = selected["rent"] * months + selected["deposit"]

    return render_template("index.html", products=products, total=total)

if __name__ == "__main__":
    app.run(debug=True)