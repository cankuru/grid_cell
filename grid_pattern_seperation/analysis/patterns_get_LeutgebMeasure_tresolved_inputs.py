# -*- coding: utf-8 -*-
"""
Created on Sun May 20 11:35:03 2018

@author: DanielM
"""

import os
import numpy as np
import shelve
import os
import analysis_main


def similarity_measure_leutgeb_inputs_directory(data_path, len_bins):
    # Setup some parameters given by paradigm_frequency_inhibition.py
    save_path = data_path
    data_files = [f for f in os.listdir(data_path) if os.path.isfile(os.path.join(data_path, f)) and '.npz' in f and not 'norm' in f and not 'trifilt' in f]
    data_files.sort()
    
    data_files = data_files[0:25]
    
    corr_matrix = np.empty((len(data_files), len(data_files)))
    
    data_list = []
    for x in data_files:
        data_list.append(np.load(data_path + x)['arr_0'])
    
    row_idx_start = 0
    row_idx_stop = 25
    
    outputs = []
    for row_idx, x in enumerate(data_list[row_idx_start:row_idx_stop]):
        for col_idx, y in enumerate(data_list[row_idx+row_idx_start:len(data_list)]):
            outputs.append(analysis_main.similarity_measure_leutgeb(x,y,len_bins))
            
    outputs = np.array(outputs)
    np.savetxt(save_path + "1_leutgeb-measure-tresolved_len-bin_" + str(len_bins) + ".txt", outputs, delimiter="\t")
    
if __name__ == '__main__':
    path = "C:\\Users\\Daniel\\pyDentateData\\pattern_separation_data_local_input_revised\\seed10000\\input_patterns_seed_10000\\"
    len_bins = 1000
    similarity_measure_leutgeb_inputs_directory(path, len_bins)