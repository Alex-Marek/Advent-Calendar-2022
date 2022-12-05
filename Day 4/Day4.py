def main():
    with open('Day 4/input.txt') as input:
        p1_Total = 0
        p2_Total = 0
        for line in input:
            #Input cleanup
            line = line.strip("\n")
            ranges = line.split(",")
            number_List = []
            for entry in ranges:
                number_List.append(int(entry.split("-")[0]))
                number_List.append(int(entry.split("-")[1]))
                if len(number_List) % 4 == 0:
                    x1 = number_List[0]
                    y1 = number_List[1]
                    x2 = number_List[2]
                    y2 = number_List[3]
                    if (is_overlapping(x1,y1,x2,y2)):
                        p2_Total += 1
                    if x1 <= x2 and y1 >= y2:
                        p1_Total += 1
                    elif x1 >= x2 and y1 <= y2:
                        p1_Total += 1
                    else:
                        print(f"0.) ({x1},{y1})?({x2},{y2})")
        print(p1_Total)
        print(p2_Total)

def is_overlapping(x1,x2,y1,y2):
    return max(x1,y1) <= min(x2,y2)

if __name__ == "__main__":
    main()