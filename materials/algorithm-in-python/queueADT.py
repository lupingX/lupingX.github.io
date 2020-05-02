class queue2(object):
    CAPACITY = 4
    def __init__(self):
        self._data=[None]*queue2.CAPACITY
        self._front = 0
        self._size =0
    def __len__(self):
        return self._data
    def is_empty(self):
       return self._size==0
    def dequeue(self):
        if self.is_empty():
            raise Exception('the queue is empty')
        else:
            result=self._data[self._front]
            self._data[self._front]=None
            self._front=(self._front+1)
            self._size -= 1

            return  result
    def enque(self,e):
        if self._size==len(self._data):
            self._resize(2*len(self._data))
        self._data[ (self._front+ self._size)%len(self._data)]=e
        self._size += 1

    def _resize(self,par):
        old=self._data
        self._data=[None]*par
        for k in range(self._size):
            self._data[k]=old[(k+self._front)%len(old)]
        self._front=0
    def __str__(self):
        return ''.join(str([self._data[(self._front+k)%len(self._data)] for k in range(self._size)]))
# if __name__ == '__main__':
#     a=queue2()
#     a.enque(3)
#     print(a)
#     a.enque(2)
#     print(a)
#     a.dequeue()
#     print(a)
#     a.enque(4)
#     a.enque(3)
#     print(a)
#     a.enque(3)
#     print(a)
#     a.dequeue()
#     print(a)
#     a.enque(3)
#     a.enque(3)
#     a.enque(3)
#     a.enque(3)
#     print(a)
#     c=[]*6
#     print(c+[[1,2]])
    # a.dequeue()
    # a.dequeue()
    # a.dequeue()