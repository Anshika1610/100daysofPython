from art import logo
print(logo)
def operations(first,operation,second):
  if operation=='*':
    return first*second
  elif operation=='-':
    return first-second
  elif operation=='+':
    return first+second
  elif operation=='/':
    return first/second
  else:
    return "Please choose only from the given operations."
  
continuing=True
while continuing:
  first=int(input("What is the first number? : "))
  first=first/1
  operation=input("What is the operation you want to perform from the following :\n+\n-\n*\n/\nEnter your operation : ")
  second=int(input("What is the second number? : "))
  second=second/1
  print(f"{first} {operation} {second} = {operations(first,operation,second)}")
  cont=input("Type 'Yes' to continue and 'No' to stop. ")
  if cont=='No':
    continuing=False

