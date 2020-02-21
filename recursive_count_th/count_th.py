'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, occurences=None):
    # Base Case
    if len(word) <= 1:
        return 0

    # Initialize data structure to keep count of "th" occurences
    if occurences is None:
        occurences = []

    # Logic to move towards base case
    if word[0] == 't' and word[1] == 'h':
        occurences.append(1)
        count_th(word[2:], occurences)

    # If first char isn't a 't' then remove from word 
    else:
        count_th(word[1:], occurences)
   
    return len(occurences)

if __name__ == "__main__":
    print(count_th('abcthxththtyz'))
