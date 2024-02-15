# PART 1

# Code to make alternate lettes uppercase.

sentence = "Welome to the world of code."
final_sentence_1 = "" #Empty string to input the final characters.

for i in range(len(sentence)): # Loop for the ength of the sentence.

    if i % 2 == 1: 
        final_sentence_1 += sentence[i].upper()   # Means the index is odd and therefore changes every other character.

    else: 
        final_sentence_1 += sentence[i].lower()   # index that is not odd must be even.

print(final_sentence_1)




#PART 2


# Code to make every alternate wrd upper case.
sentence_2 = "Welome to the world of code."

sentence_2_split = sentence_2.split()   # separates each word.

separate_words = "" # Empty list to input the separated words.

for x in range(0, len(sentence_2_split)): #loop to make every second word uppercase.

    if x % 2 == 0: #Means that the index is even and therefore wiill be every other word.
        separate_words = separate_words + " "+ sentence_2_split[x].lower() # Spaces required to make sure the words are separated and readable.

    else: #Means that the index is odd.
        separate_words = separate_words +" " + sentence_2_split[x].upper() 

final_sentence_2 = "".join(separate_words)
final_sentence_2 = final_sentence_2.strip(' ')  # Remove the aditional space at the beginning of the sentece.

print(final_sentence_2)