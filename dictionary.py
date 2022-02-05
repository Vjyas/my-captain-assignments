
import operator
print('please enter a string')
test_str=input()
all_freq={}
for i in test_str:
    if i in all_freq:
        all_freq[i]+=1
    else:
        all_freq[i]=1
so_d=dict(sorted(all_freq.items(),key=operator.itemgetter(1),reverse=True))
print('count of all chars in geeksforgeeks is:\n',str(so_d))
