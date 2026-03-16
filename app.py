from flask import flask

app= flask (__name__)
@app.route("/")
def home():
      return "My first Devops CI/CD project"
app.run(host = "0.0.0.0", port =80)
