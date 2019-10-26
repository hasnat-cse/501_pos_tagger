import nltk

from nltk.tag import *

from nltk.tbl.template import Template

from nltk.tag.brill import Pos, Word

import re

import csv

import numpy as np

import dill
import argparse
from util import prepare_output_file_path


# for the command:
# python3 pos_nltk_test.py --model PATH_TO_MODEL_FILE --test PATH_TO_TEST_FILE
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', dest="model_path", action="store", required=True)
    parser.add_argument('--test', dest="test_path", action="store", required=True)

    args = parser.parse_args()

    return args


def pre_process(filename):
    f = open(filename, "r")

    contents = f.read()

    contents = re.compile("\n").split(contents)

    data = []

    data_line = []

    for line in contents:

        if not line:

            data.append(data_line)

            data_line = []

        else:

            word_and_tag = re.compile("[ ]+").split(line)

            word_and_tag = tuple(word_and_tag)

            if (len(word_and_tag)!=2):

                temp = (word_and_tag[0], word_and_tag[1])
                word_and_tag = temp


            data_line.append(word_and_tag)

    f.close()
    return data;


def write_output(output_file, test_data, tagger):
    f = open(output_file, "w")

    for line in test_data:

        sentence = []

        for pair in line:
            sentence.append(pair[0])

        word_and_tag = tagger.tag(sentence)

        for pair in word_and_tag:
            f.write(pair[0] + " " + pair[1] + "\n")

        f.write("\n")

    f.close()


def get_dictionary(test_file, output_file):
    # unique_tag_list = set()
    unique_tag_list = []

    f1 = open(test_file, "r")

    f2 = open(output_file, "r")

    contents1 = f1.read()

    contents2 = f2.read()

    contents1 = re.compile("\n").split(contents1)

    contents2 = re.compile("\n").split(contents2)

    for i in range(0, len(contents1)):

        line1 = contents1[i]

        line2 = contents2[i]

        if not line1 or not line2:

            continue;

        else:

            word_and_tag1 = re.compile("[ ]+").split(line1)

            word_and_tag2 = re.compile("[ ]+").split(line2)

            if word_and_tag1[1] not in unique_tag_list:
                unique_tag_list.append(word_and_tag1[1])

            if word_and_tag2[1] not in unique_tag_list:
                unique_tag_list.append(word_and_tag2[1])

    f1.close()

    f2.close()

    mapping = {}

    counter = 0

    for tag in unique_tag_list:
        mapping[tag] = counter

        counter += 1

    return mapping, unique_tag_list


def get_confusion_matrix(mapping, test_file, output_file):
    confusion_matrix = np.zeros(shape=(len(mapping), len(mapping)))

    f1 = open(test_file, "r")

    f2 = open(output_file, "r")

    contents1 = f1.read()

    contents2 = f2.read()

    contents1 = re.compile("\n").split(contents1)

    contents2 = re.compile("\n").split(contents2)

    for i in range(0, len(contents1)):

        line1 = contents1[i]

        line2 = contents2[i]

        if not line1 or not line2:

            continue;

        else:

            word_and_tag1 = re.compile("[ ]+").split(line1)

            word_and_tag2 = re.compile("[ ]+").split(line2)

            confusion_matrix[mapping[word_and_tag2[1]]][mapping[word_and_tag1[1]]] += 1

    f1.close()

    f2.close()

    confusion_matrix = np.array(confusion_matrix)

    return confusion_matrix


def main():
    args = parse_arguments()
    test_file = args.test_path
    model_file = args.model_path

    test_data = pre_process(test_file)

    with open(model_file, 'rb') as f:
        hmm_tagger = dill.load(f)

    
    print(hmm_tagger.evaluate(test_data))

    output_file = prepare_output_file_path(model_file, test_file)
    write_output(output_file, test_data, hmm_tagger)

    mapping, unique_tag_list = get_dictionary(test_file, output_file)
    confusion_matrix = get_confusion_matrix(mapping, test_file, output_file)

    f = open("matrix.csv", "w")

    np.savetxt("matrix.csv", confusion_matrix, delimiter="\t")


    row = ["matrix\t"]

    

    for i in range (0, len(mapping)):

        for x in mapping.keys():

        	if (mapping[x] == i):

        		to_append = x

        		if (to_append == ","):

        			row.append("comma\t")

        		else :

        			row.append(to_append + "\t")



	
    with open("matrix.csv", "r") as readFile:

        reader = csv.reader(readFile)

        lines = list(reader)

        lines[0] = row


    with open ("matrix.csv", "w") as writeFile:

        writer = csv.writer(writeFile)

        writer.writerows(lines)


   


if __name__ == "__main__":
    main()
