from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    if not 'gold' in session:
        session['gold'] = 0
    if not 'activities' in session:
        session['activities'] = []
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    buildings = {
        'farm':random.randint(5,10),
        'casino':random.randint(-50,50),
        'cave':random.randint(0,30),
        'house':random.randint(0,5)
    }
    if request.form['building'] in buildings:
        print buildings[request.form['building']]
    return redirect('/')


if __name__ == '__main__':
  app.run(debug = True)


"""
Explain line 24!
When the user clicks the Farm button, the server 
processes the form and the value of farm prints
 to the terminal. Line 24 request.form is how the 
 information is gathered.

"""
