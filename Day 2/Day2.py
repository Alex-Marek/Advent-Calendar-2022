WIN = 6
LOSE = 0
DRAW = 3

ROCK = 1
PAPER = 2
SCISSORS = 3

with open('Day 2/input.txt') as input:
    P1total = 0
    P2total = 0
    for line in input:
        nLine = line.split(' ')
        oppMove = nLine[0]
        pMove = nLine[1][:1]
        if oppMove == "A": #Rock
            if pMove == "X":#Rock
                P1total += DRAW + ROCK
                P2total += LOSE + SCISSORS
            elif pMove == "Y":#Paper
                P1total += WIN + PAPER
                P2total += DRAW + ROCK
            elif pMove == "Z":#Scissors
                P1total += LOSE + SCISSORS
                P2total += WIN + PAPER

        elif oppMove == 'B': #Paper
            if pMove == 'X':#Rock
                P1total += LOSE + ROCK
                P2total += LOSE + ROCK
            elif pMove == 'Y':#Paper
                P1total += DRAW + PAPER
                P2total += DRAW + PAPER
            elif pMove == 'Z':#Scissors
                P1total += WIN + SCISSORS
                P2total += WIN + SCISSORS

        elif oppMove == 'C': #Scissors
            if pMove == 'X':#Rock
                P1total += WIN + ROCK
                P2total += LOSE + PAPER
            elif pMove == 'Y':#Paper
                P1total += LOSE + PAPER
                P2total += DRAW + SCISSORS
            elif pMove == 'Z':#Scissors
                P1total += DRAW + SCISSORS
                P2total += WIN + ROCK

print(f'P1 Answer Total Score: {P1total}')
print(f'P2 Answer Total Score: {P2total}')
