n=int(input("Enter the number of rounds you want to play "))
for i in range(1,n+1):
  if i%3!=0 and i%5!=0:
    print(i)
  elif i%3==0 and i%5==0:
    print("Fizzbuzz")
  elif i%3==0 and i%5!=0:
    print("Fizz")
  elif i%3!=0 and i%5==0:
    print("Buzz")

