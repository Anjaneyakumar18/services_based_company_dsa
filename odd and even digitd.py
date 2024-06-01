number=12345
evens=0
odds=0
while number>0:
    temp=number%10
    if temp%2==0:
        evens+=1
    else:
        odds+=1
    number//=10
print(f'even digits {evens} and odd digits {odds}')
