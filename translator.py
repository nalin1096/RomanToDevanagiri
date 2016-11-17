from transliterate import *

def prepare_data (test_file, list):
	with open(test_file) as f:
		for line in f:
			if (line != '\n'):
				list.append(line.lower())

# test_file  = raw_input ("Enter Data file name: ")
# list = []
# prepare_data(test_file, list)
# for data in list:
# 	print(data)
data = raw_input()
output = transliterate(data)
print(output)
# en_blob = TextBlob(output)
# print(en_blob.translate(to='en'))
# data = raw_input("Text: ")
# output = transliterate(data)
# print(output)
# en_blob = TextBlob(output)
# print(en_blob.translate(to='en'))