from flask import Flask
import Markov.markov
import codecs


app = Flask(__name__)
source = 'test.txt'
order = 3
markov_dict = {}

@app.route('/')
def generate():
    global markov_dict

    return Markov.markov.gen_words(markov_dict, order)

def generate_markov_dict(completion):
    global markov_dict

    word_file = codecs.open(source, encoding='utf-8')
    word_string = word_file.read()
    #Convert the string from unicode to ascii
    word_string = word_string.encode('ascii', 'ignore')

    word_array = word_string.split()
    print('spilt')
    markov_dict = Markov.markov.markov_dict_gen(word_array, order)
    print(markov_dict)
    completion()

if __name__ == '__main__':
    generate_markov_dict(app.run)
