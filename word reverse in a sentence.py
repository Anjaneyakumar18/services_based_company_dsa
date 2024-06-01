sentence="python progaming language"
reversed_words=''
word=''
for ch in sentence:
    if ch == " ":
        reversed_words+=word+" "
        word=''
    word=ch+word
reversed_words+=word #final word
print(reversed_words)