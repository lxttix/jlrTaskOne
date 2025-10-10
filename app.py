from flask import Flask, render_template, request
from flask import Response
import csv, sqlite3
import io
import requests
from lxml import etree
from html2image import Html2Image
# Check interpreter is set to 3.11.9 on VSCode - otherwise it wont import flask properly
# We will use the flask app to create a framework for the webpage (so we can use Python, HTML, CSS together)

app = Flask(__name__) #creates an application in flask

def preview():
    
    page_html = requests.get(request.args['url']).text

    parser = etree.HTMLParser()
    tree = etree.parse(io.StringIO(page_html), parser)

    head = tree.xpath('/html/head')[0]
    title = head.xpath('meta[@property="og:title"]/@content')[0]
    description = head.xpath('meta[@property="og:description"]/@content')[0]

    preview_html = render_template('card.html', title=title, excerpt=description)

    hti = Html2Image()
    hti.screenshot(html_str=preview_html, save_as='preview.png')

    with open('preview.png', 'rb') as f:
        preview_img = f.read()

    return Response(preview_img, mimetype='image/png')

@app.route("/") # this is the default route for the webpage
def homepage():
    return render_template("index.html", show_element="none", show_results=" ") # this returns the HTML file so it is presented to the user
    #return render_template("details.html")



@app.route("/search", methods=["GET", "POST"]) # this function will receive the form data
def searchCars():

    models = []
    makes = []
    dates = []
    colours = []
    locations = []


    if request.method == "POST":

        make = request.form.get("make-type")
        model = request.form.get("model-type")
        date = request.form.get("production-type")
        colour = request.form.get("colour-type")
        location = request.form.get("location-type")


        with open ('static/cars.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)

            for row in reader:
                item = row[2]
                item = item[6:10]
    
                
                if (row[0] == make or make == "N") and (row[1] == model or model == "N") and (item == date or date == "N") and (row[3] == colour or colour == "N") and (row[4] == location or location == "N"):
                    makes.append(row[0])
                    models.append(row[1])
                    dates.append(item)
                    colours.append(row[3])
                    locations.append(row[4])

  
        if len(models) != 0:
            return render_template("index.html", show_element="none", models=models, makes=makes, dates=dates, colours=colours, locations=locations)
        else:
            return render_template("index.html", show_element="block", show_results=" ")
        
@app.route("/details/<detail>", methods=["GET", "POST"])
def showDetails(detail):
    result = detail.split("-")
    new = []
    for res in result:
        print(res)
        res = res.replace("&", " ")
        print(res)
        
        new.append(res)
        
        
    return render_template("details.html", results=new)
        



if __name__ == "__main__":
    app.run()

# WHEN RUNNING - run as normal then click on the link 
# which says "running on http://127........." which should open the webpage



   



    