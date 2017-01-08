#!python

from linkedlist import LinkedList

class KeyValuePair:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __eq__(self, other):
            return other == self.key

class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __repr__(self):
        """Return a string representation of this hash table

        Returns:
        hashtable: str
        """
        return 'HashTable({})'.format(self.keys())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def length(self):
        """Return the length of this hash table by traversing its buckets

        Best case running time: Om(n) and
        Worst case running time: O(n) because we have to loop through all
        the elements.

        Returns:
        length: int
        """
        total = 0

        for bucket in self.buckets:
            total += bucket.length()

        return total

    def contains(self, key):
        """Return True if this hash table contains the given key, or False

        Returns:
        isContained: Bool
        """
        try:
            self.get(key)
        except KeyError:
            return False

        return True


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError

        Best case running time: Om(1) if the bucket has only one or less elements
        Worst case running time: O(n) if all the elements are in one bucket.

        Returns:
        value: Any

        Throws:
        KeyError: If key doesn't exist
        """

        index = self._bucket_index(key)
        item = self.buckets[index].find(lambda item: item == key)

        if(item):
            return item.value

        raise KeyError


    def set(self, key, value):
        """Insert or update the given key with its associated value

        Best case running time: Om(1) if the bucket is empty
        Worst case running time: O(n^2) if the bucket has many elements in it.

        """

        index = self._bucket_index(key)

        bucket_item = self.buckets[index].find(lambda item: item == key)

        if(bucket_item):
            bucket_item.value = value
        else:
            self.buckets[index].append(KeyValuePair(key, value))

    def update_value(self, key, function):
        """Update the given key by applying the function

        Best case running time: Om(1) if the bucket is empty
        Worst case running time: O(n^2) if the bucket has many elements in it.

        Keyword arguments:
        key: the key that you want to update the value
        function: lambda function which updates the value (ie x: x + 1)
        """
        index = self._bucket_index(key)

        bucket_item = self.buckets[index].find(lambda item: item == key)

        if(bucket_item):
            bucket_item.value = function(bucket_item.value)
        else:
            raise KeyError


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError

        Best case running time: Om(1) if the bucket is empty
        Worst case running time: O(n) if the bucket has all the elements in it.

        Throws:
        KeyError: If the key doesn't exist
        """

        if not self.get(key):
            raise KeyError

        index = self._bucket_index(key)
        self.buckets[index].delete(key)

    def keys(self):
        """Return a list of all keys in this hash table

        Best case running time: Om(n) and
        Worst case running time: O(b+n) because it has to got through all the elements.

        Returns:
        keys: [Any]
        """
        keys = []

        for bucket in self.buckets:
            bucket_keys = map(lambda x: x.key, bucket.as_list())
            keys.extend(bucket_keys)

        return keys

    def values(self):
        """Return a list of all values in this hash table

        Best case running time: Om(n) and
        Worst case running time: O(b+n) bceause it has to got through all the elements.

        Returns:
        values: [Any]
        """
        values = []

        for bucket in self.buckets:
            bucket_values = map(lambda x: x.value, bucket.as_list())
            values.extend(bucket_values)

        return values

    def clear(self):
        """Remove all items from the dictionary.

        Best case running time: Om(n) and
        Worst case running time: O(n) because it has to got through all the buckets."""
        self.buckets = [LinkedList() for i in range(len(self.buckets))]

    def iteritems(self):
        for bucket in self.buckets:
            for item in bucket:
                yield (item.key, item.value)

    def __iter__(self):
        for bucket in self.buckets:
            for value in bucket.as_list():
                yield value.value

def create_hashtable(amount):
    hash_table = HashTable()

    for i in range(0, amount):
        hash_table.set('test' + str(i), 'none')
    return hash_table

def lengthCheck(amount):
    hash_table = create_hashtable(amount)
    timer = Timer()

    length = hash_table.length()
    return timer.stop()

def setCheck(amount):
    timer = Timer()
    create_hashtable(amount)
    return timer.stop()

def deleteCheck(amount):
    hash_table = create_hashtable(amount)
    keys = hash_table.keys()

    timer = Timer()
    for i in range(0, amount):
        hash_table.delete(keys[i])

    return timer.stop()

def getCheck(amount):
    hash_table = create_hashtable(amount)
    keys = hash_table.keys()

    timer = Timer()
    for i in range(0, amount):
        hash_table.get(keys[i])

    return timer.stop()

def performance_test(function, first_amount, second_amount):
    first_test = function(first_amount)
    second_test = function(second_amount)

    print("Percent difference for " + function.__name__ + " " + str(second_test / first_test))


if __name__ == '__main__':
        performance_test(setCheck, 100, 10000)
        performance_test(deleteCheck, 100, 10000)
        performance_test(lengthCheck, 100, 10000)
        performance_test(getCheck, 100, 10000)
