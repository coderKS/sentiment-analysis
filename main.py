from nltk import word_tokenize, sent_tokenize

with open ('data/1155049829.txt', mode='r') as file_in:
	test_txt = file_in.read()

print test_txt
sent_tokens = sent_tokenize(test_txt)
word_tokens = []
for sent in sent_tokens:
	print sent
	word_token = word_tokenize(sent)
	word_tokens.append(word_token)

print wordtokens

# need to build the dictionary
worddict = {'good': 1, 'bad':-1,'like': 1, 'hate':-1}