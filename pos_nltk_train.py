import nltk

from nltk.tag import *

from nltk.tbl.template import Template

from nltk.tag.brill import Pos, Word

import re

import csv

import numpy as np

import dill

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

			word_and_tag = tuple(word_and_tag)

			data_line.append(word_and_tag)


	f.close()
	return data;





def main():	

	
	train_file = input("Enter train file :")
	train_data = pre_process (train_file)


	hmm_tagger = hmm.HiddenMarkovModelTagger.train(train_data)

	print(hmm_tagger)

	with open('my_tagger.dill', 'wb') as f:
		dill.dump(hmm_tagger, f)






if __name__ == "__main__":
    main()