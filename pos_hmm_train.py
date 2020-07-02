import nltk

from nltk.tag import *

from nltk.tbl.template import Template

from nltk.tag.brill import Pos, Word

import re

import csv

import numpy as np

import dill
import argparse


# for the command:
# python3 pos_nltk_train.py --train PATH_TO_TRAIN_FILE --model PATH_TO_MODEL_FILE
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', dest="train_path", action="store", required=True)
    parser.add_argument('--model', dest="model_path", action="store", required=True)

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

            data_line.append(word_and_tag)

    f.close()
    return data;


def main():
    args = parse_arguments()
    train_file = args.train_path
    model_file = args.model_path

    train_data = pre_process(train_file)

    hmm_tagger = hmm.HiddenMarkovModelTagger.train(train_data)


    with open(model_file, 'wb') as f:
        dill.dump(hmm_tagger, f)


if __name__ == "__main__":
    main()
