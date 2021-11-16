#Page replacment algorithm: Least Recently Used
def pageFaults(pages,capacity):
    s = []
    pageFaults = 0
    
    for i in pages:
        if i not in s:
            if(len(s) == capacity):
                s.remove(s[0])
                s.append(i)
            else:
                s.append(i)
            pageFaults +=1
        else:
            s.remove(i)
            s.append(i)
    return pageFaults

if __name__ == '__main__':
    pages=[7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    n=len(pages)
    capacity=4
    print(pageFaults(pages,capacity))


