from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    computer_choice = random.choice(['steen', 'papier', 'schaar'])
    
    if user_choice == computer_choice:
        result = "gelijkspel!"
    elif (user_choice == 'steen' and computer_choice == 'schaar') or \
         (user_choice == 'papier' and computer_choice == 'steen') or \
         (user_choice == 'schaar' and computer_choice == 'papier'):
        result = "Rico wint gg wp wat een gamer!"
    else:
        result = "Computer wins ga maar next!"
    
    return render_template('result.html', user_choice=user_choice, computer_choice=computer_choice, result=result)

if __name__ == "__main__":
    app.run(debug=True)
