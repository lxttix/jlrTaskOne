# THIS IS THE PYTHON FILE

from flask import Flask, render_template, request

# Check interpreter is set to 3.11.9 on VSCode - otherwise it wont import flask properly
# We will use the flask app to create a framework for the webpage (so we can use Python, HTML, CSS together)

app = Flask(__name__) #creates an application in flask

@app.route("/") # this is the default route for the webpage
def homepage():
    return render_template("index.html") # this returns the HTML file so it is presented to the user

@app.route("/search", methods=["GET", "POST"]) # this function will receive the form data
def searchCars():
    if request.method == "POST":
        dataType = request.form.get("data-type")
        dataValue = request.form.get("data-value")
    return(str(dataType) + " " + str(dataValue))

if __name__ == "__main__":
    app.run()

# WHEN RUNNING - run as normal then click on the link 
# which says "running on http://127........." which should open the webpage