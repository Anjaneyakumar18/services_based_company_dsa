#Indexing step
String="DAD"
print(f"String Palindrome  {String==String[::-1]}")
#back Indexing
St="MOM"
final=''
for i in range(len(St)-1,-1,-1):
    final=St[i]+final
print("string Palindrome",St==final)