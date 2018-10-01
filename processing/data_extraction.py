from common.xdf import load_xdf
import csv
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

def xdf2EEGLAB(index_EEG_IR, index_EEG_ER, index_EEG_IL, index_EEG_EL, index_EEG_IT, index_EEG_RS, eeg_data):

    with open('raw_EEGLAB.csv', 'wb') as nf:
        newf = csv.writer(nf, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        newf.writerow(['Time',
                       'F3',
                       'Fz',
                       'F4',
                       'C3',
                       'Cz',
                       'C4',
                       'P3',
                       'P4'])
        for i in range(len(eeg_data['time_stamps'])):
            newf.writerow([eeg_data['time_stamps'][i]] + eeg_data['time_series'][i].tolist())
    with open('event_EEGLAB.csv', 'wb') as nf:
        newf = csv.writer(nf, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        newf.writerow(['Latency',
                       'Type',
                       'Epoch',
                       'Position'])

        for i in range(len(index_EEG_IR)):
            temp=[index_EEG_IR[i][0], index_EEG_ER[i][0], index_EEG_IL[i][0], index_EEG_EL[i][0], index_EEG_IT[i][0]]
            i_temp=np.argsort(temp)
            t = 0
            t1 = 0
            for j in i_temp:
                newf.writerow([eeg_data['time_stamps'][index_EEG_RS[t+5*i][0]], 'RS', i+1, t1])
                t1 = t1+1
                if j==0:
                    newf.writerow([eeg_data['time_stamps'][temp[j]], 'IR', i+1, t1])
                    t1 = t1+1
                if j==1:
                    newf.writerow([eeg_data['time_stamps'][temp[j]], 'ER', i+1, t1])
                    t1 = t1+1
                if j==2:
                    newf.writerow([eeg_data['time_stamps'][temp[j]], 'IL', i+1, t1])
                    t1 = t1+1
                if j==3:
                    newf.writerow([eeg_data['time_stamps'][temp[j]], 'EL', i+1, t1])
                    t1 = t1+1
                if j==4:
                    newf.writerow([eeg_data['time_stamps'][temp[j]], 'IT', i+1, t1])
                    t1 = t1+1
                t = +1


def extracting_EEG_data(index_EEG_IR, index_EEG_ER, index_EEG_IL, index_EEG_EL, index_EEG_IT, index_EEG_RS, eeg_data):
    n_trial = len(index_EEG_IR)
    raw_data={}
    temp={}
    temp1={}
    #Time:8Hz,Epoch,O1,O2,Pz,P1,P2,Event Id,Event Date,Event Duration
    with open('raw_EEG.csv', 'w') as nf:   #Changed by python 3 for MNE
        newf = csv.writer(nf, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #newf.writerow(['Time','chan1','chan2','chan3','chan4','chan5','chan6','chan7','chan8','Sample_rate'])
        #Failed  importing Open vibe
        newf.writerow(['Time:250Hz',
                       'Epoch',
                       'F3',
                       'Fz',
                       'F4',
                       'C3',
                       'Cz',
                       'C4',
                       'P3',
                       'P4',
                       'Event Id',
                       'Event Date',
                       'Event Duration'])

        for i in range(n_trial):
            temp1['data']=eeg_data['time_series'][index_EEG_IR[i][0]:index_EEG_IR[i][1]]
            temp1['ts']=eeg_data['time_stamps'][index_EEG_IR[i][0]:index_EEG_IR[i][1]]
            #temp1['ts'] = np.round(temp1['ts'] - temp1['ts'][0], 3)
            for j,k in zip(temp1['ts'],temp1['data']):
                #newf.writerow([j] + k.tolist() + [250])
                newf.writerow([j, i] + k.tolist() + [0, j, 4]) #Failed importing Openvibe
            temp['IR'] = temp1.copy()
            temp1.clear()

            temp1['data'] = eeg_data['time_series'][index_EEG_ER[i][0]:index_EEG_ER[i][1]]
            temp1['ts'] = eeg_data['time_stamps'][index_EEG_ER[i][0]:index_EEG_ER[i][1]]
            #temp1['ts'] = np.round(temp1['ts'] - temp1['ts'][0], 3)
            for j,k in zip(temp1['ts'],temp1['data']):
                #newf.writerow([j] + k.tolist() + [250])
                newf.writerow([j, i] + k.tolist() + [1, j, 4]) #Failed importing Openvibe
            temp['ER']= temp1.copy()
            temp1.clear()

            temp1['data'] = eeg_data['time_series'][index_EEG_IL[i][0]:index_EEG_IL[i][1]]
            temp1['ts'] = eeg_data['time_stamps'][index_EEG_IL[i][0]:index_EEG_IL[i][1]]
            #temp1['ts'] = np.round(temp1['ts'] - temp1['ts'][0], 3)
            for j,k in zip(temp1['ts'],temp1['data']):
                #newf.writerow([j] + k.tolist() + [250])
                newf.writerow([j, i] + k.tolist() + [2, j, 4]) #Failed importing Openvibe
            temp['IL']= temp1.copy()
            temp1.clear()

            temp1['data'] = eeg_data['time_series'][index_EEG_EL[i][0]:index_EEG_EL[i][1]]
            temp1['ts'] = eeg_data['time_stamps'][index_EEG_EL[i][0]:index_EEG_EL[i][1]]
            #temp1['ts'] = np.round(temp1['ts'] - temp1['ts'][0], 3)
            for j,k in zip(temp1['ts'],temp1['data']):
                #newf.writerow([j] + k.tolist() + [250])
                newf.writerow([j, i] + k.tolist() + [3, j, 4]) #Failed importing Openvibe
            temp['EL']= temp1.copy()
            temp1.clear()

            temp1['data'] = eeg_data['time_series'][index_EEG_IT[i][0]:index_EEG_IT[i][1]]
            temp1['ts'] = eeg_data['time_stamps'][index_EEG_IT[i][0]:index_EEG_IT[i][1]]
            #temp1['ts'] = np.round(temp1['ts'] - temp1['ts'][0], 3)
            for j,k in zip(temp1['ts'],temp1['data']):
                #newf.writerow([j] + k.tolist() + [250])
                newf.writerow([j, i] + k.tolist() + [4, j, 4]) #Failed importing Openvibe
            temp['IT']= temp1.copy()
            temp1.clear()

            temp1['data'] = eeg_data['time_series'][index_EEG_RS[i][0]:index_EEG_RS[i][1]]
            temp1['ts'] = eeg_data['time_stamps'][index_EEG_RS[i][0]:index_EEG_RS[i][1]]
            #temp1['ts'] = np.round(temp1['ts'] - temp1['ts'][0], 3)
            for j,k in zip(temp1['ts'],temp1['data']):
                #newf.writerow([j] + k.tolist() + [250])
                newf.writerow([j, i] + k.tolist() + [5, j, 4]) #Failed importing Openvibe
            temp['RS']= temp1.copy()
            temp1.clear()

            raw_data[++1]=temp.copy()
            temp.copy().clear()

    return raw_data