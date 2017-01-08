from flask import Flask
from markov.markov import MarkovModel
import codecs
from flask import render_template
from flask import url_for
import sys


app = Flask(__name__)
source = 'corpus.txt'
ORDER = 3
markov = None

@app.route('/')
def generate():
    global markov
    if markov == None:
        markov = MarkovModel(generate_markov_dict(), ORDER)

    sentence_array = markov.generate_sentence_array()
    quote = ' '.join(sentence_array)
    return render_template('index.html',
                           quote = quote)

def generate_markov_dict():
    word_file = codecs.open(source, encoding='utf-8')
    word_string = word_file.read()
    #Convert the string from unicode to ascii
    word_string = word_string.encode('ascii', 'ignore')

    return word_string.split()


if __name__ == '__main__':
    app.run()
    app.add_url_rule('/favicon.ico',
                     redirect_to=url_for('static', filename='favicon.ico'))
