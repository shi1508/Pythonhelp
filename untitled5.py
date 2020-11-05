import os
h = open("noogloogi101","w")
h.write("onethang")
h.close()
filename = input("Please enter file name:\n")
if os.path.exists(filename):
   while(True):
        input1 = input("File name exists. What would you like to do? Type 'A' to read the file, 'B' to delete and start over or 'C' to append the file:\n")
        if input1 == "A" or input1 == "B" or input1 == "C":
            if input1 == "A":
                bunner = open(filename, "r")
                fish = bunner.read()
                print(fish)
                bunner.close()
                break
            elif input1 == "B":
                babi = open(filename, "w")
                smt = babi
                babi.close()
                bunner = open(filename, "r")
                fish = bunner.read()
                print(fish)
                bunner.close()                
                break
            elif input1 == "C":
                yomama = open(filename, "a")
                Appendtext = input("Please enter the text you want to add:\n")
                yomama.write(Appendtext)
                yomama.close()
                break
            else:
                continue
else:
    text = input("File doesn't exist. Please enter the text you want to add to the file:\n")
    jagoogi = open(filename, "w")
    jagoogi.write(text)
    jagoogi.close()