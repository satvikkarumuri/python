import random
WordList = ["cat", "dog", "fish", "parrot", "hamster", "frog"]

random.shuffle(WordList)

Word = WordList[0]
Answer = list(Word)

LetterCount = len(Answer)
display = []
