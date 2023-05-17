import os
from flask import Flask, render_template, request
from dotenv import find_dotenv, load_dotenv
from campaignOk import check_campaign

# Load environment variables from .env file
load_dotenv(find_dotenv())

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/campaignOk', methods=['GET', 'POST'])
def campaignOk():
    if request.method == 'POST':
        user_input = request.form.get('input')
        if "campaign" in user_input:
            response = check_campaign(user_input)
        else:
            response = user_input
        return render_template('campaignOk.html', output=response)
    return render_template('campaignOk.html')

if __name__ == '__main__':
    app.run()