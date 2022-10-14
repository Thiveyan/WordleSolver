
#constants to hold strings and lists
guess = "" 
feedback = ""
guess_list = []
score_list = []
yes_list = []

#transcribing the words from the wordlist text file into a list
try:
    with open('wordlist.txt') as f:
        for line in f:
            guess_list.append(line.strip())
except FileNotFoundError:
    print("file not found")

print("Best openers: SALET, CRANE, CRATE, SLANT, TRACE")
#prompting inputs from the user
for guesses in range(6):
    guess = input("\nword: ").lower()
    print("g - green, y - yellow, b - black")
    result = input("result: ").lower()
    if result == "ggggg":
        print("\nWell Done! Guess",guesses+1)
        break
    #creating a yes_list to compare duplicates later    
    for j in range(5):
      if result[j] == 'g':
        yes_list.append(guess[j])
      elif result[j] == 'y':
        yes_list.append(guess[j])
          
    # Creating a tuple, so that the program is not iterating through a changing list.
    temp_tuple = tuple(guess_list)
    for word in temp_tuple: 
        for i in range(5):
            #remove the words that doesn't have the green letter at the specific index and add the green letter to yes_list to check duplication later  
            if result[i] == "g" and guess[i] != word[i]:
                guess_list.remove(word)
                break
            #remove the words that doesn't have the yellow letter or has the yellow letter in the same positionand add the yellow letter to the yes_list to check duplication later
            elif result[i] == "y" and (guess[i] not in word or guess[i]  == word[i]):
                guess_list.remove(word)
                break
              
              #remove the words if it has the black letter and that letter is not present in the yes_list                       
            elif result[i] == "b":
              if (yes_list.count(guess[i]) == 0) and guess[i] in word:
                #print("b1: " + guess[i] + word, i)
                guess_list.remove(word)
                break
              #remove the word if it has the black letter in the same spot as the guess word and the black letter is present in the yes_list
              elif result[i] == "b" and (yes_list.count(guess[i]) > 0) and guess[i] == word[i]:
                guess_list.remove(word)
                break

    new_guess_list = guess_list.copy()

    #check how many common letters the word has compared to the other words in the list and assign a score for the word in the same index
    for word1 in guess_list:
      score = 0
      for word2 in new_guess_list:
        for i in range(5):
          if word1[i] == word2[i]:
            score +=1;
      score_list.append(score)

    #find the biggest score and print the word associated with it   
    max_num = max(score_list)
    suggestion_word = guess_list[score_list.index(max_num)]
    print("\nSuggested word: " + suggestion_word)
  
    score_list.clear()
    new_guess_list.clear()




