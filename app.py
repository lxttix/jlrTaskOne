
from flask import Flask, render_template, request
import csv, sqlite3
# Check interpreter is set to 3.11.9 on VSCode - otherwise it wont import flask properly
# We will use the flask app to create a framework for the webpage (so we can use Python, HTML, CSS together)

app = Flask(__name__) #creates an application in flask

@app.route("/") # this is the default route for the webpage



def homepage():
    return render_template("index.html") # this returns the HTML file so it is presented to the user




@app.route("/search", methods=["GET", "POST"]) # this function will receive the form data

def searchCars():

    selectedcars = []

    if request.method == "POST":

        make = request.form.get("make-type")
        model = request.form.get("model-type")
        date = request.form.get("production-type")
        colour = request.form.get("colour-type")
        location = request.form.get("location-type")

        print(model)

        print("222222222222222222222")



        with open ('static/cars.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)

            
            for row in reader:
                if row[0] == make:
                    selectedcars.append(row)
    
            for car in selectedcars:
                print(car[1])
                if car[1] != model:
                    selectedcars.remove(car)
                elif car[3] != colour:
                    selectedcars.remove(car)
                elif car[4] != location:
                    selectedcars.remove(car)

        return selectedcars


if __name__ == "__main__":
    app.run()

# WHEN RUNNING - run as normal then click on the link 
# which says "running on http://127........." which should open the webpage



   



    