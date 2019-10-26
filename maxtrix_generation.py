import re

import csv

import numpy as np

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

test_file = 'A3DataCleaned/Domain2Test.txt'
output_file = 'Stanford2_Domain2Test_output.txt'

mapping, unique_tag_list = get_dictionary(test_file, output_file)
confusion_matrix = get_confusion_matrix(mapping, test_file, output_file)

matrix_file_name = 'Stanford2_matrix.csv'

f = open(matrix_file_name, "w")

np.savetxt(matrix_file_name, confusion_matrix, delimiter="\t")

row = ["matrix\t"]

for i in range(0, len(mapping)):

    for x in mapping.keys():

        if (mapping[x] == i):

            to_append = x

            if (to_append == ","):

                row.append("comma\t")

            else:

                row.append(to_append + "\t")

with open(matrix_file_name, "r") as readFile:
    reader = csv.reader(readFile)

    lines = list(reader)

    lines[0] = row

with open(matrix_file_name, "w") as writeFile:
    writer = csv.writer(writeFile)

    writer.writerows(lines)
