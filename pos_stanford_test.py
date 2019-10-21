import subprocess
import os
import shutil


def main():
    stanford_pos_tagger_jar_path = 'StanfordTagger/stanford-postagger.jar'
    test_file_path = "A3DataCleaned/Domain1Test.txt"
    model_path = 'StanfordTagger/TrainedModels/Stanford1'
    output_path = 'StanfordTagger/Domain1TestOutput.txt'

    f_test = open(test_file_path, "r")
    test_contents = f_test.read()
    f_test.close()

    formatted_test_contents = test_contents.replace(' ', '/')

    if not os.path.exists('temp'):
        os.mkdir('temp')

    temp_test_file_path = 'temp/FormattedTestFile.txt'

    f_temp = open(temp_test_file_path, 'w')
    f_temp.write(formatted_test_contents)
    f_temp.close()

    subprocess.call(
        ['java', '-classpath',
         stanford_pos_tagger_jar_path,
         'edu.stanford.nlp.tagger.maxent.MaxentTagger',
         '-model', model_path,
         '-testFile', temp_test_file_path],
        stdout=open(output_path, 'w'))

    f_read_output = open(output_path, 'r')
    output_contents = f_read_output.read()
    f_read_output.close()

    formatted_output_contents = output_contents.replace('/', ' ')

    f_write_output = open(output_path, 'w')
    f_write_output.write(formatted_output_contents)
    f_write_output.close()

    shutil.rmtree('temp')


if __name__ == "__main__":
    main()
