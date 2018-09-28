from common.xdf import load_xdf
import numpy as np


def importing_data(filename):
    raw=load_xdf(filename)
    for i in range(len(raw[0])):
        if raw[0][i]['info']['name']==['Real/Imagery motor movement']:
            exp_data=raw[0][i]
        elif raw[0][i]['info']['name']==['openbci_eeg']:
            EEG_data=raw[0][i]

    return exp_data,EEG_data


def extracting_index(exp_data, eeg_data):   # RST data for the ts of the sentences+recall, data for the indexes (either EEG or Eye-tracking), type= 'sentences' or 'recall'
    #IR= Imagine right, ER= Execute right, IL= Imagine Left, EL = Execute Left, IT= Imagine third arm, RS= Resting state, FT= Final trial

    index_IR=[]
    index_ER=[]
    index_IL = []
    index_EL = []
    index_IT = []
    index_RS = []
    index_FT = []

    [index_IR.append(index) for index, value in enumerate(exp_data['time_series']) if value == [u'img_right']]
    [index_ER.append(index) for index, value in enumerate(exp_data['time_series']) if value == [u'exec_right']]
    [index_IL.append(index) for index, value in enumerate(exp_data['time_series']) if value == [u'img_left']]
    [index_EL.append(index) for index, value in enumerate(exp_data['time_series']) if value == [u'exec_left']]
    [index_IT.append(index) for index, value in enumerate(exp_data['time_series']) if value == [u'imag_third']]
    [index_RS.append(index) for index, value in enumerate(exp_data['time_series']) if value == [u'Start_trial']]
    [index_FT.append(index) for index, value in enumerate(exp_data['time_series']) if value == [u'Finish_trial']]

    index_EEG_IR = []
    index_EEG_ER = []
    index_EEG_IL = []
    index_EEG_EL = []
    index_EEG_IT = []
    index_EEG_RS = []

    for i in index_IR:
        temp_1 = np.where(np.ceil(eeg_data['time_stamps']) == np.ceil(exp_data['time_stamps'][i]))
        if i>=len(exp_data['time_stamps'])-1:
            temp_2 = np.where(eeg_data['time_stamps'] ==np.ceil(exp_data['time_stamps'][index_FT[0]]))
        else:
            temp_2 = np.where(np.ceil(eeg_data['time_stamps']) == np.ceil(exp_data['time_stamps'][i+1]))
        index_EEG_IR.append((temp_1[0][1],temp_2[0][-1]))

    for i in index_ER:
        temp_1 = np.where(np.ceil(eeg_data['time_stamps']) == np.ceil(exp_data['time_stamps'][i]))
        if i>=len(exp_data['time_stamps'])-1:
            temp_2 = np.where(eeg_data['time_stamps'] ==np.ceil(exp_data['time_stamps'][index_FT[0]]))
        else:
            temp_2 = np.where(np.ceil(eeg_data['time_stamps']) == np.ceil(exp_data['time_stamps'][i+1]))
        index_EEG_ER.append((temp_1[0][1],temp_2[0][-1]))

    for i in index_IL:
        temp_1 = np.where(np.ceil(eeg_data['time_stamps']) == np.ceil(exp_data['time_stamps'][i]))
        if i>=len(exp_data['time_stamps'])-1:
            temp_2 = np.where(eeg_data['time_stamps'] ==np.ceil(exp_data['time_stamps'][index_FT[0]]))
        else:
            temp_2 = np.where(np.ceil(eeg_data['time_stamps']) == np.ceil(exp_data['time_stamps'][i+1]))
        index_EEG_IL.append((temp_1[0][1],temp_2[0][-1]))

    for i in index_EL:
        temp_1 = np.where(np.ceil(eeg_data['time_stamps']) == np.ceil(exp_data['time_stamps'][i]))
        if i>=len(exp_data['time_stamps'])-1:
            temp_2 = np.where(eeg_data['time_stamps'] ==np.ceil(exp_data['time_stamps'][index_FT[0]]))
        else:
            temp_2 = np.where(np.ceil(eeg_data['time_stamps']) == np.ceil(exp_data['time_stamps'][i+1]))
        index_EEG_EL.append((temp_1[0][1],temp_2[0][-1]))

    for i in index_IT:
        temp_1 = np.where(np.ceil(eeg_data['time_stamps']) == np.ceil(exp_data['time_stamps'][i]))
        if i >= len(exp_data['time_stamps']) - 1:
            temp_2 = np.where(eeg_data['time_stamps'] == np.ceil(exp_data['time_stamps'][index_FT[0]]))
        else:
            temp_2 = np.where(np.ceil(eeg_data['time_stamps']) == np.ceil(exp_data['time_stamps'][i + 1]))
        index_EEG_IT.append((temp_1[0][1], temp_2[0][-1]))

    for i in index_RS:
        temp_1 = np.where(np.ceil(eeg_data['time_stamps']) == np.ceil(exp_data['time_stamps'][i]))
        if i >= len(exp_data['time_stamps']) - 1:
            temp_2 = np.where(eeg_data['time_stamps'] == np.ceil(exp_data['time_stamps'][index_FT[0]]))
        else:
            temp_2 = np.where(np.ceil(eeg_data['time_stamps']) == np.ceil(exp_data['time_stamps'][i + 1]))
        index_EEG_RS.append((temp_1[0][1], temp_2[0][-1]))

    return index_EEG_IR, index_EEG_ER, index_EEG_IL, index_EEG_EL, index_EEG_IT, index_EEG_RS

def extracting_EEG_data(index_EEG_IR, index_EEG_ER, index_EEG_IL, index_EEG_EL, index_EEG_IT, index_EEG_RS, eeg_data):
    n_trial = len(index_EEG_IR)
    raw_data={}
    temp={}
    temp1={}
    for i in range(n_trial):
        temp1['data']=eeg_data['time_series'][index_EEG_IR[i][0]:index_EEG_IR[i][1]]
        temp1['ts']=eeg_data['time_stamps'][index_EEG_IR[i][0]:index_EEG_IR[i][1]]
        temp['IR']= temp1.copy()
        temp1.clear()

        temp1['data'] = eeg_data['time_series'][index_EEG_ER[i][0]:index_EEG_ER[i][1]]
        temp1['ts'] = eeg_data['time_stamps'][index_EEG_ER[i][0]:index_EEG_ER[i][1]]
        temp['ER']= temp1.copy()
        temp1.clear()

        temp1['data'] = eeg_data['time_series'][index_EEG_IL[i][0]:index_EEG_IL[i][1]]
        temp1['ts'] = eeg_data['time_stamps'][index_EEG_IL[i][0]:index_EEG_IL[i][1]]
        temp['IL']= temp1.copy()
        temp1.clear()

        temp1['data'] = eeg_data['time_series'][index_EEG_EL[i][0]:index_EEG_EL[i][1]]
        temp1['ts'] = eeg_data['time_stamps'][index_EEG_EL[i][0]:index_EEG_EL[i][1]]
        temp['EL']= temp1.copy()
        temp1.clear()

        temp1['data'] = eeg_data['time_series'][index_EEG_IT[i][0]:index_EEG_IT[i][1]]
        temp1['ts'] = eeg_data['time_stamps'][index_EEG_IT[i][0]:index_EEG_IT[i][1]]
        temp['IT']= temp1.copy()
        temp1.clear()

        temp1['data'] = eeg_data['time_series'][index_EEG_RS[i][0]:index_EEG_RS[i][1]]
        temp1['ts'] = eeg_data['time_stamps'][index_EEG_RS[i][0]:index_EEG_RS[i][1]]
        temp['RS']= temp1.copy()
        temp1.clear()

        raw_data[i+1]=temp.copy()
        temp.copy().clear()

    return raw_data