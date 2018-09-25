from common.xdf import load_xdf
import numpy as np


def importing_data(filename):
    raw=load_xdf(filename)
    for i in range(len(raw[0])):
        if raw[0][i]['info']['name']==['Real/Imagery motor movement']:
            exp_data=raw[0][i]
        # elif raw[0][i]['info']['name']==['openbci_eeg']:
        #     EEG_data=raw[0][i]

    return exp_data


def extracting_index(exp_data, egg_data):   # RST data for the ts of the sentences+recall, data for the indexes (either EEG or Eye-tracking), type= 'sentences' or 'recall'
    #IR= Imagine right, ER= Execute right, IL= Imagine Left, EL = Execute Left, IT= Imagine third arm, RS= Resting state

    index_IR=[]
    index_ER=[]
    index_IL = []
    index_EL = []
    index_IT = []
    index_RS = []
    [index_IR.append(index) for index, value in enumerate(exp_data['time_series']) if value == [u'img_right']]
    [index_ER.append(index) for index, value in enumerate(exp_data['time_series']) if value == [u'exec_right']]
    [index_IL.append(index) for index, value in enumerate(exp_data['time_series']) if value == [u'img_left']]
    [index_EL.append(index) for index, value in enumerate(exp_data['time_series']) if value == [u'exec_left']]
    [index_IT.append(index) for index, value in enumerate(exp_data['time_series']) if value == [u'imag_third']]
    [index_RS.append(index) for index, value in enumerate(exp_data['time_series']) if value == [u'Start_trial']]
    stamps_IR = exp_data['time_stamps'][index_IR]#,exp_data['time_stamps'][np.array(index_IR)+1]]         # Start sentence, Final Sentence (indexes)
    stamps_ER = exp_data['time_stamps'][index_ER]#,exp_data['time_stamps'][np.array(index_ER)+1]]         # Start sentence, Final Sentence (indexes)
    stamps_IL = exp_data['time_stamps'][index_IL]#,exp_data['time_stamps'][np.array(index_IL)+1]]         # Start sentence, Final Sentence (indexes)
    stamps_EL = exp_data['time_stamps'][index_EL]#,exp_data['time_stamps'][np.array(index_EL)+1]]         # Start sentence, Final Sentence (indexes)
    stamps_IT = exp_data['time_stamps'][index_IT]#,exp_data['time_stamps'][np.array(index_IT)+1]]   # Start recall, Final recall (indexes)
    stamps_RS = exp_data['time_stamps'][index_RS]#,exp_data['time_stamps'][np.array(index_RS)+1]]   # Start recall, Final recall (indexes)

    return stamps_IR,stamps_ER,stamps_IL,stamps_EL,stamps_IT,stamps_RS
    # index_beg = []
    # index_end = []
    #     for i in range(np.shape(stamps_sent)[1]):
    #         temp_1 = np.where(np.ceil(data['time_stamps']) == np.ceil(stamps_sent[0][i]))
    #         temp_2 = np.where(np.ceil(data['time_stamps']) == np.ceil(stamps_sent[1][i]))
    #         index_beg.append(temp_1[0][1])  #First item for beginning
    #         index_end.append(temp_2[0][-1]) #Last item for ending
    #     return index_beg, index_end
    #
    #     for i in range(np.shape(stamps_recall)[1]):
    #         temp_1 = np.where(np.ceil(data['time_stamps']) == np.ceil(stamps_recall[0][i]))
    #         temp_2 = np.where(np.ceil(data['time_stamps']) == np.ceil(stamps_recall[1][i]))
    #         index_beg.append(temp_1[0][1])  #First item for beginning
    #         index_end.append(temp_2[0][-1]) #Last item for ending
    #     return index_beg, index_end
