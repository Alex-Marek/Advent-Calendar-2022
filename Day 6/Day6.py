def Day6(unique_Chars):
    with open("Day 6/input.txt") as input:
        count = unique_Chars
        cur_String = input.readline(unique_Chars)
        while True:
            next_Char = input.readline(1)
            remove_Dupes = "".join(set(cur_String))
            if len(remove_Dupes) < unique_Chars:
                cur_String = cur_String[1:unique_Chars]
                cur_String = cur_String + next_Char                         #Add another character onto it
            elif len(remove_Dupes) == unique_Chars:
                print(f"{unique_Chars} unique character found at {count} Characters are: {cur_String}")
                break
            if cur_String == "":
                break
            count += 1

if __name__ == "__main__":
    Day6(4)
    Day6(14)