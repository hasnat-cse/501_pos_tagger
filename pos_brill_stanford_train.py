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
    parser.add_argument('--jar', dest="jar_path", action="store", required=True)
    parser.add_argument('--model', dest="model_path", action="store", required=True)
    parser.add_argument('--train', dest="train_path", action="store", required=True)

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
    jar_file = args.jar_path
    model_file = args.model_path
    
    train_file = args.train_path

    train_data = pre_process (train_file)
    

    stanford_tagger=StanfordPOSTagger(model_filename=model_file, path_to_jar=jar_file)

    brill_trainer = BrillTaggerTrainer(stanford_tagger, brill.fntbl37())

    brill_tagger = brill_trainer.train(train_data)

    


    with open(model_file, 'wb') as f:
        dill.dump(brill_tagger, f)


if __name__ == "__main__":
    main()
