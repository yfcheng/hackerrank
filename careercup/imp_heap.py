heap_imp = [4,4,8,9,4,12,9,11,13]

class MyHeap:
    heap = []
    def __init__(self,values):
        self.heap = values

    def showItems(self):
        print self.heap

    def __siftup(self):
        pos = len(self.heap) - 1
        newItem = self.heap[pos]
        while pos > 0:
            parentpos = (pos - 1) >> 1
            parentItem = self.heap[parentpos]
            if parentItem > newItem:
                self.heap[parentpos] = newItem
                self.heap[pos] = parentItem
                pos = parentpos
                continue
            break

    def insert(self,input):
        self.heap.append(input)
        self.__siftup()


test = MyHeap(heap_imp)
test.showItems()
test.insert(2)
test.showItems()
test.insert(9)
test.showItems()
test.insert(5)
test.showItems()
