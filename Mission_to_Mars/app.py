from flask import Flask, render_template
import pymongo
import scrape_mars

app = Flask(__name__)

# Setup mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = pymongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    mars.update({}, mars_data, upsert = True)
    return "Done Scraping!"
    
if __name__ == "__main__":
    app.run()
    