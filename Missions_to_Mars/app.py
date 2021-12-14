from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import os
import pymongo


# Create an instance of Flask
app = Flask(__name__)
# app=Flask(__name__,template_folder='templates')


# Use PyMongo to establish Mongo connection
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

conn = 'mongodb://localhost:27017/mars_db'
client = pymongo.MongoClient(conn)
db=client.mars_db
db.mars_data.drop

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    #mars_data = mongo.db.collection.find_one()
    mars_data = mongo.db.mars_data.find_one()
    # Return template and data
    return render_template("index.html", mars_data=mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    mars_data=mongo.db.mars_data
    # Run the scrape function
    mars_data_scraped = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    # mongo.db.collection.update({}, mars_data, upsert=True)
    # mars_data.update({},mars_data_scraped,upsert=True)
    # mongo.db.mars_data.update({},mars_data_scraped,upsert=True)
    mars_data.insert_one(mars_data_scraped)
    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
