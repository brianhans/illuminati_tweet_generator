from histogram import Histogram
from queue import Queue

# def markov_dict_gen(word_array):
#     markov_dict = {}
#     word_array.append(None)
#     word_array.insert(0, '*start*')
#     for i in range(0, len(word_array) - 1):
#         if word_array[i] in markov_dict:
#             #Add increment histogram
#             markov_dict[word_array[i]].update([word_array[i + 1]])
#         else:
#             #Create histogram
#             markov_dict[word_array[i]] = Histogram(word_array[i + 1])
#
#     return markov_dict


def markov_dict_gen(word_array, order):
    markov_dict = {}
    queue = Queue()

    queue.extend(word_array[0:order])

    for i in range(1, len(word_array) - order + 1):
        #Shift the queue to the next word
        queue.dequeue()
        queue.enqueue(word_array[i + order - 1])

        try:
            end_index = queue.index('*end*')
        except ValueError:
            end_index = -1

        if end_index > 0 and end_index != order - 1:
            continue

        if end_index is 0:
            history_tuple = '*end*'
        else:
            history_tuple = tuple(queue[0: len(queue) - 1])

        if history_tuple in markov_dict:
            #Add increment histogram
            markov_dict[history_tuple].update([queue[-1]])
        else:
            #Create histogram
            markov_dict[history_tuple] = Histogram('')
            markov_dict[history_tuple].append(queue[-1])

    return markov_dict

def gen_words(markov_dict, order):
    word_array = []
    # word_array.insert(0, '*start*')
    # for _ in range(2, order):
    #     word_array.insert(0, None)
    start_tuple = '*end*'#tuple(word_array)

    word_array.append(markov_dict[start_tuple].random())

    while word_array[-1] != 'None':
        print(word_array)
        previous_array = []
        for i in reversed(range(1, order)):
            previous_array.append(word_array[len(word_array) - i])
        word_array.append(markov_dict[tuple(previous_array)].random())

    del word_array[-1]

    for _ in range(1, order):
        del word_array[0]
    return word_array


if __name__ == '__main__':
    markov_dict = markov_dict_gen(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'], 3)
    word_list = gen_words(markov_dict, 3)
    print(' '.join(word_list))
