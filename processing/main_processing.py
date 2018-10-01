from data_extraction import *
exp_data, eeg_data = importing_data('common/001_05_2.xdf')
index_EEG_IR, index_EEG_ER, index_EEG_IL, index_EEG_EL, index_EEG_IT, index_EEG_RS= extracting_index(exp_data, eeg_data)
data=extracting_EEG_data(index_EEG_IR, index_EEG_ER, index_EEG_IL, index_EEG_EL, index_EEG_IT, index_EEG_RS, eeg_data)
#xdf2EEGLAB(index_EEG_IR, index_EEG_ER, index_EEG_IL, index_EEG_EL, index_EEG_IT, index_EEG_RS, eeg_data)

