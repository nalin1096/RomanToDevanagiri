# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from textblob import TextBlob
import re

consonants = {
	'k':u'\u0915',
	'kh':u'\u0916',
	'g':u'\u0917',
	'gh':u'\u0918',
	'c':u'\u091A',
	'ch':u'\u091B',
	'j':u'\u091C',
	'jh':u'\u091D',
	'ny':u'\u091E',
	'tt':u'\u091F',
	'tth':u'\u0920',
	'dd':u'\u0921',
	'ddh':u'\u0922',
	'nn':u'\u0923',
	't':u'\u0924',
	'th':u'\u0925',
	'd':u'\u0926',
	'dh':u'\u0927',
	'n':u'\u0928',
	'nnn':u'\u0929',
	'p':u'\u092A',
	'ph':u'\u092B',
	'b':u'\u092C',
	'bh':u'\u092D',
	'm':u'\u092E',
	'y':u'\u092F',
	'r':u'\u0930',
	'z':u'\u095B',
	'l':u'\u0932',
	'w':u'\u0935',
	'v':u'\u0935',
	'sh':u'\u0936',
	'ss':u'\u0937',
	's':u'\u0938',
	'h':u'\u0939',
	'a':u'\u0905',
	'aa':u'\u0906',
	'i':u'\u0907',
	'ii':u'\u0908',
	'u':u'\u0909',
	'uu':u'\u090A',
	'e':u'\u090F',
	'ai':u'\u0910',
	'o':u'\u0913',
	'au':u'\u0914'
}

matras = {
	'aa':u'\u093E',
	'i':u'\u093F',
	'ii':u'\u0940',
	'u':u'\u0941',
	'uu':u'\u0942',
	'oo':u'\u0942',
	'r':u'\u0943',
	'rr':u'\u0944',
	'e':u'\u0947',
	'ai':u'\u0948',
	'o':u'\u094B',
	'au':u'\u094C',
	'ain':u'\u0948' + u'\u0902',
	# 'aun':u'\u094C' + u'\u0902',
	'oon':u'\u0942' + u'\u0901',
	'ein':u'\u0947' + u'\u0902'
}


def helper (buf, data):
	global i
	len_data = len(data)
	temp_buf = ""

	if (i==len_data):
		return temp_buf

	if (len_data - i >=3):
		token = data[i:i+3]
	else:
		token = data[i:]
	while token:
		if token in matras:
			i = i+len(token)
			if (token=='i' and i==len_data):
				temp_buf = buf + u'\u0940'
				break
			temp_buf = buf + matras[token]
			break
		else:
			token = token[:-1]
	if (temp_buf==""):
		if (data[i] == 'a'):
			i = i+1
			temp_buf="no_viram"
	return temp_buf

def transliterate (data):
	global i
	words = re.split(r'(>+|!+|]+|\?+|,+|\.+| +|\n+)',data.lower())
	sentence = ""

	for word in words:
		if (len(word)<=1):
			sentence = sentence + word
		else:
			i = 0
			buf = ""
			len_data = len(word)

			while i<len_data:
				if (len_data - i >=3):
					token = word[i:i+3]
				else:
					token = word[i:]
				while token:
					if token in consonants:
						i = i+len(token)
						if (token=='a' or token=='aa' or token=='i' or token=='ii' or token=='u' or token=='uu' or token=='e' or token=='ai' or token=='o' or token=='au'):
							buf = buf + consonants[token]
							break


						temp = helper(consonants[token],word)

						if temp == "no_viram":
							if (len_data==i):
								tok = consonants[token] + u'\u093E'
								buf = buf + tok
							else:
								buf = buf + consonants[token]
						elif temp == "":
							if (len_data!=i):
								tok = consonants[token] + u'\u094D'
								buf = buf + tok 
							else:
								buf = buf + consonants[token]
						else:
							buf = buf + temp
						break
					else:
						token = token[:-1]
			sentence = sentence + buf
	return sentence

