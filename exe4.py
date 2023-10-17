from itertools import permutations

def solve_cryptarithmetic(puzzle):
    letters = set("".join(puzzle))
    if len(letters) > 10:
        print("Invalid input: Too many unique letters")
        return

    for perm in permutations("0123456789", len(letters)):
        mapping = dict(zip(letters, perm))
        if all(mapping[word[0]] != '0' for word in puzzle):
            num1 = int(''.join(mapping[c] for c in puzzle[0]))
            num2 = int(''.join(mapping[c] for c in puzzle[1]))
            result = int(''.join(mapping[c] for c in puzzle[2]))
            if num1 + num2 == result:
                print("Solution found:")
                for word in puzzle:
                    print(word, '=', ''.join(mapping[c] for c in word))
                return

    print("No solution found")

# Example usage:
puzzle = ["SEND", "MORE", "MONEY"]
solve_cryptarithmetic(puzzle)
