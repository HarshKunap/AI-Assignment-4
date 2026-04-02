"""Universal Cryptarithmetic solver using backtracking."""

def solve_cryptarithmetic(word1, word2, result_word):
    # Automatically grab all unique letters
    letters = list(set(word1 + word2 + result_word))

    if len(letters) > 10:
        print("Too many unique letters! We only have 10 digits.")
        return None

    def to_number(word, assignment):
        value = 0
        for char in word:
            value = value * 10 + assignment.get(char, 0)
        return value

    def is_valid_final(assignment):
        # Words can't start with zero
        if assignment.get(word1[0]) == 0 or assignment.get(word2[0]) == 0 or assignment.get(result_word[0]) == 0:
            return False

        num1 = to_number(word1, assignment)
        num2 = to_number(word2, assignment)
        num_result = to_number(result_word, assignment)

        return num1 + num2 == num_result

    def backtrack(index, assignment, used_digits):
        if index == len(letters):
            if is_valid_final(assignment):
                return dict(assignment)
            return None

        letter = letters[index]

        for digit in range(10):
            if digit in used_digits:
                continue

            assignment[letter] = digit
            result = backtrack(index + 1, assignment, used_digits | {digit})
            
            if result:
                return result
                
            del assignment[letter]

        return None

    return backtrack(0, {}, set())


def main():
    # You can change these to test any puzzle!
    word1 = "CROSS"
    word2 = "ROADS"
    result_word = "DANGER"

    print(f"Solving: {word1} + {word2} = {result_word}\n")
    result = solve_cryptarithmetic(word1, word2, result_word)

    if result:
        print("Solution found!\n")
        
        # Helper to print the math nicely
        def format_num(w): return sum(result[c] * (10**i) for i, c in enumerate(reversed(w)))
        
        print(f"{word1.rjust(10)} = {format_num(word1)}")
        print(f"{word2.rjust(10)} = {format_num(word2)}")
        print(f"{result_word.rjust(10)} = {format_num(result_word)}")

        print("\nLetter Mapping:")
        for letter in sorted(result):
            print(f"{letter} = {result[letter]}")
    else:
        print("No solution exists for this setup.")


if __name__ == "__main__":
    main()