#Page Replacement Algorithm: FIFO
def pageFaults(pages,capacity):
    s=[]
    faults=0
    for i in pages:
        if len(s)<capacity:
            if i not in s:
                s.append(i)
                faults+=1
        else:
            if i not in s:
                s.pop(0)
                s.append(i)
                faults+=1
    return faults

if __name__ == '__main__':
    pages=[7, 0, 1, 2, 0, 3, 0,4, 2, 3, 0, 3, 2]
    n=len(pages)
    capacity=4
    print(pageFaults(pages,capacity))