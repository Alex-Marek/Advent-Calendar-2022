COLUMNS = 9

#1+(n-1)4       #General form of formula for finding the position of each letter

def problemOne():
    q_List = []
    col_List = []
    #Initializaing
    for n in range(1,COLUMNS+1):
        col_List.append(1+(n-1)*4)
        q_List.append([])                           #Create all the Queues
    with open("Day 5/input.txt") as input:
        input_Ended = False
        i_Count = 0
        for line in input:                          #Every time you go down one
            if line == "\n":
                input_Ended = True
            if input_Ended == False:
                j_Count = 0
                for entry in col_List:              #Every time or move to the right one 
                    if line[entry:entry+1] != " ":
                        q_List[j_Count].append(line[entry:entry+1])
                    j_Count += 1
                i_Count += 1
            #Program has now read in the array
            else:
                line = line.strip("\n")
                line_SP = line.split(" ")
                if len(line_SP) > 1:                        
                    move_Amount = int(line_SP[1])
                    move_From = int(line_SP[3])
                    move_To = int(line_SP[5])
                    print(f'moving {move_Amount} from queue:{move_From} to:{move_To}')
                    for i in range(0,move_Amount):
                        q_List[move_To-1].insert(0,q_List[move_From-1].pop(0))
        for crates in q_List:
            print(crates)

def problemTwo():
    q_List = []
    col_List = []
    #Initializaing
    for n in range(1,COLUMNS+1):
        col_List.append(1+(n-1)*4)
        q_List.append([])                           #Create all the Queues
    with open("Day 5/input.txt") as input:
        input_Ended = False
        i_Count = 0
        for line in input:                          #Every time you go down one
            if line == "\n":
                input_Ended = True
            if input_Ended == False:
                j_Count = 0
                for entry in col_List:              #Every time or move to the right one 
                    if line[entry:entry+1] != " ":
                        q_List[j_Count].append(line[entry:entry+1])
                    j_Count += 1
                i_Count += 1
            else:
                line = line.strip("\n")
                line_SP = line.split(" ")
                if len(line_SP) > 1:                        
                    move_Amount = int(line_SP[1])
                    move_From = int(line_SP[3])
                    move_To = int(line_SP[5])
                    for i in range(move_Amount,0, -1):
                        q_List[move_To-1].insert(0,q_List[move_From-1].pop(i))
                    print("\n")
        for crates in q_List:
            print(crates)



if __name__ == "__main__":
    #problemOne()
    problemTwo()
