from flask import Flask, render_template, request
import csv, sqlite3
# Check interpreter is set to 3.11.9 on VSCode - otherwise it wont import flask properly
# We will use the flask app to create a framework for the webpage (so we can use Python, HTML, CSS together)

app = Flask(__name__) #creates an application in flask

@app.route("/") # this is the default route for the webpage



def homepage():
    return render_template("index.html", show_element="none", show_results=" ") # this returns the HTML file so it is presented to the user




@app.route("/search", methods=["GET", "POST"]) # this function will receive the form data

def searchCars():

    selectedcars = []

    reqs = []

    if request.method == "POST":

        make = request.form.get("make-type")
        model = request.form.get("model-type")
        date = request.form.get("production-type")
        colour = request.form.get("colour-type")
        location = request.form.get("location-type")

        reqs.append(make)
        reqs.append(model)
        reqs.append(date)
        reqs.append(colour)
        reqs.append(location)

        with open ('static/cars.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)

            for row in reader:
                item = row[2]
                item = item[6:10]
                print(item)
                
                if (row[0] == make or make == "N") and (row[1] == model or model == "N") and (item == date or date == "N") and (row[3] == colour or colour == "N") and (row[4] == location or location == "N"):
                    selectedcars.append(row)

  
        if len(selectedcars) != 0:

            return render_template("index.html", show_element="none", show_results=f"{selectedcars}")
        else:

            return render_template("index.html", show_element="block", show_results=" ")


if __name__ == "__main__":
    app.run()

# WHEN RUNNING - run as normal then click on the link 
# which says "running on http://127........." which should open the webpage



   



    