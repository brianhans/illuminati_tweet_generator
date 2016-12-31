from flask import Flask
import Markov.markov
import codecs
from Markov.timer import Timer

app = Flask(__name__)
source = 'corpus.txt'
order = 3
markov_dict = {}

@app.route('/')
def generate():
    global markov_dict

    sentence_array = Markov.markov.gen_words(markov_dict, order)
    if len(sentence_array) > 1:
        return ' '.join(sentence_array)
    else:
        return 'Please wait'

def generate_markov_dict(completion):
    global markov_dict
    timer = Timer()

    word_file = codecs.open(source, encoding='utf-8')
    word_string = word_file.read()
    #Convert the string from unicode to ascii
    word_string = word_string.encode('ascii', 'ignore')

    word_array = word_string.split()
    markov_dict = Markov.markov.markov_dict_gen(word_array, order)
    print(timer.stop())
    completion()

if __name__ == '__main__':
    app.run()
    generate_markov_dict()
