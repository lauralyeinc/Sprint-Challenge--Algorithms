'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #check to see if the word has at least two characters
    if (len(word) < 2):
        # if not return results 
        return 0
    #set up count
    count = 0 
    #check the index of the word to see if 0 is T and 1 is H
    if word[0] == 't' and word[1] =='h':
        count = 1
        #resetting the count to start after the th in the word. like found th so we start at eimer...
    count = count + count_th(word[1:])
    #return results to use!
    return count
    #pass

print(count_th("theimertheimertheimer"))
print(count_th('eithereithereithereither'))
