from histogram import Histogram
from queue import Queue
from timer import Timer

class MarkovModel:

    def __init__(self, word_array, order):
        self.order = order
        """ Generates a markov dictionary
        Keyword arguments:
        word_array -- an array of words of tokens that make up the corpus
        order -- the order of markov model that you want to create (more info: https://goo.gl/BTsSLx)

        """
        markov_dict = {}
        queue = Queue()

        word_array.insert(0, '*end*')
        queue.extend(word_array[0:order])

        for i in range(1, len(word_array) - order + 1):
            #Shift the queue to the next word
            queue.dequeue()
            queue.enqueue(word_array[i + order - 1])

            history_tuple = tuple(queue[0: len(queue) - 1])

            try:
                end_index = queue.index('*end*')
            except ValueError:
                end_index = -1

            #if the queue has end in it, replace the other words with None because
            #it has moved on to the next sentence
            if end_index > 0 and end_index != order - 1:
                history_array = []
                for i in range(0, end_index):
                    history_array.append(None);
                history_array.append('*end*')
                history_tuple = tuple(history_array)

            #if end is in the beginning it is a new sentence, so ignore the order
            #and just record the first word in the sentence
            if end_index is 0:
                followed_by = queue[1:-1]

                #Don't start sentences that are shorter than the order
                if '*end*' in followed_by:
                    continue

                if '*end*' in markov_dict:
                    #Add increment histogram
                    markov_dict['*end*'].update([tuple(followed_by)])
                else:
                    #Create histogram
                    markov_dict['*end*'] = Histogram('')
                    markov_dict['*end*'].append(tuple(followed_by))

            #Add the tuple into the dict followed by the next word
            if history_tuple in markov_dict:
                #Add increment histogram
                markov_dict[history_tuple].update([queue[-1]])
            else:
                #Create histogram
                markov_dict[history_tuple] = Histogram('')
                markov_dict[history_tuple].append(queue[-1])

            self.dict = markov_dict

    def generate_sentence_array(self):
        """ Generates a sentence using the markov model

        Returns
        sentence: [str]
        """

        word_array = ['*end*']
        start_tuple = '*end*'

        word_array.extend(self.dict[start_tuple].random())

        while word_array[-1] != '*end*':
            previous_array = []
            for i in reversed(range(1, self.order)):
                previous_array.append(word_array[len(word_array) - i])
            word_array.append(self.dict[tuple(previous_array)].random())

        del word_array[-1]

        del word_array[0]
        return word_array

if __name__ == '__main__':
    markov = MarkovModel(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'], 3)
    word_list = markov.generate_sentence()
    print(' '.join(word_list))
