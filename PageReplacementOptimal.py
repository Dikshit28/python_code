#Page Replacement Algorithm: Optimal
def predict(pages,frame,index):
    res=-1
    farthest=index
    for i in range(0,len(frame)):
        for j in range(index,len(pages)):
            if pages[j]==frame[i]:
                if j>farthest:
                    farthest=j
                    res=i
                break
        if j==len(pages)-1:
            return i
    if res==-1:
        return 0
    return res

def pageFaults(pages,capacity):
    page_faults = 0
    s=[]
    
    for i in range(len(pages)):
        print("Frame : ",s,", Incoming Page : ",pages[i])
        if pages[i] in s:
            print("page {} already in memory".format(pages[i]))
            continue
        if len(s) < capacity:
            s.append(pages[i])
            page_faults += 1
        else:
            j=predict(pages,s,i+1)
            print("page {} is replaced by page {}".format(s[j],pages[i]))
            s[j]=pages[i]
            page_faults += 1
    return page_faults


if __name__ == '__main__':
    pages=[7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2,3]
    n=len(pages)
    capacity=4
    print(pageFaults(pages,capacity))