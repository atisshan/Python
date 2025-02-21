feelings=input('How do you feel?:' )
ans=feelings.split()
dict={
    "good":":)",
    "bad":":("
}
output=""
for x in ans:
    output += dict.get(x , x) + " "
print(output)