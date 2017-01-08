import sys
import codecs
from hashtable import HashTable
import random

class Histogram(dict):

    def __init__(self, source):
        self.types = 0
        self.tokens = 0

        word_string = source
        if(source.endswith('.txt')):
            word_file = codecs.open(source, encoding='utf-8')
            word_string = word_file.read()
            #Convert the string from unicode to ascii
            word_string = word_string.encode('ascii', 'ignore')

        word_array = word_string.split()

        #super(Histogram, self).__init__(20)
        self.update(word_array)


    def update(self, iterable):
        """Adds a list of items to the histogram

        Keyword arguments:
        iterable -- list of elements to add to the histogram
        """
        for word in iterable:
            self.append(word)

    def append(self, item):
        """Adds an item to the histogram

        Keyword arguments:
        item -- element to add to the histogram
        """

        try:
            self[item] = self[item] + 1
            #self.update_value(item, lambda count: count + 1)
            self.types += 1
        except KeyError:
            self[item] = 1
            #self.set(item, 1)
        self.tokens += 1


    def unique_elements(self):
        """Returns the amount of unique items in the histogram

        Returns:
        unique_elements: int
        """

        return len(self.keys())

    def most_frequent(self):
        """Returns the element that appears most in the histogram

        Returns:
        most_frequent_element: Any
        """
        most_used = ('', 0)
        for word, amount in self.iteritems():
            if(amount > most_used[1]):
                most_used = word, amount

        return most_used

    def count(self, word):
        if word in self:
            return self.get(word)
        else:
            return 0

    def random(self):
        """Returns a random element using a stochastic algorthim

        Returns:
        random_element: Any
        """
        return stochastic_random(self)


def random_element(histogram):
    """Generates a random element from the histogram.

    Keyword arguments:
    histogram -- the histogram to get the random element from

    Returns:
    element: Any
    """
    keys = histogram.keys()
    random_index = random.randint(0, len(keys) - 1)
    return keys[random_index]

def get_element(num, position, tuple_list):
    """Find the word that has a range that num fits into.

    Keyword arguments:
    num -- the number that is the position of element
    position -- the index of the element in tuple_list that you want to check
    tuple_list -- a tuple of (word, starting_index [INCLUSIVE], ending_index [INCLUSIVE]])

    Returns:
    word: str
    """

    #If the number is in the range, return it (Base case)
    if(num <= tuple_list[position][1] and (position - 1 < 0 or num > tuple_list[position - 1][1])):
        return tuple_list[position][0]
    #If the number is less than the beginning of the range
    elif(num < tuple_list[position][1]):
        #Split in array to be just the words that are ranges lower than the current position
        first_half = tuple_list[:len(tuple_list)/2]
        middle_index = len(first_half) / 2
        return get_element(num, middle_index, first_half)
    #If the number is greater than the end of range
    elif(num > tuple_list[position][1]):
        #Split in array to be just the words that are ranges higher than the current position
        second_half = tuple_list[len(tuple_list)/2:]
        middle_index = len(second_half) / 2
        return get_element(num, middle_index, second_half)



def stochastic_random(histogram, tuple_list=None):
    """Generates a random word that has a chance to display the word based on the frequency of the word in the histogram.

    Keyword arguments:
    histogram -- a histogram to generate a random word from (OPTIONAL IF you provide a tuple_list)
    tuple_list -- a tuple of (word, starting_index [INCLUSIVE], ending_index [INCLUSIVE]]) (OPTIONAL IF you provide a histogram) (default: None)

    Returns:
    word: str
    """

    if(not tuple_list):
        tuple_list = generate_tuple(histogram)

    #The maxiumum number to generate which is the ending range of the final word
    maxRange = tuple_list[len(tuple_list) - 1][1]

    random_index = random.randint(0, maxRange)
    middle_index = len(tuple_list) / 2
    return get_element(random_index, middle_index, tuple_list)


def generate_tuple(histogram):
    """Generates a tuple_list from a histogram. The tuple is of (word, starting_index [INCLUSIVE], ending_index [INCLUSIVE]])

    Keyword arguments:
    histogram -- a histogram to generate a tuple_list from

    Return:
    tuple_list: (word, ending_index [INCLUSIVE]])
    """

    index = 0
    tuple_list = []
    for word, amount in histogram.iteritems():
        tuple_list.append((word, index + amount - 1))
        index += amount

    return tuple_list


if __name__ == '__main__':
    file_name = sys.argv[1]
    gram = Histogram(file_name)
    print(real_random.stochastic_random(gram))
