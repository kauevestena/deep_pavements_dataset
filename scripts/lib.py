from constants import *
import shutil
import os
import hashlib
import argparse
import pandas as pd
import plotly.express as px

raw_reports_path = os.path.join('analysis', 'raw_reports_first_test')

class_label = 'class'
prediction_label = 'prediction'

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def get_path_last_part(path):
    return os.path.basename(path)

def get_unique_filename(foldername, filename):
    file_extension = filename.split('.')[-1]
    return hashlib.md5((foldername + filename).encode('utf-8')).hexdigest() + '.' + file_extension

def read_raw_reports(inpath = raw_reports_path):
    available_classes = os.listdir(inpath)

    model_names = []

    dfs_dict = {}
    for available_class in available_classes:
        dfs_dict[available_class] = {}

        class_path = os.path.join(inpath, available_class)

        available_models = os.listdir(class_path)

        for available_model in available_models:
            base_df = pd.read_csv(os.path.join(class_path, available_model))

            base_df[class_label] = available_class

            model_name = available_model.replace('.csv', '')

            dfs_dict[available_class][model_name] = base_df

            model_names.append(model_name)

    return dfs_dict, [cname.replace('_', ' ') for cname in available_classes], list(set(model_names))