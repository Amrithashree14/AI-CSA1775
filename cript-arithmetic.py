from itertools import permutations
def solve_cryptarithm(word1, word2, result_word):
    unique_letters = ''.join(set(word1 + word2 + result_word))
    if len(unique_letters) > 10:
        print("More than 10 unique letters, no solution possible.")
        return
    digits = range(10)
    for perm in permutations(digits, len(unique_letters)):
        mapping = dict(zip(unique_letters, perm))
        if mapping[word1[0]] == 0 or mapping[word2[0]] == 0 or mapping[result_word[0]] == 0:
            continue
        num1 = int(''.join(str(mapping[letter]) for letter in word1))
        num2 = int(''.join(str(mapping[letter]) for letter in word2))
        result = int(''.join(str(mapping[letter]) for letter in result_word))
        if num1 + num2 == result:
            print(f"{word1}: {num1}, {word2}: {num2}, {result_word}: {result}")
            print(f"Mapping: {mapping}")
            return
    print("No solution found.")
word1 = input("Enter the first word: ").strip()
word2 = input("Enter the second word: ").strip()
result_word = input("Enter the result word: ").strip()
solve_cryptarithm(word1, word2, result_word)
