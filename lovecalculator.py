print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1l=name1.lower()
name2l=name2.lower()
counttrue=name1l.count("t")+name1l.count("r")+name1l.count("u")+name1l.count("e")+name2l.count("t")+name2l.count("r")+name2l.count("u")+name2l.count("e")
countlove=name1l.count("l")+name1l.count("o")+name1l.count("v")+name1l.count("e")+name2l.count("l")+name2l.count("o")+name2l.count("v")+name2l.count("e")
c=counttrue*10+countlove
if c<10 or c>90:
  print(f"Your score is {c}, you go together like coke and mentos.")
elif c>40 and c<50:
  print(f"Your score is {c}, you are alright together.")
else:
  print(f"Your score is {c}.")
