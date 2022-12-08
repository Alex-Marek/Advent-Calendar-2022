SIZE_AMOUNT = 100000

def main():
    with open("Day 7/input.txt") as input:
        for line in input:
            line = line.strip("\n")
            if line.find("$ cd ") != -1:
                if line.find("$ cd ..") != -1:
                    print(f'{line} goes back a directory')
                else:                                                           #Moves in a specific directory
                    print(f'{line} goes forward to {line.split(" ")[2]}')
            elif line.find("$ ls") != -1: pass
            elif line.find("dir ") != -1: pass                                  #This will probably also do nothing
            else:                                                               #Should take the file size if less than SIZE_AMOUNT add it to the dictionaries current directory size
                print(f'{line} = size:{line.split(" ")[0]} name:{line.split(" ")[1]}')



if __name__ == "__main__":
    main()