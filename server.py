from flask import Flask, render_template, request
import data

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)


@app.route('/')
def index():
    """Homepage"""

    return render_template("index.html")

@app.route('/word-cloud')
def make_word_cloud():
    """Makes the word cloud!"""

    pasted_text = request.args.get('text-to-cloud')
    color = request.args.get('color')

    if pasted_text:
        word_count = data.count_words(data.get_words(str(pasted_text)))
    else:
        word_count = data.count_words(data.get_words('dolls_house.txt'))

    return render_template("word_cloud.html",
                           color=color,
                           words=word_count,
                           word_count=len(word_count))


if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)
