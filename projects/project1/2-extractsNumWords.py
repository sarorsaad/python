# A program that takes a sentence from the user and extracts the number of words in the sentence without Repetition
your_sentence =input(' Enter your sentence ')
wordlist = your_sentence.split()

wordfreq = []
for i in wordlist:
    wordfreq.append(wordlist.count(i))
    
print(your_sentence )
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(list(zip(wordlist, wordfreq))))