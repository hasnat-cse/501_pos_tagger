import nltk

from nltk.tag import hmm

import re


f = open("Domain1Train.txt","r")

contents = f.read()

contents = re.compile("\n").split(contents)

train_data = []

train_data_line = []



for line in contents:

	if not line:
		
		

		train_data.append (train_data_line)

		train_data_line = []

	else:
		

		word_and_tag = re.compile("[ ]+").split(line)

		word_and_tag = tuple(word_and_tag)

		train_data_line.append(word_and_tag)

		






f = open("Domain1Test.txt", "r")

contents = f.read()

contents = re.compile("\n").split(contents)

test_data = []

test_data_line = []

for line in contents:

	if not line:
		
		

		test_data.append (test_data_line)

		test_data_line = []

	else:
		

		word_and_tag = re.compile("[ ]+").split(line)

		word_and_tag = tuple(word_and_tag)

		test_data_line.append(word_and_tag)

tagger = hmm.HiddenMarkovModelTagger.train(train_data,test_data)



