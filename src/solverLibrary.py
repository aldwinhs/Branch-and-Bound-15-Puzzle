class PrioQueue:
    # Constructor
    def __init__(self, priority_function):
        self.queue = []
        self.func = priority_function
    
    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Enqueue item with priority
    def enqueue(self, item):
        i = 0
        found = False

        while(not found and i < len(self.queue)):
            if(self.func(item, self.queue[i])):
                found = True
            else:
                i+=1
        
        self.queue.insert(i, item)

    # Dequeue
    def dequeue(self):
        return self.queue.pop(0)

class StateNode:
    def __init__(self):
        self.matrix = []
        self.parent = None
        self.depth = 0
        self.cost = 0
        self.move = ""