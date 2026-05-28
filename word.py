def matchword(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)
    print("list of words which have the first and last character same",lst)
    return ctr
count=matchword(["abc","cfc","aba"])
print("number of words which have the first and last character same",count)
