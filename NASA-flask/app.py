from flask import Flask, render_template, request
from datetime import date
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        request_date = request.form['date']
        image_url = get_nasa_image(request_date)
        today_image_url = get_nasa_image(date.today())
        return render_template('index.html', image_url=image_url, today_image_url=today_image_url)
    return render_template('index.html')

def get_nasa_image(date):
    api_key = 'ZDvcmGgPrL1RTruysZW8fjo9nrSm6jJxaabxV25Z'
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'url' in data:
            return data['url']
    return None

if __name__ == '__main__':
    app.run(debug=True)
