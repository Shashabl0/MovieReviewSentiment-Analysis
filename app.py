from flask import Flask,render_template,request,redirect,url_for
from flask.helpers import url_for
from general import *



app = Flask(__name__)



txt = ["Review is Negative", "Review is Positive", "Please write a little more"]

pred = 3
review = ""
count = 0


class msg():
    def __init__(self, n_review, nflag):
        self.review = n_review
        self.flag = nflag


@app.route("/")
def home():
    global review
    
    if review != "":
        msgs = msg(review,pred)
        review = ""
    else:
        msgs = msg("",3)
    # print("final ",msgs.flag)
    return render_template('index.html' , html_file = "main.html", msg = msgs)

@app.route("/submit",methods=["POST"])
def submit():
    text = request.form.get("review")
    global pred
    global review

    if len(text) >= 20:
        prediction = movie_sentiment(text)
        print(txt[prediction])
        
        pred = prediction
        review = text
    
    elif len(text) < 20:
        pred = 2
        review = text
        # print("Please write a little more")
    
    return redirect(url_for("home"))


@app.route("/about")
def about():
    global review
    review = ""
    msgs = msg("",2)
    render_template('index.html',html_file = "" ,msg = msgs )
    return render_template('index.html',html_file = 'about.html' ,msg = msgs )


if __name__ == "__main__":
    app.run(debug=True)
