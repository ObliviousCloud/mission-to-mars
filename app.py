# Import flask and pymongo
from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import pymongo
import scrape_mars



app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)


@app.route("/")
def home():

	mars = mongo.db.mars.find_one()
	return render_template("index.html", data=mars)

@app.route("/scrape")
def scrape():
	#run scraped function
	mars = mongo.db.mars
	marsdata = scrape_mars.scrape()
	mars.update({}, marsdata, upsert=True)
	return redirect("/", code=302)
	

if __name__ == "__main__":
	app.run(debug=True)

	
