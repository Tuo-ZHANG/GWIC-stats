import os
import pandas as pd
import csv

dataset_list_1 = ["dwug_es", "dwug_sv", "dwug_de", "dwug_en", "refwug", "surel", "DUPS-WUG", "diawug", "discowug"]

for i in range(len(dataset_list_1)):
    parent_folder = "dataset/" + dataset_list_1[i] + '/data'
    total_number = 0
    for lemma in os.listdir(parent_folder):
        csv_path = os.path.join(parent_folder, lemma, "judgments.csv")
        df = pd.read_csv(csv_path, delimiter='\t', quoting =csv.QUOTE_MINIMAL)
        num_rows = len(df)
        total_number = total_number + num_rows

    print("number of judgments for dataset ", dataset_list_1[i], ": ", str(total_number))


dataset_list_2 = ["nor_dia_change_1", "nor_dia_change_2", "rusemshift_1", "rusemshift_2", "rushifteval1", "rushifteval2", "rushifteval3", "RuDSI"]
list_2 = []

for i in range(len(dataset_list_2)):
    parent_folder = "dataset/" + dataset_list_2[i] + '/data'
    total_number = 0
    for lemma in os.listdir(parent_folder):
        csv_path = os.path.join(parent_folder, lemma, "judgments.csv")
        df = pd.read_csv(csv_path, delimiter='\t', quoting =csv.QUOTE_MINIMAL)
        num_rows = len(df)
        total_number = total_number + num_rows

    print("number of judgments for dataset ", dataset_list_2[i], ": ", str(total_number))
    list_2.append(total_number)

print(list_2[0] + list_2[1])
print(list_2[2] + list_2[3])
print(list_2[4] + list_2[5] + list_2[6])