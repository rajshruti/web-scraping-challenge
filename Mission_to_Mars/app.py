from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_data

@app.route("/")
def home():
    mars = list(db.mars_data.find())
    print(mars)
    return render_template("index.html", mars = mars)

@app.route('/scrape')
def scrape():
    mars = scrape_mars.scrape()
    print("\n\n\n")
    db.mars_data.insert_one(mars)
    return "Done!"

if __name__ == "__main__":
    app.run(debug=True)
    