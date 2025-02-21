phone=input("Phone:" )
dict={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}
output=""
for ch in phone:
    output += dict.get(ch , "!") + " "
print(output)
