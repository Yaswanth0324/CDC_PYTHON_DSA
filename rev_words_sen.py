def rev_sen(sentence):
    words=sentence.split(" ")
    rev_words=words[::-1]
    return " ".join(rev_words)
    
sentence=input("enter a sentence: ")
print(rev_sen(sentence))
