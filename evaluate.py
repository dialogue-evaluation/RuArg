import sys
import os
import pandas as pd
import numpy as np
from sklearn.metrics import f1_score, classification_report


def get_submitted(parent):
    names = [name for name in os.listdir(parent)]
    if len(names) == 0:
        raise RuntimeError('No files in submitted')
    if len(names) > 1:
        if names[1] != "metadata":
            raise RuntimeError('Multiple files in submitted: {}'.format(' '.join(names)))
    return os.path.join(parent, names[0])


def get_reference(parent):
    names = [os.path.join(parent, name) for name in os.listdir(parent)]
    if len(names) == 0:
        raise RuntimeError('No files in reference')
    if len(names) != 1:
        raise RuntimeError('There should be exact one file in reference: {}'.format(' '.join(names)))
    return names[0]


input_dir = sys.argv[1]
output_dir = sys.argv[2]

submit_dir = os.path.join(input_dir, 'res')
truth_dir = os.path.join(input_dir, 'ref')

if not os.path.isdir(submit_dir):
    print("%s doesn't exist" % submit_dir)

if os.path.isdir(submit_dir) and os.path.isdir(truth_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_filename = os.path.join(output_dir, 'scores.txt')
    output_file = open(output_filename, 'w')

    truth_file = get_reference(truth_dir)
    truth = pd.read_csv(truth_file, sep='\t')

    submission_answer_file = get_submitted(submit_dir)
    predicted = pd.read_csv(submission_answer_file, sep='\t')
    predicted = predicted.fillna(100)
    
    print("MASKS")
    f1_masks_stance = f1_score(truth['masks_stance'].values.tolist(), predicted['masks_stance'].values.tolist(), labels=[2, 1, 0], average="macro")
    f1_masks_argument = f1_score(truth['masks_argument'].values.tolist(), predicted['masks_argument'].values.tolist(), labels=[2, 1, 0], average="macro")
    print('f1_masks_stance_macro: ' + str(f1_masks_stance) + '\n')
    print('f1_masks_argument_macro: ' + str(f1_masks_argument) + '\n')

    print("VACCINES")
    f1_vaccines_stance = f1_score(truth['vaccines_stance'].values.tolist(), predicted['vaccines_stance'].values.tolist(), labels=[2, 1, 0], average="macro")
    f1_vaccines_argument = f1_score(truth['vaccines_argument'].values.tolist(), predicted['vaccines_argument'].values.tolist(), labels=[2, 1, 0], average="macro")
    print('f1_vaccines_stance_macro: ' + str(f1_vaccines_stance) + '\n')
    print('f1_vaccines_argument_macro: ' + str(f1_vaccines_argument) + '\n')

    print("QUARANTINE")
    f1_quarantine_stance = f1_score(truth['quarantine_stance'].values.tolist(), predicted['quarantine_stance'].values.tolist(), labels=[2, 1, 0], average="macro")
    f1_quarantine_argument = f1_score(truth['quarantine_argument'].values.tolist(), predicted['quarantine_argument'].values.tolist(), labels=[2, 1, 0], average="macro")
    print('f1_quarantine_stance_macro: ' + str(f1_quarantine_stance) + '\n')
    print('f1_quarantine_argument_macro: ' + str(f1_quarantine_argument) + '\n')

    output_file.write("f1_stance: " + str((f1_masks_stance+f1_vaccines_stance+f1_quarantine_stance)/3) + "\n")
    output_file.write("f1_premise: " + str((f1_masks_argument+f1_vaccines_argument+f1_quarantine_argument)/3) + "\n")
    output_file.close()
