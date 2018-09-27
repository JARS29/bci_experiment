#!/usr/bin/env python
# -*- coding: utf-8 -*-


from trials import *

experiment_session = int(raw_input("Session's number? "))
participant = int(raw_input("User's number? "))

text_instructions_1='Olá, Bem-vindo'

text_final_s2 = "Pronto!!!\nO experimento terminou. Aguarde ao experimentador.\n \n" \
                "Muito obrigado pela participação."

# Store info about the experiment session
expName = 'Real/Imagery motor movement'  # from the Builder filename that created this script
expInfo = {u'Session': experiment_session, u'Participant': participant}

thisExp = setting_exp(expName, expInfo)

# Labstreaminglayer setting
outlet=LSL_initizialization(expName, expInfo[u'Session']+expInfo[u'Participant'])

# Setup monitor
win = setting_monitor('default', 80, expInfo)
# Instructions trial
info_trial(win, text_instructions_1)


main_trial(win, thisExp, expInfo, outlet)
outlet.push_sample(['Finish_trial'])
time.sleep(0.0001)


info_trial(win, text_final_s2)

thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()