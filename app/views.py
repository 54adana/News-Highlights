from flask import render_template
from app import app
from .request import get_news

# Views


@app.route('/')
def index():


    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    Sports = get_news('sports')
    Business = get_news('business')
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title, sports = Sports, business = Business)

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)
