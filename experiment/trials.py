#!/usr/bin/env python
# -*- coding: utf-8 -*-

from psychopy import  visual, core, data, event, logging, monitors, sound
from psychopy.constants import (NOT_STARTED, STARTED,
                                STOPPED, FINISHED)
from pylsl import StreamInfo, StreamOutlet
import time
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

globalClock = core.Clock()  # to track the time since experiment started
endExpNow = False  # flag for 'escape' or other condition => quit the exp

def LSL_initizialization(expName, user_info):
    info = StreamInfo(expName, 'Markers', 1, 0, 'string', str(user_info))
    outlet = StreamOutlet(info)
    raw_input('Setting LSL \nPlease press Enter for starting')
    return outlet


# Experiment information
def setting_exp(expName,expInfo):
    # Path
    _thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
    os.chdir(_thisDir)
    # Pop-up window
    # dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
    # if dlg.OK == False:
    #     core.quit()  # user pressed cancel
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    expInfo['expName'] = expName

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' % (expInfo['Session'], expInfo['Participant'])

    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='',
                                     extraInfo=expInfo, runtimeInfo=None,
                                     originPath=None,
                                     savePickle=True, saveWideText=True,
                                     dataFileName=filename)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename + '.log', level=logging.WARNING)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
    return thisExp



# Monitor
def setting_monitor(name, distance, expInfo):
    # Setup Monitor
    from win32api import GetSystemMetrics

    mon = monitors.Monitor(name)
    mon.setDistance(distance)
    mon_size = mon.getSizePix()
    if mon_size==None:
        mon_size=[GetSystemMetrics(0),GetSystemMetrics(1)]
    print(mon_size)
    # Setup Window
    win = visual.Window(
        size=mon_size, fullscr=True, screen=0,
        allowGUI=False, allowStencil=False,
        monitor=mon, color='black', colorSpace='rgb',
        blendMode='avg', useFBO=True,
        units='norm')
    expInfo['frameRate'] = win.getActualFrameRate()
    if expInfo['frameRate'] != None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess

    return win

# Instructions trial
def info_trial(win, text, endExpNow=endExpNow):
    instructPracticeClock = core.Clock()
    instruction_stimuli = visual.TextStim(win=win, name='instr1',
                             text=text, font='Arial',
                             pos=[-0.1, 0], height=0.1, wrapWidth=1.5, ori=0,
                             bold=True, depth=1,
                             color='white', colorSpace='rgb', opacity=1)

    # ------Prepare to start Routine "instructPractice"-------
    t = 0
    instructPracticeClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_instruction = event.BuilderKeyResponse()
    # keep track of which components have finished
    instructPracticeComponents = [instruction_stimuli, key_instruction]
    for thisComponent in instructPracticeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "instructPractice"-------
    while continueRoutine:
        # get current time
        t = instructPracticeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *instr1* updates
        if t >= 0.0 and instruction_stimuli.status == NOT_STARTED:
            # keep track of start time/frame for later
            instruction_stimuli.tStart = t
            instruction_stimuli.frameNStart = frameN  # exact frame index
            instruction_stimuli.setAutoDraw(True)

        # *ready1* updates
        if t >= 0.0 and key_instruction.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_instruction.tStart = t
            key_instruction.frameNStart = frameN  # exact frame index
            key_instruction.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_instruction.status == STARTED:
            theseKeys = event.getKeys()

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructPracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "instructPractice"-------
    for thisComponent in instructPracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructPractice" was not non-slip safe, so reset the non-slip timer


# Main trial
def main_trial(win, thisExp, expInfo, outlet, endExpNow=endExpNow ):
    trialClock = core.Clock()
    sound_1 = sound.Sound('440', secs=1.0)
    sound_1.setVolume(1)
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine
    fixation_cross = visual.ImageStim(
                win=win, name='image',
                image=u'common\\recall_cross.png', mask=None,
                ori=0, pos=(0, 0), size=(1, 1),
                color=[1,1,1], colorSpace='rgb', opacity=1,
                flipHoriz=False, flipVert=False,
                texRes=128, interpolate=True, depth=0.0)
    arrow_image = visual.ImageStim(
                win=win, name='image',
                image='sin', mask=None,
                ori=0.0, pos=(0, 0), size=(1, 1),
                color=[1,1,1], colorSpace='rgb', opacity=1,
                flipHoriz=False, flipVert=False,
                texRes=128, interpolate=True, depth=-2.0)

    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=5, method='random',
                               extraInfo=expInfo, originPath=-1,
                               trialList=data.importConditions(u'common\\conditions.xlsx'),
                               seed=None, name='trials')

    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec ('{} = thisTrial[paramName]'.format(paramName))


    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        outlet.push_sample(['Start_trial'])
        time.sleep(0.0001)
        if thisTrial != None:
            for paramName in thisTrial:
                exec ('{} = thisTrial[paramName]'.format(paramName))

        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(7.000000)
        # update component parameters for each repeat
        sound_1.setSound('440', secs=1.0)
        arrow_image.setImage(img)
        # keep track of which components have finished
        trialComponents = [sound_1, fixation_cross, arrow_image]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # start/stop sound_1
            if t >= 2 and sound_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                sound_1.tStart = t
                sound_1.frameNStart = frameN  # exact frame index
                sound_1.play()  # start the sound (it finishes automatically)
                outlet.push_sample(['Start_sound'])
                time.sleep(0.0001)

            # *polygon* updates
            if t >= 2 and fixation_cross.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation_cross.tStart = t
                fixation_cross.frameNStart = frameN  # exact frame index
                fixation_cross.setAutoDraw(True)
                outlet.push_sample(['Start_fixation'])
                time.sleep(0.0001)
            frameRemains = 2 + 5 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation_cross.status == STARTED and t >= frameRemains:
                fixation_cross.setAutoDraw(False)

            # *image* updates
            if t >= 3.0 and arrow_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                arrow_image.tStart = t
                arrow_image.frameNStart = frameN  # exact frame index
                arrow_image.setAutoDraw(True)
                outlet.push_sample(['Start_arrow'])
                time.sleep(0.0001)

            frameRemains = 3.0 + 1.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if arrow_image.status == STARTED and t >= frameRemains:
                arrow_image.setAutoDraw(False)
                outlet.push_sample([condition])
                time.sleep(0.0001)

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sound_1.stop()  # ensure sound has stopped at end of routine
        routineTimer.reset()
        thisExp.nextEntry()

    # save data for this loop
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(thisExp.dataFileName + '.csv')
    #thisExp.saveAsPickle(thisExp.dataFileName)
    logging.flush()