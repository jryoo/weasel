import string
import random
import operator

corPhrase = "METHINKS IT IS LIKE A WEASEL"
N = 28

def phrase_generator(size=28, chars = string.ascii_uppercase+' '):
	return ''.join(random.choice(chars) for x in range(size))

def mutate(percent=5):
	return random.randrange(100) <= percent

generated = []
bestPhrase = phrase_generator()
bestPhraseScore = 0
iteration = 0
while(bestPhraseScore != len(corPhrase)):
	iteration += 1
	for i in range(0,100):
		phrase = list(bestPhrase)
		for j in range(0,28):
			if(mutate(5)):
				phrase[j] = phrase_generator(1)
		phrase = ''.join(phrase)
		score = map(operator.eq, phrase, corPhrase).count(True)
		if(score > bestPhraseScore):
			print phrase
			print score
			print iteration
			bestPhrase = phrase
			bestPhraseScore = score
print iteration