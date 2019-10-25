import argparse
import subprocess
import os
import shutil


# for the command:
# python3 pos_stanford_test.py --jar PATH_TO_STANFORD_TAGGER_JAR --model PATH_TO_MODEL_FILE --test PATH_TO_TEST_FILE
#             --output PATH_TO_OUTPUT_FILE
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--jar', dest="jar_path", action="store", required=True)
    parser.add_argument('--model', dest="model_path", action="store", required=True)
    parser.add_argument('--test', dest="test_path", action="store", required=True)
    parser.add_argument('--output', dest="output_path", action="store", required=True)

    args = parser.parse_args()

    return args


def main():
    # parse command line arguments and set the paths accordingly
    args = parse_arguments()
    stanford_pos_tagger_jar_path = args.jar_path
    model_file_path = args.model_path
    test_file_path = args.test_path
    output_file_path = args.output_path

    # stanford_pos_tagger_jar_path = 'StanfordTagger/stanford-postagger.jar'
    # test_file_path = "A3DataCleaned/ELLTest.txt"
    # model_file_path = 'StanfordTagger/TrainedModels/StanfordELL'
    # output_file_path = 'StanfordTagger/ELLTestOutput.txt'

    # read the test file
    f_test = open(test_file_path, "r")
    test_contents = f_test.read()
    f_test.close()

    # replace space between word and tag with '/' in test contents to use by pos tagger
    formatted_test_contents = test_contents.replace(' ', '/')

    # create a temporary directory to hold the formatted contents of test file
    if not os.path.exists('temp'):
        os.mkdir('temp')

    # save the formatted contents of test file to a temporary file to use by the pos tagger
    temp_test_file_path = 'temp/FormattedTestFile.txt'
    f_temp = open(temp_test_file_path, 'w')
    f_temp.write(formatted_test_contents)
    f_temp.close()

    # call the stanford pos tagger to test a file against trained model and write the output
    subprocess.call(
        ['java', '-classpath',
         stanford_pos_tagger_jar_path,
         'edu.stanford.nlp.tagger.maxent.MaxentTagger',
         '-model', model_file_path,
         '-testFile', temp_test_file_path],
        stdout=open(output_file_path, 'w'))

    # read the output file content
    f_read_output = open(output_file_path, 'r')
    output_contents = f_read_output.read()
    f_read_output.close()

    # replace '/' between word and tag with space created by the pos tagger to format the output
    formatted_output_contents = output_contents.replace('/', ' ')

    # write the formatted content to the output file
    f_write_output = open(output_file_path, 'w')
    f_write_output.write(formatted_output_contents)
    f_write_output.close()

    # now delete the temporary directory
    if os.path.exists('temp'):
        shutil.rmtree('temp')


if __name__ == "__main__":
    main()
