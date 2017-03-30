from nltk.corpus import wordnet

def get_seeddict(worddict):
	seeddict = dict()

	for o_word in worddict:
		# Finding the synonyms and antonyms
		# for this word
		synonyms = []
		antonyms = []
		score = worddict[o_word]
		for syn in wordnet.synsets(o_word) :
			for l in syn.lemmas():
				synonyms.append(l.name())
				if l.antonyms():
					antonyms.append(l.antonyms()[0].name())
		
		# Appending the words into the dictionary if it does not exist, with its score
		# We assume that positive words get +1 and negative get -1
		synonyms.append(o_word)
		for word in synonyms:
			seeddict[word] = score
		for word in antonyms:
			seeddict[word] = -score
	
	return seeddict

# todo 
# positive_words = ['good', 'well']
# negative_words = ['hate', 'bad']
# worddict = {'good': 1, 'bad':-1,'like': 1, 'hate':-1}
def parse_words(positive_words, negative_words):
	# init positive dictionary
	with open ("data/positive.txt", "r") as f:
	  posText = f.read()
	posTokens = posText.split()

	# score dictionary items (1)
	worddict = {}
	for x in xrange(0,len(posTokens)):
		worddict[posTokens[x]] = 1

	# init negative dictionary
	with open ("data/negative.txt", "r") as f:
	  negText = f.read()
	negTokens = negText.split()

	# score dictionary items (-1)
	for x in xrange(0,len(negTokens)):
		worddict[negTokens[x]] = -1

	return worddict

