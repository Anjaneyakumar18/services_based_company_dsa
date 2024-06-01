#method1 Using Skip Indexing
string="ABCDEF"
print(f"String Reverse {string[::-1]}")
#using BackIndexing
final=''
for i in range(len(string)-1,-1,-1):
    final+=string[i]
print(f'String Reverse  {final}')