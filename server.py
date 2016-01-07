from flask import Flask, render_template, request, redirect, session
from cards import Cards
app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    try:
        session['deck']
    except:
        #session['deck'] after this except should be a list with dictionaries of cards with in it!
        session['deck'] = Cards().shuffle().deck
    return render_template('index.html')



if __name__ == '__main__':
  app.run(debug = True)
