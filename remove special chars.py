import string 
alpha_nums=string.ascii_letters+string.digits #lowe case + upper case + 0-9 digits
word="1rde5zhbbfjgugwdu763479#%*9927"
ans=''
for ch in word:
    if ch in alpha_nums:
        ans+=ch
print(ans)