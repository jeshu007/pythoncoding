def words(sentence):
    words=0
    for i in sentence:
        a=i.split()
        b=len(a)
        if b>words:
            words=b
    return words
sentence=["python is a high level language"]
print("the maximum number of words in the given string",words(sentence))
