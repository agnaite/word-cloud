from flask import Flask, render_template
import data

app = Flask(__name__)


@app.route('/')
def index():
    """Word cloud"""

    word_count = data.count_words(data.get_words('dolls_house.txt'))

    return render_template("index.html",
                           words=word_count)


if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)
