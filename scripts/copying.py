from lib import *

'''

this script will copy all filenames from one folder to another

example usage:

    python copying.py --input ./input

The input folderpath must point to a folder with only a single level subfolders, which will be copied to the output folder

'''

## add an argparse to parse an input folderpath:
parser = argparse.ArgumentParser(description='Copy filenames from one folder to another')
parser.add_argument('--input', type=str, help='Input folder path')

args = parser.parse_args()

input_folder = args.input

classes = []

# now iterate recursively for all folders in the input folder
for root, dirs, filenames in os.walk(input_folder):
    for dir in dirs:
        create_folder(os.path.join(DATASET_PATH, dir))
        classes.append(dir)

    if root != input_folder:
        for filename in filenames:
            foldername = get_path_last_part(root)

            # generate a new unique filename, using hashes:
            new_filename = get_unique_filename(foldername, filename)


            shutil.copy(os.path.join(root, filename), os.path.join(DATASET_PATH,foldername, new_filename))


