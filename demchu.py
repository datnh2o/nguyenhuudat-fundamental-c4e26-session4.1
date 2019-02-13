word = input ("Enter a word: ")
a = word.lower()
dictionary = {

}
for i in range(len(word)):
    if word[i]==" ":
        print("")
    else:
        dictionary[a[i]] = a.count(a[i]) 
for i, w in sorted(dictionary.items()):
    print(i, w, sep=" - ")
#bài làm có tham khảo =)    