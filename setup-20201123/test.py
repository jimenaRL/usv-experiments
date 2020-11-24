import numpy as np
import pandas as pd
from time import time

from sklearn import metrics
from sklearn import decomposition
from sklearn.cluster import (KMeans, AgglomerativeClustering)

SEED = 666

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
import seaborn as sns
sns.set_style('white')

from audiovocana.dataset import get_dataset
from audiovocana.preprocessing import get_dataframe

PLOT = True
RESULTS_FOLDER = "/home/utilisateur/Desktop/palomars/ultra-sonic-vocalizations/experiments/setup-20201123/results"

# full
csv_path = '/home/utilisateur/Desktop/palomars/data/setup/dataset.csv'
cache_folder = '/home/utilisateur/Desktop/palomars/cache/setup_dataset'
xlsx_folder = "/home/utilisateur/Desktop/palomars/data/setup/_all"
audio_folder = "/media/utilisateur/lacieExFAT/paloma-USV-data/setup"


df = get_dataframe(
    kind='setup',
    xlsx_folder=xlsx_folder,
    audio_folder=audio_folder,
    csv_path=csv_path,
    recompute=True,
    save=False
)

print(df.head())

# dataset = get_dataset(
#     df=df,
#     cache_folder=cache_folder,
#     shuffle=True,
#     recompute=True
# )

# sample = next(iter(dataset))

# print(list(sample.keys()))

# print(sample['audio_path'].numpy())
