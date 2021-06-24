from itertools import combinations

def minion_game(string):
    vowels = ['A','E','I','O','U']
    k = 0
    s = 0
    for i in range(len(string)):
        if string[i] in vowels:
            k += len(string) - i
        else:
            s += len(string) - i
    if s > k:
        print("Stuart"+" "+ "%d" % s)
    elif k > s:
        print("Kevin"+" "+'%d' % k)
    else:
        print("Draw")
    
    



if __name__ == '__main__':
    s = input()
    minion_game(s)
