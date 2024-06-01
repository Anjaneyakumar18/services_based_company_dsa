senetence="problem solving using python programing"
words=0
current=''
for ch in senetence:
    if ch==" ":
        words+=1
        current=''
    current+=ch
if current is not None:
    print(words+1)
else:
    print(words)