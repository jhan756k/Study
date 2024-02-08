word = "strike"
word = list(word)
print("length of word is", len(word))
print()
while True:
  inp = input("Enter a word: ")
  charlist = list(inp)
  ball, strike = 0, 0
  strikeind = []
  if len(charlist) != len(word):
    print("Length of word is not equal to the length of the word")
    print()
  elif charlist == word:
    print("Homerun")
    exit()
  else:
    for x in range(len(word)):
      if word[x] == charlist[x]:
        strike += 1
        strikeind.append(x)
    for x in range(len(word)):
      if x not in strikeind:
        for y in range(len(word)):
          if x != y and word[x] == charlist[y] and y not in strikeind:
            ball += 1
    if strike == 0 and ball == 0:
      print("Out")
      print()
    else:
      print(strike, "strike", ball, "ball")
      print()