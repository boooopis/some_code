score = 20
name = input("input a name. ")
x = name[0:3]
print(x)
file = open('score.txt','a+')
print(x)
f = file.write('\n')
f = file.write(str(score))
f = file.write(' , ')
f = file.write(str(x))
file.close()

