import os
def disk_usage(path):
    total=os.path.getsize(path)
    if os.path.isdir(path):
        for sub in os.listdir(path):
            total+=disk_usage(os.path.join(path,sub))
    print('{0:<7}'.format(total),path)
    return total
def quick_sort(A):
    flag=A[0]
    for i in range(1,len(A)):
        if A[i]>flag:

if __name__=='__main__':
    print(disk_usage('C:\\Users\\lx2n14\\Desktop\\Program'))