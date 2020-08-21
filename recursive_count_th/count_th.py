'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, num=0):

    # count = word.count("th")
    # print(count)
    # return count
    word = list(word)
    # count = 0
    start = 0
    end = 2
    print(word)
    print(num)
    # print(word[start:end])
    if len(word) <= 1:
        return num
    else:
        if word[start:end] == ['t', 'h']:
            num += 1
            del word[0]
        else:
            del word[0]
    count_th(word, num)
    # print(count)

    

count_th("abcthefthghith")
