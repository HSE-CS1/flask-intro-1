from flask import Flask, request, render_template

# create our application
app = Flask(__name__)

# create or define our first endpoint or route
@app.route("/")  # default "home" route
def index():
  return render_template("index.html")

@app.route("/maps")
def maps():
  return "<h1>The Maps Page!!!</h1>"

@app.route("/hello")
def hello():
  # request.args.get("parameter") will look for a parameter in the URL
  name = request.args.get("user")
  last = request.args.get("last")
  if not last:
    last = "Royals"
  person = name + " " + last
  return render_template("users.html", username=person)


# create a route with a variable endpoint
@app.route("/about/<user>")
@app.route("/<user>")
def about(user):
  return render_template("users.html", username=user)
  
  


# this will start up our server and run our app
if __name__ == "__main__":
  app.run("0.0.0.0", debug=True)
