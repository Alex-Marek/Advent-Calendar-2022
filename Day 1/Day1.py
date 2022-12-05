with open('Day 1/input.txt') as input:
    eTotals = []
    addTop = 3
    total = 0
    for line in input:
        if line != '\n':
            total += int(line)
        else:
            eTotals.append(total)
            total = 0
    
    #Part 2
    topTotals = []
    for i in range(addTop):
        topTotals.append(max(eTotals))
        eTotals.remove(max(eTotals))

print(f"Max Calories is: {max(eTotals)}")
print(f"Total Calories for top {addTop}: {sum(topTotals)}")
