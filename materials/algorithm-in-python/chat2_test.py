import copy
class vector:
    def __init__(self,b):
        self._cor=[4]*b
    def __len__(self ):
        return len(self._cor)
    def __getitem__(self, item):
        return self._cor[item]
    def __setitem__(self, key, value):
        self._cor[key]=value
    def __sub__(self, other):
        result=vector(len(self))
        for i in range(len(self)):
            result[i]=self[i]-other[i]
        return result
    def __rsub__(self, other):
        result=vector(len(self))
        for i in range(len(self)):
            result[i]=-self[i]+other[i]
        return result
    def  __mul__(self, other):
        result=vector(len(self))
        for i in range(len(self)):
            result[i]=self._cor[i]*other[i]
        return result
    def  __neg__(self):
        result = vector(len(self))
        for i in range(len(self)):
            result[i]=-self[i]
        return result
    def __str__(self):
        return '<'+str(self._cor)[1:-1]+'>'
class matrix(vector):
      def __init__(self,b,c):
          self._cor=[[1]*c]*b
      def col(self):
          return len(self._cor[0])
      def row(self):
          return len(self._cor)
      def setValue(self,b,c,value):
          self._cor[b][c]=value
          return self
      def getValue(self,b,c):
          return self._cor[b][c]
      def __mul__(self, other):#not right in math, but just practice overloading
          result=matrix(self.row(),other.col())
          print(result)
          for i in range(self.row()):
              for j in range(other.col()):
                  for m in range(self.row()):
                      for n in range(self.col()):
                        result.setValue(i,j,self.getValue(i,n)*other.getValue(m,j)+result.getValue(i,j))
          return result
      def __str__(self):
          output=''
          for i in range(self.row()):
              output+=str(self._cor[i])
              output+='\n'
          return output


if __name__=='__main__':
    a=matrix(2,3)
    b = matrix(3, 2)
    # print(a)
    # print(b)
    print(a*b)
    # # b[-1].append(6)
    # for i in range(4):
    #     print(id(a))
    #     print(id(b))
    #     print((a[i]))
    #     print((b[i]))