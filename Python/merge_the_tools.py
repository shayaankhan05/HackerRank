def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        s = ""
        for j in string[i : i + k]:
            if j not in s:
                s += j          
        print(s)
        


        
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    
    
# Solution Using pandas


import pandas as pd
string = "AABCAAADA"
k = 3
t = []
t = [string[i:i+k] for i in range(0, len(string), k)]
print(t)
distinct = []
for i in range(len(t)):
    distinct.append((list(pd.unique(list(t[i])))))
    print("".join(distinct[i]))


