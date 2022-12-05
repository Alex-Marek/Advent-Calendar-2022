#ASCII values - 96 for lower case
ASCII_LOWER = 96
#ASCII values - 38 for upper case
ASCII_UPPER = 38

def problem_One():
    with open("Day 3/input.txt") as input:
        p1_Total = 0
        for line in input:
            line = line.strip("\n")
            half_Point = int(len(line) / 2)
            first_Half = line[0:half_Point]
            second_Half = line[half_Point::]
            p1Strings = [first_Half, second_Half]
            dupe_Char = find_Duplicate(p1Strings)
            ascii_Num = ord(dupe_Char)
            if dupe_Char.isupper():
                ascii_Num -= ASCII_UPPER
            elif dupe_Char.islower():
                ascii_Num -= ASCII_LOWER
            p1_Total += ascii_Num
        print("The total for P1 is: ", p1_Total)

def problem_Two():
    with open("Day 3/input.txt") as input:
        p2_Total = 0
        p2List = []
        for line in input:
            line = line.strip("\n")
            p2List.append(line)
            if len(p2List) % 3 == 0:
                dupe_Char = find_Duplicate(p2List)
                ascii_Num = ord(dupe_Char)
                if dupe_Char.isupper():
                    ascii_Num -= ASCII_UPPER
                elif dupe_Char.islower():
                    ascii_Num -= ASCII_LOWER
                p2_Total += ascii_Num
                p2List.clear()
        print("The total for P2 is: ", p2_Total)

#Find duplicate letters given strings should return a single character if only one found or a list of characters if multiple
def find_Duplicate(str_List):
    found = len(str_List)-1
    dupe_List = []
    characters = {}
    if len(str_List) < 2:                                           #Function shouldn't run if there are under 2 strings
        return "List of strings must have at least two values"

    for j in range(0,len(str_List)):                                #Removes duplicate letters from strings
        str_List[j] = "".join(set(str_List[j]))

    for letter in str_List[0]:                                      #Initialize the dict
        characters[letter] = 0

    for i in range(1,len(str_List)):                                #Loops through all the strings (except the first)
        for letter in str_List[i]:                                  
            if letter in characters:
                characters[letter] += 1
            else:                                                   #if a letter is not found in the character dictionary then add it with a value of 0
                characters[letter] = 0
    
    for values in characters.keys():
        if characters[values] >= found:
            dupe_List.append(values)
    if len(dupe_List) == 1:
        return dupe_List[0]
    else:
        return dupe_List
    

                

if __name__ == "__main__":
    problem_One()
    problem_Two()