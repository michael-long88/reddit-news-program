from flask import Flask, render_template
import news

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/news')
def get_news():
    submissions = news.get_top_10()
    return render_template('news.html', submissions=submissions)


if __name__ == '__main__':
    app.run()
