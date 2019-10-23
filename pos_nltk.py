import nltk

from nltk.tag import *

from nltk.tbl.template import Template



import re


f = open("A3DataCleaned/Domain2Train.txt","r")

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

		if (len(word_and_tag)!=2):

			print(word_and_tag)

		word_and_tag = tuple(word_and_tag)

		train_data_line.append(word_and_tag)

		






f = open("A3DataCleaned/Domain1Test.txt", "r")

contents = f.read()

contents = re.compile("\n").split(contents)

test_data = []

test_data_line = []

for line in contents:

	if not line:
		
		

		test_data.append (test_data_line)

		test_data_line = []

	else:
		

		if (len(word_and_tag)!=2):

			print(word_and_tag)

		word_and_tag = re.compile("[ ]+").split(line)

		word_and_tag = tuple(word_and_tag)

		test_data_line.append(word_and_tag)

hmm_tagger = hmm.HiddenMarkovModelTagger.train(train_data,test_data)



#sentence = ["lone" ,"wolf", "dies", "and", "the", "pack", "survives"]

#print(hmm_tagger.tag(sentence))

#print(hmm_tagger.evaluate(test_data))

Template._cleartemplates() #clear any templates created in earlier tests



brill_trainer = BrillTaggerTrainer(hmm_tagger, brill.brill24())

brill_tagger = brill_trainer.train(train_data)

print(brill_tagger.evaluate(test_data))

#brill_tagger.evaluate(test_data)



