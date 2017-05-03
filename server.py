from flask import Flask, render_template
import data

app = Flask(__name__)


@app.route('/')
def index():
    """Homepage"""

    return render_template("index.html")

@app.route('/word-cloud')
def make_word_cloud():
    """Makes the word cloud!"""

    word_count = data.count_words(data.get_words('dolls_house.txt'))

    return render_template("word_cloud.html",
                           words=word_count)


if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)
