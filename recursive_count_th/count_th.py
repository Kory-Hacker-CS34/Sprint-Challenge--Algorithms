'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count=0):

    word = list(word)
    start = 0
    end = 2
    # print("word length")
    # print(len(word))
    # print(f"blahblah: {word[0] + word[1]}")
    # print(word)
    if len(word) < 2:
        # print(f"count: {count}")
        # tester = 4
        return count
    else:
        if word[0] + word[1] == 'th':
            count += 1
            # del word[0:1]
            return count_th(word[2:], count)
            # count_th(word, num)
        else:
            # del word[0:1]
            return count_th(word[1:], count)
            # count_th(word, num)
    # count_th(word, count)
    
    

arr = count_th("abcthefthghith")

# print(f"The resulting of count_th is: {count_th(arr)}")
print(arr)
