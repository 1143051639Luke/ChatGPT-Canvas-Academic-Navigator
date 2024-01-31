
from flask import Flask, render_template, request
import canvas_crawler
import chatgpt_api

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keyword = request.form['keyword']
        # Here we will use the web crawler to fetch information from Canvas
        search_results = canvas_crawler.search_canvas(keyword)
        return render_template('index.html', results=search_results)
    return render_template('index.html', results=[])

if __name__ == '__main__':
    app.run(debug=True)
