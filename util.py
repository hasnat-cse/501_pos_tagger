import re


# get file name excluding extension
def get_file_name_excluding_extension(file_path):
    # gets the file name as "udhr-yao" from "811_a1_dev/udhr-yao.txt.dev" and "811_a1_train/udhr-yao.txt.tra" for unix
    filename_pattern = r".*[/\\](.+)\..*"

    filename = re.findall(filename_pattern, file_path)

    if len(filename) == 0:
        # gets the file name as "udhr-yao" from "811_a1_dev/udhr-yao and "811_a1_train/udhr-yao" for unix
        filename_pattern = r".*[/\\](.+)\.?.*"

        filename = re.findall(filename_pattern, file_path)

    return filename[0]


# prepare the output file name
def prepare_output_file_path(tagger_name, model_file_path, test_file_path):
    output_file_path = tagger_name + '_' + get_file_name_excluding_extension(model_file_path) + '_' + \
                     get_file_name_excluding_extension(test_file_path) + '_output.txt'

    return output_file_path
