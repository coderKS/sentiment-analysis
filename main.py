from calculator import get_document_score
from dict_parser import get_seeddict, parse_words

# parameters
positive_words_path = 'data/positive.txt'
negative_words_path = 'data/negative.txt'
# documents = ['data/1155049829.txt', 'data/1155047854.txt', 'data/LAW_Yue_Hei.txt', 'data/Tse_Ching_Hin.txt']
documents = ['https://kamshingblog.wordpress.com', 'https://ierg3320aplus.wordpress.com/', 'https://ierg3320site.wordpress.com/', 'https://kelvin0218xierg3320.wordpress.com/']
documents_scores = dict()

# start program
print ("Parsing positive and negative words\n")
word_dict = parse_words(positive_words_path, negative_words_path)
print ("Getting synonyms and antonyms\n")
seed_dict = get_seeddict(word_dict)

for document in documents:
	documents_scores[document] = get_document_score(document, seed_dict)

print documents_scores