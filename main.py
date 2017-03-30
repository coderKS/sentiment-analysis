from nltk import word_tokenize, sent_tokenize
from dict_parser import get_seeddict, parse_words

def get_score(word, seed_dict):
	if word in seed_dict:
		return seed_dict[word]
	else: 
		return 0

def get_document_score(document_path):
	
	with open (document_path, mode='r') as file_in:
		test_txt = file_in.read()

	sent_tokens = sent_tokenize(test_txt)
	word_tokens = []
	for sent in sent_tokens:
		word_token = word_tokenize(sent)
		word_tokens.append(word_token)

	print ("ready to parse words")
	word_dict = parse_words('data/positive.txt','data/negative.txt')

	print ("ready to get seed dict")
	seed_dict = get_seeddict(word_dict)

	print ("ready to calculate score")
	score = 0.0
	for sent in word_tokens:
		for word in sent:
			# print "words = " + word
			score = score + get_score(word, seed_dict)

	score = score / len(word_tokens)
	return score

documents = ['data/1155049829.txt', 'data/1155047854.txt']
for document in documents
	score = get_document_score(document)
	print score
