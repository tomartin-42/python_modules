import random

def generator(text, sep=" ", option=None):
    """
    Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded.
    """
    if not isinstance(text, str) or not isinstance(sep, str) or len(sep) == 0:
        print("ERROR")
        exit(1)
    lst = text.split(sep)
    if option == None:
        for e in lst:
            yield e 
    if option == 'shuffle':
        while len(lst):
            e = lst[random.randint(0, len(lst) - 1)]
            lst.remove(e)
            yield e
    if option == 'ordered':
        o_l = sorted(lst)
        for e in o_l:
            yield e
    if option == 'unique':
        s_l = set(lst)
        for e in s_l:
            yield e
    



if __name__ == '__main__':
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, sep=" "):
        print(word)
    print("=============================================")
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    print("=============================================")
    for word in generator(text, sep=" ", option="ordered"):
        print(word)
    print("=============================================")
    text = "Lorem Ipsum Lorem Ipsum"
    for word in generator(text, sep=" ", option="unique"):
        print(word)
    text = 10
    for word in generator(text, sep="" , option="unique"):
        print(word)
    
