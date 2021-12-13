# Web Scraping Homework - Mission to Mars



A web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

Web scraping is done using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Created Jupyter Notebook file called `mission_to_mars.ipynb` 

### NASA Mars News

* Scraped the [Mars News Site](https://redplanetscience.com/) and collected the latest News Title and Paragraph Text. 

### JPL Mars Space Images - Featured Image

* Visited the site for the Featured Space Image site [here](https://spaceimages-mars.com).

* Used splinter to navigate to the site to find the image url for the current Featured Mars Image 


### Mars Facts

* Visited the Mars Facts webpage [here](https://galaxyfacts-mars.com) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Used Pandas to convert the data to a HTML table string wiht the help of df2.to_html() and df2.to_html("mars_info_table.html")

### Mars Hemispheres

* Visited the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.

* The  image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name are saved in a Python dictionary 


## Step 2 - MongoDB and Flask Application

* A new HTML page is created with Mongo DB and Flask that displays all of the information that was scraped from the URLs above.

* Converted the Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` returning one Python dictionary containing all of the scraped data.

* A route called `/scrape`  is created importing `scrape_mars.py` script calling the  `scrape` function.

* Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.

* HTML file  `index.html` is created which displays  the mars data dictionary and display all of the data in the appropriate HTML elements.


- - -



© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
