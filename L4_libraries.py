i = 3

while i!=0:
    with open("savefile.txt","a") as file:
        file.write(input("say what you wanna say: ")+"\n")
        
    i-=1
with open("savefile.txt", "r") as file:
    lines = file.readlines()

print(lines)