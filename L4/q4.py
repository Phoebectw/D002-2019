sentence=input("please input a sentence")
letter=input("please input a letter")
def checker(sentence, letter):
    result = []
    for t in range (0, len(sentence)):
        if letter == sentence[t]:
            result.append(t)
    return result
print(checker(sentence, letter))
