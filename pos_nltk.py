import nltk

from nltk.tag import *

from nltk.tbl.template import Template

from nltk.tag.brill import Pos, Word

import re

def pre_process(filename):

	f = open(filename, "r")

	contents = f.read()

	contents = re.compile("\n").split(contents)

	data = []

	data_line = []



	for line in contents:

		if not line:
			
			

			
			data.append (data_line)

			data_line = []

		else:
			

			word_and_tag = re.compile("[ ]+").split(line)

			if (len(word_and_tag)!=2):

				print(word_and_tag)

			word_and_tag = tuple(word_and_tag)

			data_line.append(word_and_tag)


	return data;


def write_output (output_file, test_data, tagger):


	f = open (output_file, "w")

	for line in test_data:


		sentence = []

		for pair in line :

			sentence.append(pair[0])


		word_and_tag = tagger.tag(sentence)

		for pair in word_and_tag :

			f.write(pair[0]+ " " + pair[1] + "\n")

		f.write("\n")



def main():	


	train_file = "Domain2Train.txt"
	

	train_data = pre_process (train_file)


	test_file = "Domain1Test.txt"


	test_data = pre_process (test_file)

	
	hmm_tagger = hmm.HiddenMarkovModelTagger.train(train_data,test_data)

	output_file = "output_hmm_" + train_file + "_" + test_file

	write_output(output_file, test_data, hmm_tagger)
	


	Template._cleartemplates() #clear any templates created in earlier tests



	brill_trainer = BrillTaggerTrainer(hmm_tagger, brill.brill24())

	brill_tagger = brill_trainer.train(train_data)

	print(brill_tagger.evaluate(test_data))

	#brill_tagger.evaluate(test_data)




if __name__ == "__main__":
    main()