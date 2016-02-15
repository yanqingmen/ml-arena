'''basic settings for this workspace'''
import os
import logging

#path settings
CURRENT_PATH = os.path.dirname(__file__)
DATA_FOLDER = os.path.join(CURRENT_PATH, 'data')
MODEL_FOLDER = os.path.join(CURRENT_PATH, 'model')
RESOURCES_FOLDER = os.path.join(CURRENT_PATH, 'resources')
UTIL_FOLDER = os.path.join(CURRENT_PATH, 'util')
TMP_FOLDER = os.path.join(CURRENT_PATH, 'tmp')

# file settings
RAW_FEATURES_CSV = 'raw_features.csv'
DATA_FOR_PREDICT = 'final_features.csv'

#logging settings
logging.basicConfig(level=logging.DEBUG, \
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', \
    datefmt='%a, %d %b %Y %H:%M:%S', \
    filename=os.path.join(CURRENT_PATH, 'tmp/ml.log'), \
    filemode='w')
