import re


# get file name excluding extension
def get_file_name_excluding_extension(file_path):

    if file_path.find('/') == -1:
        filename_without_ext = file_path.rsplit('.', 1)[0]
    else:
        filename = file_path.rsplit('/', 1)[1]
        filename_without_ext = filename.rsplit('.', 1)[0]

    return filename_without_ext


# prepare the output file name
def prepare_output_file_path(model_file_path, test_file_path):
    output_file_path = get_file_name_excluding_extension(model_file_path) + '_' + \
                     get_file_name_excluding_extension(test_file_path) + '_output.txt'

    return output_file_path
