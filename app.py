from flask import Flask
import markov.markov
import codecs
from flask import render_template
from flask import url_for


app = Flask(__name__)
source = 'corpus.txt'
order = 3
markov_dict = {}

@app.route('/')
def generate():
    global markov_dict
    if markov_dict == {}:
        generate_markov_dict()

    sentence_array = markov.markov.gen_words(markov_dict, order)
    quote = ' '.join(sentence_array)
    return render_template('index.html',
                           quote = quote)

def generate_markov_dict():
    global markov_dict

    word_file = codecs.open(source, encoding='utf-8')
    word_string = word_file.read()
    #Convert the string from unicode to ascii
    word_string = word_string.encode('ascii', 'ignore')

    word_array = word_string.split()
    markov_dict = markov.markov.markov_dict_gen(word_array, order)

if __name__ == '__main__':
    app.run()
    #app.add_url_rule('/favicon.ico',
    #                 redirect_to=url_for('static', filename='favicon.ico'))
