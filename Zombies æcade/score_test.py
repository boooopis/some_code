score = 10


name = input("input a 3 character name. ")
if name != ' ':
    x = name[0:3]
    print(x ,'x')
    myFile = open("score.csv","a+")
    f = myFile.write("\n")
    f = myFile.write(str(score))
    f = myFile.write(str(x))

    myFile.close()

