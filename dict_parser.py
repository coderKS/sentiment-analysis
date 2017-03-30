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

