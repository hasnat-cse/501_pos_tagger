import subprocess
import os
import shutil


def main():
    stanford_pos_tagger_jar_path = 'StanfordTagger/stanford-postagger.jar'
    props_file_path = 'StanfordTagger/myPropsFile.prop'
    train_file_path = "A3DataCleaned/Domain2Train.txt"
    model_path = 'StanfordTagger/TrainedModels/Stanford2'

    f_train = open(train_file_path, "r")
    train_contents = f_train.read()
    f_train.close()

    formatted_train_contents = train_contents.replace(' ', '/')

    if not os.path.exists('temp'):
        os.mkdir('temp')

    temp_train_file_path = 'temp/FormattedTrainFile.txt'

    f_temp = open(temp_train_file_path, 'w')
    f_temp.write(formatted_train_contents)
    f_temp.close()

    subprocess.call(
        ['java', '-classpath',
         stanford_pos_tagger_jar_path,
         'edu.stanford.nlp.tagger.maxent.MaxentTagger',
         '-props', props_file_path,
         '-model', model_path,
         '-trainFile', temp_train_file_path])

    shutil.rmtree('temp')


if __name__ == "__main__":
    main()
