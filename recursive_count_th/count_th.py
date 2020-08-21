'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word= None, num=0):

    # count = word.count("th")
    # print(count)
    # return count
    print(num)
    flobort = num
    word = list(word)
    # count = 0
    start = 0
    end = 2
    print(word)
        # print(num)
        # print(word[start:end])
    if len(word) == 0:
        return flobort
    else:
        if word[start:end] == ['t', 'h']:
            num += 1
            del word[0:1]
        else:
            del word[0:1]
        count_th(word, num)


    

arr = count_th("abcthefthghith")

print(f"The resulting of count_th is: {count_th(arr)}")
