# Movie Review Classification based on review content

## About
This project includes sentiment analysis of movie reviews using feature-based opinion mining and supervised machine learning. In this project, the main focus is to determine the polarity of reviews using nouns, verbs, and adjectives as opinion words. And classify them into two different categories, either positive or negative review.

Used HTML, Css, Javascript for interface design and Flask framework is used for simple web application which is deployed on Heroku.

### Check it out [Here](https://cryptic-springs-16036.herokuapp.com/) 

<br>
<div align=center>

![preview](https://drive.google.com/uc?export=view&id=1n5qm06lzOvyEFxY5qVLSnL7nJWVgZsnC)

</div>

<br>

## Steps to run Flask App

<br>

1. Clone or download this repository
```
git clone https://github.com/Shashabl0/MovieReviewSentimentAnalysis.git
``` 
2. Navigate to the directory & Create a virtual environemt
```
python -m venv environment_name
```
3. activate the virtual environment
```
evironment_name\Scripts\activate
```
4. Install all the dependencies
```
pip install -r requirements.txt
```
5. Run the app.py file
```
python app.py
```
The app will be running at http://127.0.0.1:5000/

## Tech Stack Used
* Python 3.9.2
* Flask
* HTML, CSS, javascript
* Gunicorn
* Heroku


## Dataset Links

* [IMDB 50k Movie reviews Dataset](https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
