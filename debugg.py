msg = "Hello Worldf"

# practice writing if else
if msg == "Hello World":
  print(msg)
else:
  print("I don't know the message")

# I made a function
def friendlyMsg(name):
  return f'Hello, {name}! Have a great day!'

print(friendlyMsg("james").upper())
print(friendlyMsg("clayton"))
