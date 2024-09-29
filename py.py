# importing pandas
import pandas as pd


#! change me
letterClasses = [['A', 'N', 'U'], 
                 ['M', "I", "C"], 
                 ['R', 'L', 'O'],
                 ['D', 'S', 'Z']
                ]


number_of_words_in_solution = 2 #! change me (1, 2, or 3 (slow))

try_hard_words = False #! change me

show_all_solutions = True #! change me

possible_soultions = []


# read text file into pandas DataFrame
if try_hard_words:
    df = pd.read_csv("words_hard.csv")
else:
    df = pd.read_csv("words_easy.csv")

# remove all two letter words
df = df[df[df.columns[0]].apply(lambda x: isinstance(x, str) and len(x) > 2)]

# create a list of all the letters in letterClasses
letters = [letter for letterClass in letterClasses for letter in letterClass]

# remove all words that contain letters not in the list of letters
df = df[df[df.columns[0]].apply(lambda x: all([letter in letters for letter in x]))]

# if the word contains letters from the same class adjacent to each other, remove it
df = df[df[df.columns[0]].apply(lambda x: not any([x[i] in letterClasses[j] and x[i+1] in letterClasses[j] for j in range(len(letterClasses)) for i in range(len(x)-1)]))]

# creata a numpy array of the words
words = df[df.columns[0]].values

def capatalize(word):
    return word[0] + word[1:].lower()

if number_of_words_in_solution == 1:
    oneWordSolution = max(words, key=lambda x: len(set(x)))
    if len(set(oneWordSolution)) == 12:
        possible_soultions.append(capatalize(oneWordSolution))
        # print(capatalize(oneWordSolution))
    # else:
    #     print("not possible, closest is:", capatalize(oneWordSolution))

if number_of_words_in_solution == 2:
    for word1 in words:
        last_letter = word1[-1]

        # a list of all words starting with the last letter of word1
        words2 = [w for w in words if w[0] == last_letter]        

        for word2 in words2:

            if len(set(word1 + word2)) == 12:
                possible_soultions.append([capatalize(word1), capatalize(word2)])
                # print(capatalize(word1), capatalize(word2))

if number_of_words_in_solution == 3:
    for word1 in words:
        last_letter = word1[-1]

        # a list of all words starting with the last letter of word1
        words2 = [w for w in words if w[0] == last_letter]        

        for word2 in words2:
            last_letter = word2[-1]

            # a list of all words starting with the last letter of word2
            words3 = [w for w in words if w[0] == last_letter]        

            for word3 in words3:

                if len(set(word1 + word2 + word3)) == 12:
                    possible_soultions.append([capatalize(word1), capatalize(word2), capatalize(word3)])
                    # print(capatalize(word1), capatalize(word2), capatalize(word3))

def display_solution():
    if len(possible_soultions) == 0:
        print("no solutions found. Closest is:", max(words, key=lambda x: len(set(x))), "with", len(set(max(words, key=lambda x: len(set(x))))), "unique letters (of 12)")
    else:
        
        if number_of_words_in_solution == 3:
            if show_all_solutions:
                for solution in possible_soultions:
                    print(solution[0], solution[1], solution[2])
            else:
                print("A possible solution is:", possible_soultions[0][0], possible_soultions[0][1], possible_soultions[0][2])
        elif number_of_words_in_solution == 2:
            if show_all_solutions:
                for solution in possible_soultions:
                    print(solution[0], solution[1])
            else:
                print("A possible solution is:", possible_soultions[0][0], possible_soultions[0][1])
        elif number_of_words_in_solution == 1:
            if show_all_solutions:
                for solution in possible_soultions:
                    print(solution)
            else:
                print("A possible solution is:", possible_soultions[0])

        print(len(possible_soultions), "solutions found")

display_solution()

