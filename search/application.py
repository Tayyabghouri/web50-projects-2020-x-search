from flask import Flask , render_template, url_for


app = Flask(__name__)

@app.route("/")
@app.route("/google")
def google():
    return render_template("google.html")

@app.route("/googleImage")
def googleImage():
    return render_template("googleimagesearch.html")  

@app.route("/advancesearch")
def advancesearch():
    return render_template("advancesearch.html")     

if __name__ == '__main__':
    app.run(debug=True)
