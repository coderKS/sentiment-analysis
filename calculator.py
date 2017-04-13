from nltk import word_tokenize, sent_tokenize
from crawler import getAllCommentsByBlogUrl
import re
def get_word_score(word, seed_dict):
	if word in seed_dict:
		return seed_dict[word]
	else: 
		return 0

def get_document_score(document_path, seed_dict):
	print ("calculating the score of %s" % document_path)

	# with open (document_path, mode='r') as file_in:
	# 	test_txt = file_in.read()

	test_txt = getAllCommentsByBlogUrl(document_path)
 	# tokenize the document
	sent_tokens = sent_tokenize(test_txt)

	word_tokens = []
	for sent in sent_tokens:
		word_token = word_tokenize(sent)
		word_tokens.append(word_token)

	score = 0.0
	words_count = 0
	word_list = []
	for sent in word_tokens:
		for word in sent:
			word = re.sub('[^A-Za-z]+', '', word) # remove special character
			if word == "": 
				continue 
			# print "word = %s" % word
			word_list.append(word)
			score = score + get_word_score(word, seed_dict)
			words_count = words_count + 1

	# pairwise compare (bonus)
	new_score = 0
	for i in xrange(len(word_list)):
		if i == len(word_list) - 1:
			break
		score_word1 = get_word_score(word_list[i], seed_dict)
		score_word2 = get_word_score(word_list[i+1], seed_dict)
		if (score_word1 == 1 and score_word2 == -1) or (score_word1 == -1 and score_word2 == 1):
			new_score = new_score + 1

	new_score = score - new_score
	score = score / words_count 
	new_score = new_score / words_count

	print ("   score = %f" % score)
	print ("   pairwise comparison score = %f" % new_score)
	return score
