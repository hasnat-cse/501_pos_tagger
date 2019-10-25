import nltk

from nltk.tag import *

from nltk.tbl.template import Template

from nltk.tag.brill import Pos, Word

import re

import csv

import numpy as np

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

	f.close()


def get_dictionary(test_file, output_file):


	unique_tag_list = set()

	f1 = open(test_file, "r")

	f2 = open(output_file, "r")


	contents1 = f1.read()

	contents2 = f2.read()

	contents1 = re.compile("\n").split(contents1)

	contents2 = re.compile("\n").split(contents2)


	for i in range (0, len(contents1)):

		line1 = contents1[i]

		line2 = contents2[i]


		if not line1 or not line2:

			continue;

		else : 

			word_and_tag1 = re.compile("[ ]+").split(line1)

			word_and_tag2 = re.compile("[ ]+").split(line2)


			unique_tag_list.add(word_and_tag1[1])

			unique_tag_list.add(word_and_tag2[1])


	f1.close()

	f2.close()



	mapping = {}

	counter = 0

	for tag in unique_tag_list :

		mapping[tag] = counter

		counter += 1

	return mapping, unique_tag_list



def get_confusion_matrix(mapping, test_file, output_file):



	rows, cols = (len(mapping), len(mapping)) 
	confusion_matrix = [[0]*cols]*rows

	


	f1 = open(test_file, "r")

	f2 = open(output_file, "r")


	contents1 = f1.read()

	contents2 = f2.read()

	contents1 = re.compile("\n").split(contents1)

	contents2 = re.compile("\n").split(contents2)

	


	for i in range (0, len(contents1)):

		line1 = contents1[i]

		line2 = contents2[i]


		if not line1 or not line2:

			continue;

		else : 

			word_and_tag1 = re.compile("[ ]+").split(line1)

			word_and_tag2 = re.compile("[ ]+").split(line2)



			

			confusion_matrix[mapping[word_and_tag2[1]]][mapping[word_and_tag1[1]]] += 1

			


	f1.close()

	f2.close()

	print(len(confusion_matrix))

	confusion_matrix = np.array(confusion_matrix)

	return confusion_matrix



def main():	


	train_file = "Domain2Train.txt"
	train_data = pre_process (train_file)


	test_file = "Domain1Test.txt"
	test_data = pre_process (test_file)

	
	hmm_tagger = hmm.HiddenMarkovModelTagger.train(train_data,test_data)

	output_file = "output_hmm_" + train_file + "_" + test_file
	write_output(output_file, test_data, hmm_tagger)


	mapping, unique_tag_list = get_dictionary(test_file, output_file)
	confusion_matrix = get_confusion_matrix(mapping, test_file, output_file)

	

	f = open ("matrix.csv", "w")

	np.savetxt("matrix.csv", confusion_matrix, delimiter="\t")


	Template._cleartemplates() #clear any templates created in earlier tests

	stanfordTagger = StanfordPOSTagger('StanfordTagger/TrainedModels/Stanford1', 'StanfordTagger/stanford-postagger.jar')

	brill_trainer = BrillTaggerTrainer(hmm_tagger, brill.brill24())

	brill_tagger = brill_trainer.train(train_data)

	print(brill_tagger.evaluate(test_data))

	sentence = ["the", "lone", "wolf", "dies", "but" ,"the", "pack", "survives"]

	print(brill_tagger.tag(sentence))




if __name__ == "__main__":
    main()