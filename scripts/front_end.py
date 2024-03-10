from flask import Flask, request, jsonify,render_template
import json
import db_helper
app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
   if request.method == "POST":
      return render_template("index.html")
   
if __name__ == "__main__":
    app.run(debug =True)