phone=input("phone: ")
greeting={
  "one":"1",
  "two":"2",
  "three": "3"
}
output=" "
for ch in phone:
  print(greeting.get(ch, "!"))
    


