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

@app.route('/flip', methods = ['POST'])
def flippy():
    session['deck'][int(request.form['card_index'])]['image'],session['deck'][int(request.form['card_index'])]['alternate']=session['deck'][int(request.form['card_index'])]['alternate'],session['deck'][int(request.form['card_index'])]['image']
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('deck')
    return redirect('/')
    
if __name__ == '__main__':
  app.run(debug = True)
