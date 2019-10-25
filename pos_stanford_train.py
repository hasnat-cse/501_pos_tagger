import argparse
import subprocess
import os
import shutil


# for the command:
# python3 pos_stanford_train.py --jar PATH_TO_STANFORD_TAGGER_JAR --prop PATH_TO_PROP_FILE --model PATH_TO_MODEL_FILE
#            --train PATH_TO_TRAIN_FILE
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--jar', dest="jar_path", action="store", required=True)
    parser.add_argument('--prop', dest="prop_path", action="store", required=True)
    parser.add_argument('--model', dest="model_path", action="store", required=True)
    parser.add_argument('--train', dest="train_path", action="store", required=True)

    args = parser.parse_args()

    return args


def main():
    # parse command line arguments and set the paths accordingly
    args = parse_arguments()
    stanford_pos_tagger_jar_path = args.jar_path
    props_file_path = args.prop_path
    model_file_path = args.model_path
    train_file_path = args.train_path

    # stanford_pos_tagger_jar_path = 'StanfordTagger/stanford-postagger.jar'
    # props_file_path = 'StanfordTagger/stanfordPropsFile.prop'
    # train_file_path = "A3DataCleaned/ELLTrain.txt"
    # model_file_path = 'StanfordTagger/TrainedModels/StanfordELL'

    # read the training file
    f_train = open(train_file_path, "r")
    train_contents = f_train.read()
    f_train.close()

    # replace space between word and tag with '/' in train content to use by pos tagger
    formatted_train_contents = train_contents.replace(' ', '/')

    # create a temporary directory to hold the formatted contents of train file
    if not os.path.exists('temp'):
        os.mkdir('temp')

    # save the formatted contents of train file to a temporary file to use by the pos tagger
    temp_train_file_path = 'temp/FormattedTrainFile.txt'
    f_temp = open(temp_train_file_path, 'w')
    f_temp.write(formatted_train_contents)
    f_temp.close()

    # call the stanford pos tagger to train a model using train file
    subprocess.call(
        ['java', '-classpath',
         stanford_pos_tagger_jar_path,
         'edu.stanford.nlp.tagger.maxent.MaxentTagger',
         '-props', props_file_path,
         '-model', model_file_path,
         '-trainFile', temp_train_file_path])

    # now delete the temporary directory
    if os.path.exists('temp'):
        shutil.rmtree('temp')


if __name__ == "__main__":
    main()
