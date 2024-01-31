from constants import *
import shutil
import os
import hashlib
import argparse


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def get_path_last_part(path):
    return os.path.basename(path)

def get_unique_filename(foldername, filename):
    file_extension = filename.split('.')[-1]
    return hashlib.md5((foldername + filename).encode('utf-8')).hexdigest() + '.' + file_extension