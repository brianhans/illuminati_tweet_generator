class Queue(list):

    def enqueue(self, item):
        self.append(item)

    def dequeue(self):
        return self.pop(0)
