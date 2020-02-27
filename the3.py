def place_words(Corpus):
    mylist=[]
    k=0
    if len(place(Corpus,mylist,k))==len(Corpus[0]):
        return place(Corpus,mylist,k)
    else:
        return False        


def place(Corpus,mylist,k):
    N=len(Corpus)
    i=0                     
    
    stack=[]
    n=len(Corpus[0])
          
    while i < N:
        mylist.append(Corpus[i])
        if answer_test(mylist,Corpus)==True and place(Corpus,mylist,k): 
            return mylist
                  
        else:
            mylist.pop()
            i= i + 1
               
    
    while k < N:
        k=k+1
        if len(mylist)<len(Corpus[0]):
            a=mylist.pop()
            find=Corpus.index(a) 
            Corpus=Corpus[:find]+Corpus[find+1:]+[a]
            return place(Corpus,mylist,k) 
                      
        else:       
            return mylist
    return mylist


def answer_test(lstans,lstlist):
    if len(lstans)==0: 
        return True
    if len(lstlist)==0:
        return False
    if horizantal_test(lstans,lstlist)==True and search(lstans,lstlist)==True:
        return True
    else:
        return False     
      

def test(lst,N): 
    if len(lst)==0:   
        return ('')       
    else:
        return lst[0][N] + test(lst[1:],N)

def search(word,lstlist):
        i=0
        while i<len(lstlist):
            if lstlist[i] in word:
                lstlist=lstlist[:i]+lstlist[i+1:]
                i=i+1
            i=i+1    

        if len(word)==0:
            return True
        if len(lstlist)==0:
            return True
        mylist=[]
        i=0
        j=0
        while i<len(lstlist) and j<len(word[0]):
            if test(word,j).upper()==lstlist[i][:len(word)].upper() and test(word,j) not in word:
                    mylist=mylist+[1]
                    j=j+1
                    i=0
            else:
                        i=i+1
        
        if len(mylist)==len(word[0]):
                return True    
        else:
                return False     

def horizantal_test(lstans,lstlist):      
        lst=[]
        i=0
        if len(lstans)==0: 
                return True
        if len(lstlist)==0:
            return False
        while i<len(lstans): 
                    if lstans[i] in lstlist:
                        lst = lst + [1] 
                        i=i+1                  
        if len(lst)==len(lstans):
                return True    
        else:
                return False
    