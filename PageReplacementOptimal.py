#Page Replacement Algorithm: Optimal
#pages=pg,s=fr, pn =len(pages), capacity=fn,
def predict(pages,frame,index):
    res=-1
    farthest=index
    print("farthest: {}".format(farthest))
    for i in range(len(frame)):
        for j in range(index,len(pages)):
            if pages[j]==frame[i]:
                if j>farthest:
                    farthest=j
                    res=i
                break
        if j==len(pages):
            return i
    print("farthest: {}".format(farthest))
    if res==-1:
        return 0
    return res

def pageFaults(pages,capacity):
    page_faults = 0
    s=[]
    for i in range(len(pages)):
        if pages[i] in s:
            print("page {} already in memory".format(pages[i]))
            page_faults+=1
            continue
        if len(s) < capacity:
            s.append(pages[i])
        else:
            j=predict(pages,s,i)
            s[j]=pages[i]
        print('frame:',s)
    return page_faults


if __name__ == '__main__':
    pages=[7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    n=len(pages)
    capacity=4
    print(pageFaults(pages,capacity))