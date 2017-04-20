from calculator import get_document_score
from dict_parser import get_seeddict, parse_words
import json


# parameters
positive_words_path = 'data/positive.txt'
negative_words_path = 'data/negative.txt'
project_dictionary_path = 'data/dictionary.dat'
# documents = ['data/1155049829.txt', 'data/1155047854.txt', 'data/LAW_Yue_Hei.txt', 'data/Tse_Ching_Hin.txt']
documents = ['https://kamshingblog.wordpress.com', 'https://ierg3320aplus.wordpress.com/', 'https://ierg3320site.wordpress.com/', 'https://kelvin0218xierg3320.wordpress.com/']

def calculate_score(documents, seed_dict):
	documents_scores = dict()

	# calculate score using our dictionary data
	for document in documents:
		print ("Crawling the data from the website %s" % document)
		documents_scores[document] = get_document_score(document, seed_dict)
	# print documents_scores


# start program
print ("########################################")
print ("#                                      #")
print ("#     Sentiment-Analysis (IERG3320)    #")
print ("#             Project 1                #")
print ("#                                      #")
print ("########################################")

print ("Please select the dictioinary source: ")
print ("1. Our own constructed dictionary")
print ("2. Provided dictionary")

val = ''
while (val != '1' and val != '2'):
	val = raw_input("Your Input (1 or 2): ")

if val == '1':
	print ("\nParsing positive and negative words\n")
	word_dict = parse_words(positive_words_path, negative_words_path)
	print ("Getting synonyms and antonyms\n")
	seed_dict = get_seeddict(word_dict)

	calculate_score(documents, seed_dict)
else:
	print ("Reading the provided dictionary data ...\n")
	with open(project_dictionary_path) as fi:
		print ("Done !\n")
		seed_dict = json.load(fi)
		calculate_score(documents, seed_dict)
