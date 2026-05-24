#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.1.3),
    on Май 24, 2026, at 21:10
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.1.3'
expName = 'MentalRotationFinal'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': '',
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [2560, 1440]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\root\\Desktop\\dataserver\\MentalRotation_scenes\\MentalRotationFinal.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    # store pilot mode in data file
    thisExp.addData('piloting', PILOTING, priority=priority.LOW)
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('exp')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Hello" ---
    helloText = visual.TextStim(win=win, name='helloText',
        text='Дорогой испытуемый! \n\nМы изучаем особенности пространственного мышления и хотим выяснить, как люди представляют людей и объекты под разными углами. В данном эксперименте вам предстоит увидеть ряд изображений и после каждого ответить на поставленные вопросы. \nПеред началом вы увидите подробную инструкцию и пример задачи. \n\nЧтобы продолжить, нажмите ПРОБЕЛ.',
        font='Arial',
        units='height', pos=[0, 0], draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    helloKey = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "InstructionMR" ---
    InstMR_text = visual.TextStim(win=win, name='InstMR_text',
        text='Вы увидите ряд изображений, на которых человек сидит за столом. Перед человеком в центре стола расположен прямоугольный планшет, и вокруг планшета расположены 4 точки справа, слева, спереди и сзади.\n\nПри показе изображения одна из точек будет загораться. Под изображением вам также будет схематично представлен пример зажигания точек.\n\nВашей задачей будет определить как можно быстрее, СОВПАДАЕТ ЛИ ситуация на изображении с представленным примером.\n\nЕсли изображение и пример РАЗЛИЧАЮТСЯ, нажмите клавишу "<=”. Если они ОДИНАКОВЫЕ, нажмите клавишу “=>”.\n\nДля продолжения нажмите ПРОБЕЛ.',
        font='Arial',
        pos=(0, -0.25), draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    InstMR_keyresp = keyboard.Keyboard(deviceName='defaultKeyboard')
    InstMR_image = visual.ImageStim(
        win=win,
        name='InstMR_image', units='height', 
        image='rot60drwhoL.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.2), draggable=False, size=(0.5, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    InstMR_stimulus = visual.ImageStim(
        win=win,
        name='InstMR_stimulus', units='height', 
        image='stimuliLeft.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.08, 0.03),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "InstructionQnA" ---
    InstQnA_text = visual.TextStim(win=win, name='InstQnA_text',
        text='После ответа на изображения вам нужно оценить, как вы решали задачу. В основном есть 2 типа решения задач: либо через мысленное "поворачивание объектов" до тех пор, пока не получится произвести сравнение, либо через "представление чужой точки зрения" и того, слева или справа по отношению к смотрящему находится зажженая точка.\n\nЕсли в задаче до вопроса вы определили сходство или различие, мысленно поворачивая объекты на столе до нужного угла, нажмите клавишу "<=”.\nЕсли вы определили сходство или различие, представляя себя на чужом месте, нажмите клавишу "=>”. \nЕсли ни один из вариантов не кажется правильным, нажмите клавишу "пробел".\n\nДалее вы потренируетесь на нескольких примерах. Если вы ознакомились с инструкцией, нажмите ПРОБЕЛ.\n',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    InstQnA_keyresp = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "InstTest" ---
    InstTest_text = visual.TextStim(win=win, name='InstTest_text',
        text='Перед основной частью эксперимента вы потренируетесь на 4 задачах. Результаты этих задач не будут учитываться.\nВам понадобятся клавиши: "<=", "=>", "пробел".\n\nНе торопитесь, убедитесь, что вы полностью понимаете, что вам нужно делать. Если у вас возникают вопросы, задавайте их экспериментатору.\n\nЕсли готовы приступить, нажмите ПРОБЕЛ.',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    InstTest_keyresp = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "TestTrialMR" ---
    TestTrialMR_keyresp = keyboard.Keyboard(deviceName='defaultKeyboard')
    TestTrialMR_stimulus = visual.ImageStim(
        win=win,
        name='TestTrialMR_stimulus', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.27), draggable=False, size=(0.08, 0.03),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    TestTrialMR_image = visual.ImageStim(
        win=win,
        name='TestTrialMR_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.7, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    TestTrialMR_text = visual.TextStim(win=win, name='TestTrialMR_text',
        text="нажмите '<=' для ДРУГОЕ         нажмите '=>' для ТО ЖЕ",
        font='Arial',
        pos=(0, -0.4), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blank" ---
    polygon_centr = visual.ShapeStim(
        win=win, name='polygon_centr', vertices='cross',
        size=(0.1, 0.1),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "TestTrialQnA" ---
    TestTrialQnA_text = visual.TextStim(win=win, name='TestTrialQnA_text',
        text='Как вы решали?\n\n\n<= поворачивая объекты                представляя точку зрения=> ',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    TestTrialQnA_Ans = keyboard.Keyboard(deviceName='defaultKeyboard')
    TestTrialQnA_text2 = visual.TextStim(win=win, name='TestTrialQnA_text2',
        text='другое\n||\nv',
        font='Open Sans',
        pos=(0, -0.2), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "blank" ---
    polygon_centr = visual.ShapeStim(
        win=win, name='polygon_centr', vertices='cross',
        size=(0.1, 0.1),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "InstBegin" ---
    InstBegin_text = visual.TextStim(win=win, name='InstBegin_text',
        text='Сейчас начнется основная часть эксперимента.\nБудьте внимательны, не отвлекайтесь.\n\nЧтобы начать, нажмите ПРОБЕЛ.',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    InstBegin_keyresp = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "TrialSD" ---
    TrialSD_keyresp = keyboard.Keyboard(deviceName='defaultKeyboard')
    TrialSD_stimulus = visual.ImageStim(
        win=win,
        name='TrialSD_stimulus', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.27), draggable=False, size=(0.08, 0.03),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    TrialSD_image = visual.ImageStim(
        win=win,
        name='TrialSD_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.7, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    TrialSD_text = visual.TextStim(win=win, name='TrialSD_text',
        text="нажмите '<=' для ДРУГОЕ         нажмите '=>' для ТО ЖЕ",
        font='Arial',
        pos=(0, -0.4), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blank" ---
    polygon_centr = visual.ShapeStim(
        win=win, name='polygon_centr', vertices='cross',
        size=(0.1, 0.1),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "TrialQnA" ---
    TrialQnA_text = visual.TextStim(win=win, name='TrialQnA_text',
        text='Как вы решали?\n\n\n<= поворачивая объекты                представляя точку зрения=> ',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    TrialQnA_Ans = keyboard.Keyboard(deviceName='defaultKeyboard')
    TrialQnA_text2 = visual.TextStim(win=win, name='TrialQnA_text2',
        text='другое\n||\nv',
        font='Open Sans',
        pos=(0, -0.2), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "blank" ---
    polygon_centr = visual.ShapeStim(
        win=win, name='polygon_centr', vertices='cross',
        size=(0.1, 0.1),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "Goodbye" ---
    text_Ending = visual.TextStim(win=win, name='text_Ending',
        text='Спасибо за участие в эксперименте!\nОбратитесь к экспериментатору для дальнейших инструкций.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.08, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_Ending = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Hello" ---
    # create an object to store info about Routine Hello
    Hello = data.Routine(
        name='Hello',
        components=[helloText, helloKey],
    )
    Hello.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for helloKey
    helloKey.keys = []
    helloKey.rt = []
    _helloKey_allKeys = []
    # store start times for Hello
    Hello.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Hello.tStart = globalClock.getTime(format='float')
    Hello.status = STARTED
    thisExp.addData('Hello.started', Hello.tStart)
    Hello.maxDuration = None
    # keep track of which components have finished
    HelloComponents = Hello.components
    for thisComponent in Hello.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Hello" ---
    thisExp.currentRoutine = Hello
    Hello.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *helloText* updates
        
        # if helloText is starting this frame...
        if helloText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            helloText.frameNStart = frameN  # exact frame index
            helloText.tStart = t  # local t and not account for scr refresh
            helloText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(helloText, 'tStartRefresh')  # time at next scr refresh
            # update status
            helloText.status = STARTED
            helloText.setAutoDraw(True)
        
        # if helloText is active this frame...
        if helloText.status == STARTED:
            # update params
            pass
        
        # *helloKey* updates
        waitOnFlip = False
        
        # if helloKey is starting this frame...
        if helloKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            helloKey.frameNStart = frameN  # exact frame index
            helloKey.tStart = t  # local t and not account for scr refresh
            helloKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(helloKey, 'tStartRefresh')  # time at next scr refresh
            # update status
            helloKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(helloKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(helloKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if helloKey.status == STARTED and not waitOnFlip:
            theseKeys = helloKey.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _helloKey_allKeys.extend(theseKeys)
            if len(_helloKey_allKeys):
                helloKey.keys = _helloKey_allKeys[-1].name  # just the last key pressed
                helloKey.rt = _helloKey_allKeys[-1].rt
                helloKey.duration = _helloKey_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Hello,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            Hello.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if Hello.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in Hello.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Hello" ---
    for thisComponent in Hello.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Hello
    Hello.tStop = globalClock.getTime(format='float')
    Hello.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Hello.stopped', Hello.tStop)
    thisExp.nextEntry()
    # the Routine "Hello" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "InstructionMR" ---
    # create an object to store info about Routine InstructionMR
    InstructionMR = data.Routine(
        name='InstructionMR',
        components=[InstMR_text, InstMR_keyresp, InstMR_image, InstMR_stimulus],
    )
    InstructionMR.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for InstMR_keyresp
    InstMR_keyresp.keys = []
    InstMR_keyresp.rt = []
    _InstMR_keyresp_allKeys = []
    # store start times for InstructionMR
    InstructionMR.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    InstructionMR.tStart = globalClock.getTime(format='float')
    InstructionMR.status = STARTED
    thisExp.addData('InstructionMR.started', InstructionMR.tStart)
    InstructionMR.maxDuration = None
    # keep track of which components have finished
    InstructionMRComponents = InstructionMR.components
    for thisComponent in InstructionMR.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "InstructionMR" ---
    thisExp.currentRoutine = InstructionMR
    InstructionMR.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstMR_text* updates
        
        # if InstMR_text is starting this frame...
        if InstMR_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstMR_text.frameNStart = frameN  # exact frame index
            InstMR_text.tStart = t  # local t and not account for scr refresh
            InstMR_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstMR_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            InstMR_text.status = STARTED
            InstMR_text.setAutoDraw(True)
        
        # if InstMR_text is active this frame...
        if InstMR_text.status == STARTED:
            # update params
            pass
        
        # *InstMR_keyresp* updates
        waitOnFlip = False
        
        # if InstMR_keyresp is starting this frame...
        if InstMR_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstMR_keyresp.frameNStart = frameN  # exact frame index
            InstMR_keyresp.tStart = t  # local t and not account for scr refresh
            InstMR_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstMR_keyresp, 'tStartRefresh')  # time at next scr refresh
            # update status
            InstMR_keyresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(InstMR_keyresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(InstMR_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if InstMR_keyresp.status == STARTED and not waitOnFlip:
            theseKeys = InstMR_keyresp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _InstMR_keyresp_allKeys.extend(theseKeys)
            if len(_InstMR_keyresp_allKeys):
                InstMR_keyresp.keys = _InstMR_keyresp_allKeys[-1].name  # just the last key pressed
                InstMR_keyresp.rt = _InstMR_keyresp_allKeys[-1].rt
                InstMR_keyresp.duration = _InstMR_keyresp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *InstMR_image* updates
        
        # if InstMR_image is starting this frame...
        if InstMR_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstMR_image.frameNStart = frameN  # exact frame index
            InstMR_image.tStart = t  # local t and not account for scr refresh
            InstMR_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstMR_image, 'tStartRefresh')  # time at next scr refresh
            # update status
            InstMR_image.status = STARTED
            InstMR_image.setAutoDraw(True)
        
        # if InstMR_image is active this frame...
        if InstMR_image.status == STARTED:
            # update params
            pass
        
        # *InstMR_stimulus* updates
        
        # if InstMR_stimulus is starting this frame...
        if InstMR_stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstMR_stimulus.frameNStart = frameN  # exact frame index
            InstMR_stimulus.tStart = t  # local t and not account for scr refresh
            InstMR_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstMR_stimulus, 'tStartRefresh')  # time at next scr refresh
            # update status
            InstMR_stimulus.status = STARTED
            InstMR_stimulus.setAutoDraw(True)
        
        # if InstMR_stimulus is active this frame...
        if InstMR_stimulus.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=InstructionMR,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            InstructionMR.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if InstructionMR.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in InstructionMR.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "InstructionMR" ---
    for thisComponent in InstructionMR.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for InstructionMR
    InstructionMR.tStop = globalClock.getTime(format='float')
    InstructionMR.tStopRefresh = tThisFlipGlobal
    thisExp.addData('InstructionMR.stopped', InstructionMR.tStop)
    # check responses
    if InstMR_keyresp.keys in ['', [], None]:  # No response was made
        InstMR_keyresp.keys = None
    thisExp.addData('InstMR_keyresp.keys',InstMR_keyresp.keys)
    if InstMR_keyresp.keys != None:  # we had a response
        thisExp.addData('InstMR_keyresp.rt', InstMR_keyresp.rt)
        thisExp.addData('InstMR_keyresp.duration', InstMR_keyresp.duration)
    thisExp.nextEntry()
    # the Routine "InstructionMR" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "InstructionQnA" ---
    # create an object to store info about Routine InstructionQnA
    InstructionQnA = data.Routine(
        name='InstructionQnA',
        components=[InstQnA_text, InstQnA_keyresp],
    )
    InstructionQnA.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for InstQnA_keyresp
    InstQnA_keyresp.keys = []
    InstQnA_keyresp.rt = []
    _InstQnA_keyresp_allKeys = []
    # store start times for InstructionQnA
    InstructionQnA.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    InstructionQnA.tStart = globalClock.getTime(format='float')
    InstructionQnA.status = STARTED
    thisExp.addData('InstructionQnA.started', InstructionQnA.tStart)
    InstructionQnA.maxDuration = None
    # keep track of which components have finished
    InstructionQnAComponents = InstructionQnA.components
    for thisComponent in InstructionQnA.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "InstructionQnA" ---
    thisExp.currentRoutine = InstructionQnA
    InstructionQnA.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstQnA_text* updates
        
        # if InstQnA_text is starting this frame...
        if InstQnA_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstQnA_text.frameNStart = frameN  # exact frame index
            InstQnA_text.tStart = t  # local t and not account for scr refresh
            InstQnA_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstQnA_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            InstQnA_text.status = STARTED
            InstQnA_text.setAutoDraw(True)
        
        # if InstQnA_text is active this frame...
        if InstQnA_text.status == STARTED:
            # update params
            pass
        
        # *InstQnA_keyresp* updates
        waitOnFlip = False
        
        # if InstQnA_keyresp is starting this frame...
        if InstQnA_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstQnA_keyresp.frameNStart = frameN  # exact frame index
            InstQnA_keyresp.tStart = t  # local t and not account for scr refresh
            InstQnA_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstQnA_keyresp, 'tStartRefresh')  # time at next scr refresh
            # update status
            InstQnA_keyresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(InstQnA_keyresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(InstQnA_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if InstQnA_keyresp.status == STARTED and not waitOnFlip:
            theseKeys = InstQnA_keyresp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _InstQnA_keyresp_allKeys.extend(theseKeys)
            if len(_InstQnA_keyresp_allKeys):
                InstQnA_keyresp.keys = _InstQnA_keyresp_allKeys[-1].name  # just the last key pressed
                InstQnA_keyresp.rt = _InstQnA_keyresp_allKeys[-1].rt
                InstQnA_keyresp.duration = _InstQnA_keyresp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=InstructionQnA,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            InstructionQnA.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if InstructionQnA.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in InstructionQnA.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "InstructionQnA" ---
    for thisComponent in InstructionQnA.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for InstructionQnA
    InstructionQnA.tStop = globalClock.getTime(format='float')
    InstructionQnA.tStopRefresh = tThisFlipGlobal
    thisExp.addData('InstructionQnA.stopped', InstructionQnA.tStop)
    # check responses
    if InstQnA_keyresp.keys in ['', [], None]:  # No response was made
        InstQnA_keyresp.keys = None
    thisExp.addData('InstQnA_keyresp.keys',InstQnA_keyresp.keys)
    if InstQnA_keyresp.keys != None:  # we had a response
        thisExp.addData('InstQnA_keyresp.rt', InstQnA_keyresp.rt)
        thisExp.addData('InstQnA_keyresp.duration', InstQnA_keyresp.duration)
    thisExp.nextEntry()
    # the Routine "InstructionQnA" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "InstTest" ---
    # create an object to store info about Routine InstTest
    InstTest = data.Routine(
        name='InstTest',
        components=[InstTest_text, InstTest_keyresp],
    )
    InstTest.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for InstTest_keyresp
    InstTest_keyresp.keys = []
    InstTest_keyresp.rt = []
    _InstTest_keyresp_allKeys = []
    # store start times for InstTest
    InstTest.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    InstTest.tStart = globalClock.getTime(format='float')
    InstTest.status = STARTED
    thisExp.addData('InstTest.started', InstTest.tStart)
    InstTest.maxDuration = None
    # keep track of which components have finished
    InstTestComponents = InstTest.components
    for thisComponent in InstTest.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "InstTest" ---
    thisExp.currentRoutine = InstTest
    InstTest.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstTest_text* updates
        
        # if InstTest_text is starting this frame...
        if InstTest_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstTest_text.frameNStart = frameN  # exact frame index
            InstTest_text.tStart = t  # local t and not account for scr refresh
            InstTest_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstTest_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            InstTest_text.status = STARTED
            InstTest_text.setAutoDraw(True)
        
        # if InstTest_text is active this frame...
        if InstTest_text.status == STARTED:
            # update params
            pass
        
        # *InstTest_keyresp* updates
        waitOnFlip = False
        
        # if InstTest_keyresp is starting this frame...
        if InstTest_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstTest_keyresp.frameNStart = frameN  # exact frame index
            InstTest_keyresp.tStart = t  # local t and not account for scr refresh
            InstTest_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstTest_keyresp, 'tStartRefresh')  # time at next scr refresh
            # update status
            InstTest_keyresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(InstTest_keyresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(InstTest_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if InstTest_keyresp.status == STARTED and not waitOnFlip:
            theseKeys = InstTest_keyresp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _InstTest_keyresp_allKeys.extend(theseKeys)
            if len(_InstTest_keyresp_allKeys):
                InstTest_keyresp.keys = _InstTest_keyresp_allKeys[-1].name  # just the last key pressed
                InstTest_keyresp.rt = _InstTest_keyresp_allKeys[-1].rt
                InstTest_keyresp.duration = _InstTest_keyresp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=InstTest,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            InstTest.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if InstTest.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in InstTest.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "InstTest" ---
    for thisComponent in InstTest.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for InstTest
    InstTest.tStop = globalClock.getTime(format='float')
    InstTest.tStopRefresh = tThisFlipGlobal
    thisExp.addData('InstTest.stopped', InstTest.tStop)
    # check responses
    if InstTest_keyresp.keys in ['', [], None]:  # No response was made
        InstTest_keyresp.keys = None
    thisExp.addData('InstTest_keyresp.keys',InstTest_keyresp.keys)
    if InstTest_keyresp.keys != None:  # we had a response
        thisExp.addData('InstTest_keyresp.rt', InstTest_keyresp.rt)
        thisExp.addData('InstTest_keyresp.duration', InstTest_keyresp.duration)
    thisExp.nextEntry()
    # the Routine "InstTest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    testTrials = data.TrialHandler2(
        name='testTrials',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(
        'condition_file_2.xlsx', 
        selection='12:16'
    )
    , 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(testTrials)  # add the loop to the experiment
    thisTestTrial = testTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTestTrial.rgb)
    if thisTestTrial != None:
        for paramName in thisTestTrial:
            globals()[paramName] = thisTestTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTestTrial in testTrials:
        testTrials.status = STARTED
        if hasattr(thisTestTrial, 'status'):
            thisTestTrial.status = STARTED
        currentLoop = testTrials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTestTrial.rgb)
        if thisTestTrial != None:
            for paramName in thisTestTrial:
                globals()[paramName] = thisTestTrial[paramName]
        
        # --- Prepare to start Routine "TestTrialMR" ---
        # create an object to store info about Routine TestTrialMR
        TestTrialMR = data.Routine(
            name='TestTrialMR',
            components=[TestTrialMR_keyresp, TestTrialMR_stimulus, TestTrialMR_image, TestTrialMR_text],
        )
        TestTrialMR.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for TestTrialMR_keyresp
        TestTrialMR_keyresp.keys = []
        TestTrialMR_keyresp.rt = []
        _TestTrialMR_keyresp_allKeys = []
        TestTrialMR_stimulus.setImage(stimulifile)
        TestTrialMR_image.setImage(imagefile)
        # store start times for TestTrialMR
        TestTrialMR.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        TestTrialMR.tStart = globalClock.getTime(format='float')
        TestTrialMR.status = STARTED
        thisExp.addData('TestTrialMR.started', TestTrialMR.tStart)
        TestTrialMR.maxDuration = None
        # keep track of which components have finished
        TestTrialMRComponents = TestTrialMR.components
        for thisComponent in TestTrialMR.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TestTrialMR" ---
        thisExp.currentRoutine = TestTrialMR
        TestTrialMR.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTestTrial, 'status') and thisTestTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *TestTrialMR_keyresp* updates
            waitOnFlip = False
            
            # if TestTrialMR_keyresp is starting this frame...
            if TestTrialMR_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TestTrialMR_keyresp.frameNStart = frameN  # exact frame index
                TestTrialMR_keyresp.tStart = t  # local t and not account for scr refresh
                TestTrialMR_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TestTrialMR_keyresp, 'tStartRefresh')  # time at next scr refresh
                # update status
                TestTrialMR_keyresp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(TestTrialMR_keyresp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(TestTrialMR_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if TestTrialMR_keyresp.status == STARTED and not waitOnFlip:
                theseKeys = TestTrialMR_keyresp.getKeys(keyList=['left','right'], ignoreKeys=["escape"], waitRelease=False)
                _TestTrialMR_keyresp_allKeys.extend(theseKeys)
                if len(_TestTrialMR_keyresp_allKeys):
                    TestTrialMR_keyresp.keys = _TestTrialMR_keyresp_allKeys[-1].name  # just the last key pressed
                    TestTrialMR_keyresp.rt = _TestTrialMR_keyresp_allKeys[-1].rt
                    TestTrialMR_keyresp.duration = _TestTrialMR_keyresp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *TestTrialMR_stimulus* updates
            
            # if TestTrialMR_stimulus is starting this frame...
            if TestTrialMR_stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TestTrialMR_stimulus.frameNStart = frameN  # exact frame index
                TestTrialMR_stimulus.tStart = t  # local t and not account for scr refresh
                TestTrialMR_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TestTrialMR_stimulus, 'tStartRefresh')  # time at next scr refresh
                # update status
                TestTrialMR_stimulus.status = STARTED
                TestTrialMR_stimulus.setAutoDraw(True)
            
            # if TestTrialMR_stimulus is active this frame...
            if TestTrialMR_stimulus.status == STARTED:
                # update params
                pass
            
            # *TestTrialMR_image* updates
            
            # if TestTrialMR_image is starting this frame...
            if TestTrialMR_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TestTrialMR_image.frameNStart = frameN  # exact frame index
                TestTrialMR_image.tStart = t  # local t and not account for scr refresh
                TestTrialMR_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TestTrialMR_image, 'tStartRefresh')  # time at next scr refresh
                # update status
                TestTrialMR_image.status = STARTED
                TestTrialMR_image.setAutoDraw(True)
            
            # if TestTrialMR_image is active this frame...
            if TestTrialMR_image.status == STARTED:
                # update params
                pass
            
            # *TestTrialMR_text* updates
            
            # if TestTrialMR_text is starting this frame...
            if TestTrialMR_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TestTrialMR_text.frameNStart = frameN  # exact frame index
                TestTrialMR_text.tStart = t  # local t and not account for scr refresh
                TestTrialMR_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TestTrialMR_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                TestTrialMR_text.status = STARTED
                TestTrialMR_text.setAutoDraw(True)
            
            # if TestTrialMR_text is active this frame...
            if TestTrialMR_text.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=TestTrialMR,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                TestTrialMR.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if TestTrialMR.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in TestTrialMR.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TestTrialMR" ---
        for thisComponent in TestTrialMR.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for TestTrialMR
        TestTrialMR.tStop = globalClock.getTime(format='float')
        TestTrialMR.tStopRefresh = tThisFlipGlobal
        thisExp.addData('TestTrialMR.stopped', TestTrialMR.tStop)
        # check responses
        if TestTrialMR_keyresp.keys in ['', [], None]:  # No response was made
            TestTrialMR_keyresp.keys = None
        testTrials.addData('TestTrialMR_keyresp.keys',TestTrialMR_keyresp.keys)
        if TestTrialMR_keyresp.keys != None:  # we had a response
            testTrials.addData('TestTrialMR_keyresp.rt', TestTrialMR_keyresp.rt)
            testTrials.addData('TestTrialMR_keyresp.duration', TestTrialMR_keyresp.duration)
        # the Routine "TestTrialMR" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank" ---
        # create an object to store info about Routine blank
        blank = data.Routine(
            name='blank',
            components=[polygon_centr],
        )
        blank.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for blank
        blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank.tStart = globalClock.getTime(format='float')
        blank.status = STARTED
        thisExp.addData('blank.started', blank.tStart)
        blank.maxDuration = None
        # keep track of which components have finished
        blankComponents = blank.components
        for thisComponent in blank.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank" ---
        thisExp.currentRoutine = blank
        blank.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisTestTrial, 'status') and thisTestTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_centr* updates
            
            # if polygon_centr is starting this frame...
            if polygon_centr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_centr.frameNStart = frameN  # exact frame index
                polygon_centr.tStart = t  # local t and not account for scr refresh
                polygon_centr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_centr, 'tStartRefresh')  # time at next scr refresh
                # update status
                polygon_centr.status = STARTED
                polygon_centr.setAutoDraw(True)
            
            # if polygon_centr is active this frame...
            if polygon_centr.status == STARTED:
                # update params
                pass
            
            # if polygon_centr is stopping this frame...
            if polygon_centr.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_centr.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_centr.tStop = t  # not accounting for scr refresh
                    polygon_centr.tStopRefresh = tThisFlipGlobal  # on global time
                    polygon_centr.frameNStop = frameN  # exact frame index
                    # update status
                    polygon_centr.status = FINISHED
                    polygon_centr.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=blank,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                blank.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if blank.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in blank.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank" ---
        for thisComponent in blank.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank
        blank.tStop = globalClock.getTime(format='float')
        blank.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blank.stopped', blank.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank.maxDurationReached:
            routineTimer.addTime(-blank.maxDuration)
        elif blank.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "TestTrialQnA" ---
        # create an object to store info about Routine TestTrialQnA
        TestTrialQnA = data.Routine(
            name='TestTrialQnA',
            components=[TestTrialQnA_text, TestTrialQnA_Ans, TestTrialQnA_text2],
        )
        TestTrialQnA.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for TestTrialQnA_Ans
        TestTrialQnA_Ans.keys = []
        TestTrialQnA_Ans.rt = []
        _TestTrialQnA_Ans_allKeys = []
        # store start times for TestTrialQnA
        TestTrialQnA.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        TestTrialQnA.tStart = globalClock.getTime(format='float')
        TestTrialQnA.status = STARTED
        thisExp.addData('TestTrialQnA.started', TestTrialQnA.tStart)
        TestTrialQnA.maxDuration = None
        # keep track of which components have finished
        TestTrialQnAComponents = TestTrialQnA.components
        for thisComponent in TestTrialQnA.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TestTrialQnA" ---
        thisExp.currentRoutine = TestTrialQnA
        TestTrialQnA.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTestTrial, 'status') and thisTestTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *TestTrialQnA_text* updates
            
            # if TestTrialQnA_text is starting this frame...
            if TestTrialQnA_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TestTrialQnA_text.frameNStart = frameN  # exact frame index
                TestTrialQnA_text.tStart = t  # local t and not account for scr refresh
                TestTrialQnA_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TestTrialQnA_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                TestTrialQnA_text.status = STARTED
                TestTrialQnA_text.setAutoDraw(True)
            
            # if TestTrialQnA_text is active this frame...
            if TestTrialQnA_text.status == STARTED:
                # update params
                pass
            
            # *TestTrialQnA_Ans* updates
            waitOnFlip = False
            
            # if TestTrialQnA_Ans is starting this frame...
            if TestTrialQnA_Ans.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TestTrialQnA_Ans.frameNStart = frameN  # exact frame index
                TestTrialQnA_Ans.tStart = t  # local t and not account for scr refresh
                TestTrialQnA_Ans.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TestTrialQnA_Ans, 'tStartRefresh')  # time at next scr refresh
                # update status
                TestTrialQnA_Ans.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(TestTrialQnA_Ans.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(TestTrialQnA_Ans.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if TestTrialQnA_Ans.status == STARTED and not waitOnFlip:
                theseKeys = TestTrialQnA_Ans.getKeys(keyList=['left','right','space'], ignoreKeys=["escape"], waitRelease=False)
                _TestTrialQnA_Ans_allKeys.extend(theseKeys)
                if len(_TestTrialQnA_Ans_allKeys):
                    TestTrialQnA_Ans.keys = _TestTrialQnA_Ans_allKeys[-1].name  # just the last key pressed
                    TestTrialQnA_Ans.rt = _TestTrialQnA_Ans_allKeys[-1].rt
                    TestTrialQnA_Ans.duration = _TestTrialQnA_Ans_allKeys[-1].duration
                    # was this correct?
                    if (TestTrialQnA_Ans.keys == str('')) or (TestTrialQnA_Ans.keys == ''):
                        TestTrialQnA_Ans.corr = 1
                    else:
                        TestTrialQnA_Ans.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *TestTrialQnA_text2* updates
            
            # if TestTrialQnA_text2 is starting this frame...
            if TestTrialQnA_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TestTrialQnA_text2.frameNStart = frameN  # exact frame index
                TestTrialQnA_text2.tStart = t  # local t and not account for scr refresh
                TestTrialQnA_text2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TestTrialQnA_text2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TestTrialQnA_text2.started')
                # update status
                TestTrialQnA_text2.status = STARTED
                TestTrialQnA_text2.setAutoDraw(True)
            
            # if TestTrialQnA_text2 is active this frame...
            if TestTrialQnA_text2.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=TestTrialQnA,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                TestTrialQnA.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if TestTrialQnA.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in TestTrialQnA.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TestTrialQnA" ---
        for thisComponent in TestTrialQnA.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for TestTrialQnA
        TestTrialQnA.tStop = globalClock.getTime(format='float')
        TestTrialQnA.tStopRefresh = tThisFlipGlobal
        thisExp.addData('TestTrialQnA.stopped', TestTrialQnA.tStop)
        # check responses
        if TestTrialQnA_Ans.keys in ['', [], None]:  # No response was made
            TestTrialQnA_Ans.keys = None
            # was no response the correct answer?!
            if str('').lower() == 'none':
               TestTrialQnA_Ans.corr = 1;  # correct non-response
            else:
               TestTrialQnA_Ans.corr = 0;  # failed to respond (incorrectly)
        # store data for testTrials (TrialHandler)
        testTrials.addData('TestTrialQnA_Ans.keys',TestTrialQnA_Ans.keys)
        testTrials.addData('TestTrialQnA_Ans.corr', TestTrialQnA_Ans.corr)
        if TestTrialQnA_Ans.keys != None:  # we had a response
            testTrials.addData('TestTrialQnA_Ans.rt', TestTrialQnA_Ans.rt)
            testTrials.addData('TestTrialQnA_Ans.duration', TestTrialQnA_Ans.duration)
        # the Routine "TestTrialQnA" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank" ---
        # create an object to store info about Routine blank
        blank = data.Routine(
            name='blank',
            components=[polygon_centr],
        )
        blank.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for blank
        blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank.tStart = globalClock.getTime(format='float')
        blank.status = STARTED
        thisExp.addData('blank.started', blank.tStart)
        blank.maxDuration = None
        # keep track of which components have finished
        blankComponents = blank.components
        for thisComponent in blank.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank" ---
        thisExp.currentRoutine = blank
        blank.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisTestTrial, 'status') and thisTestTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_centr* updates
            
            # if polygon_centr is starting this frame...
            if polygon_centr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_centr.frameNStart = frameN  # exact frame index
                polygon_centr.tStart = t  # local t and not account for scr refresh
                polygon_centr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_centr, 'tStartRefresh')  # time at next scr refresh
                # update status
                polygon_centr.status = STARTED
                polygon_centr.setAutoDraw(True)
            
            # if polygon_centr is active this frame...
            if polygon_centr.status == STARTED:
                # update params
                pass
            
            # if polygon_centr is stopping this frame...
            if polygon_centr.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_centr.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_centr.tStop = t  # not accounting for scr refresh
                    polygon_centr.tStopRefresh = tThisFlipGlobal  # on global time
                    polygon_centr.frameNStop = frameN  # exact frame index
                    # update status
                    polygon_centr.status = FINISHED
                    polygon_centr.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=blank,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                blank.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if blank.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in blank.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank" ---
        for thisComponent in blank.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank
        blank.tStop = globalClock.getTime(format='float')
        blank.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blank.stopped', blank.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank.maxDurationReached:
            routineTimer.addTime(-blank.maxDuration)
        elif blank.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        # mark thisTestTrial as finished
        if hasattr(thisTestTrial, 'status'):
            thisTestTrial.status = FINISHED
        # if awaiting a pause, pause now
        if testTrials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            testTrials.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'testTrials'
    testTrials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "InstBegin" ---
    # create an object to store info about Routine InstBegin
    InstBegin = data.Routine(
        name='InstBegin',
        components=[InstBegin_text, InstBegin_keyresp],
    )
    InstBegin.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for InstBegin_keyresp
    InstBegin_keyresp.keys = []
    InstBegin_keyresp.rt = []
    _InstBegin_keyresp_allKeys = []
    # store start times for InstBegin
    InstBegin.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    InstBegin.tStart = globalClock.getTime(format='float')
    InstBegin.status = STARTED
    thisExp.addData('InstBegin.started', InstBegin.tStart)
    InstBegin.maxDuration = None
    # keep track of which components have finished
    InstBeginComponents = InstBegin.components
    for thisComponent in InstBegin.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "InstBegin" ---
    thisExp.currentRoutine = InstBegin
    InstBegin.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstBegin_text* updates
        
        # if InstBegin_text is starting this frame...
        if InstBegin_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstBegin_text.frameNStart = frameN  # exact frame index
            InstBegin_text.tStart = t  # local t and not account for scr refresh
            InstBegin_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstBegin_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            InstBegin_text.status = STARTED
            InstBegin_text.setAutoDraw(True)
        
        # if InstBegin_text is active this frame...
        if InstBegin_text.status == STARTED:
            # update params
            pass
        
        # *InstBegin_keyresp* updates
        waitOnFlip = False
        
        # if InstBegin_keyresp is starting this frame...
        if InstBegin_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstBegin_keyresp.frameNStart = frameN  # exact frame index
            InstBegin_keyresp.tStart = t  # local t and not account for scr refresh
            InstBegin_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstBegin_keyresp, 'tStartRefresh')  # time at next scr refresh
            # update status
            InstBegin_keyresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(InstBegin_keyresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(InstBegin_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if InstBegin_keyresp.status == STARTED and not waitOnFlip:
            theseKeys = InstBegin_keyresp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _InstBegin_keyresp_allKeys.extend(theseKeys)
            if len(_InstBegin_keyresp_allKeys):
                InstBegin_keyresp.keys = _InstBegin_keyresp_allKeys[-1].name  # just the last key pressed
                InstBegin_keyresp.rt = _InstBegin_keyresp_allKeys[-1].rt
                InstBegin_keyresp.duration = _InstBegin_keyresp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=InstBegin,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            InstBegin.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if InstBegin.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in InstBegin.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "InstBegin" ---
    for thisComponent in InstBegin.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for InstBegin
    InstBegin.tStop = globalClock.getTime(format='float')
    InstBegin.tStopRefresh = tThisFlipGlobal
    thisExp.addData('InstBegin.stopped', InstBegin.tStop)
    # check responses
    if InstBegin_keyresp.keys in ['', [], None]:  # No response was made
        InstBegin_keyresp.keys = None
    thisExp.addData('InstBegin_keyresp.keys',InstBegin_keyresp.keys)
    if InstBegin_keyresp.keys != None:  # we had a response
        thisExp.addData('InstBegin_keyresp.rt', InstBegin_keyresp.rt)
        thisExp.addData('InstBegin_keyresp.duration', InstBegin_keyresp.duration)
    thisExp.nextEntry()
    # the Routine "InstBegin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    loopSD = data.TrialHandler2(
        name='loopSD',
        nReps=2, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('condition_file_2.xlsx'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(loopSD)  # add the loop to the experiment
    thisLoopSD = loopSD.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoopSD.rgb)
    if thisLoopSD != None:
        for paramName in thisLoopSD:
            globals()[paramName] = thisLoopSD[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLoopSD in loopSD:
        loopSD.status = STARTED
        if hasattr(thisLoopSD, 'status'):
            thisLoopSD.status = STARTED
        currentLoop = loopSD
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLoopSD.rgb)
        if thisLoopSD != None:
            for paramName in thisLoopSD:
                globals()[paramName] = thisLoopSD[paramName]
        
        # --- Prepare to start Routine "TrialSD" ---
        # create an object to store info about Routine TrialSD
        TrialSD = data.Routine(
            name='TrialSD',
            components=[TrialSD_keyresp, TrialSD_stimulus, TrialSD_image, TrialSD_text],
        )
        TrialSD.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for TrialSD_keyresp
        TrialSD_keyresp.keys = []
        TrialSD_keyresp.rt = []
        _TrialSD_keyresp_allKeys = []
        TrialSD_stimulus.setImage(stimulifile)
        TrialSD_image.setImage(imagefile)
        # store start times for TrialSD
        TrialSD.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        TrialSD.tStart = globalClock.getTime(format='float')
        TrialSD.status = STARTED
        thisExp.addData('TrialSD.started', TrialSD.tStart)
        TrialSD.maxDuration = None
        # keep track of which components have finished
        TrialSDComponents = TrialSD.components
        for thisComponent in TrialSD.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TrialSD" ---
        thisExp.currentRoutine = TrialSD
        TrialSD.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisLoopSD, 'status') and thisLoopSD.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *TrialSD_keyresp* updates
            waitOnFlip = False
            
            # if TrialSD_keyresp is starting this frame...
            if TrialSD_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrialSD_keyresp.frameNStart = frameN  # exact frame index
                TrialSD_keyresp.tStart = t  # local t and not account for scr refresh
                TrialSD_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrialSD_keyresp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TrialSD_keyresp.started')
                # update status
                TrialSD_keyresp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(TrialSD_keyresp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(TrialSD_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if TrialSD_keyresp.status == STARTED and not waitOnFlip:
                theseKeys = TrialSD_keyresp.getKeys(keyList=['left','right'], ignoreKeys=["escape"], waitRelease=False)
                _TrialSD_keyresp_allKeys.extend(theseKeys)
                if len(_TrialSD_keyresp_allKeys):
                    TrialSD_keyresp.keys = _TrialSD_keyresp_allKeys[-1].name  # just the last key pressed
                    TrialSD_keyresp.rt = _TrialSD_keyresp_allKeys[-1].rt
                    TrialSD_keyresp.duration = _TrialSD_keyresp_allKeys[-1].duration
                    # was this correct?
                    if (TrialSD_keyresp.keys == str(corrAns)) or (TrialSD_keyresp.keys == corrAns):
                        TrialSD_keyresp.corr = 1
                    else:
                        TrialSD_keyresp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *TrialSD_stimulus* updates
            
            # if TrialSD_stimulus is starting this frame...
            if TrialSD_stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrialSD_stimulus.frameNStart = frameN  # exact frame index
                TrialSD_stimulus.tStart = t  # local t and not account for scr refresh
                TrialSD_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrialSD_stimulus, 'tStartRefresh')  # time at next scr refresh
                # update status
                TrialSD_stimulus.status = STARTED
                TrialSD_stimulus.setAutoDraw(True)
            
            # if TrialSD_stimulus is active this frame...
            if TrialSD_stimulus.status == STARTED:
                # update params
                pass
            
            # *TrialSD_image* updates
            
            # if TrialSD_image is starting this frame...
            if TrialSD_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrialSD_image.frameNStart = frameN  # exact frame index
                TrialSD_image.tStart = t  # local t and not account for scr refresh
                TrialSD_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrialSD_image, 'tStartRefresh')  # time at next scr refresh
                # update status
                TrialSD_image.status = STARTED
                TrialSD_image.setAutoDraw(True)
            
            # if TrialSD_image is active this frame...
            if TrialSD_image.status == STARTED:
                # update params
                pass
            
            # *TrialSD_text* updates
            
            # if TrialSD_text is starting this frame...
            if TrialSD_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrialSD_text.frameNStart = frameN  # exact frame index
                TrialSD_text.tStart = t  # local t and not account for scr refresh
                TrialSD_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrialSD_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                TrialSD_text.status = STARTED
                TrialSD_text.setAutoDraw(True)
            
            # if TrialSD_text is active this frame...
            if TrialSD_text.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=TrialSD,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                TrialSD.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if TrialSD.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in TrialSD.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TrialSD" ---
        for thisComponent in TrialSD.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for TrialSD
        TrialSD.tStop = globalClock.getTime(format='float')
        TrialSD.tStopRefresh = tThisFlipGlobal
        thisExp.addData('TrialSD.stopped', TrialSD.tStop)
        # check responses
        if TrialSD_keyresp.keys in ['', [], None]:  # No response was made
            TrialSD_keyresp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               TrialSD_keyresp.corr = 1;  # correct non-response
            else:
               TrialSD_keyresp.corr = 0;  # failed to respond (incorrectly)
        # store data for loopSD (TrialHandler)
        loopSD.addData('TrialSD_keyresp.keys',TrialSD_keyresp.keys)
        loopSD.addData('TrialSD_keyresp.corr', TrialSD_keyresp.corr)
        if TrialSD_keyresp.keys != None:  # we had a response
            loopSD.addData('TrialSD_keyresp.rt', TrialSD_keyresp.rt)
            loopSD.addData('TrialSD_keyresp.duration', TrialSD_keyresp.duration)
        # the Routine "TrialSD" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank" ---
        # create an object to store info about Routine blank
        blank = data.Routine(
            name='blank',
            components=[polygon_centr],
        )
        blank.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for blank
        blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank.tStart = globalClock.getTime(format='float')
        blank.status = STARTED
        thisExp.addData('blank.started', blank.tStart)
        blank.maxDuration = None
        # keep track of which components have finished
        blankComponents = blank.components
        for thisComponent in blank.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank" ---
        thisExp.currentRoutine = blank
        blank.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisLoopSD, 'status') and thisLoopSD.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_centr* updates
            
            # if polygon_centr is starting this frame...
            if polygon_centr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_centr.frameNStart = frameN  # exact frame index
                polygon_centr.tStart = t  # local t and not account for scr refresh
                polygon_centr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_centr, 'tStartRefresh')  # time at next scr refresh
                # update status
                polygon_centr.status = STARTED
                polygon_centr.setAutoDraw(True)
            
            # if polygon_centr is active this frame...
            if polygon_centr.status == STARTED:
                # update params
                pass
            
            # if polygon_centr is stopping this frame...
            if polygon_centr.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_centr.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_centr.tStop = t  # not accounting for scr refresh
                    polygon_centr.tStopRefresh = tThisFlipGlobal  # on global time
                    polygon_centr.frameNStop = frameN  # exact frame index
                    # update status
                    polygon_centr.status = FINISHED
                    polygon_centr.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=blank,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                blank.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if blank.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in blank.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank" ---
        for thisComponent in blank.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank
        blank.tStop = globalClock.getTime(format='float')
        blank.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blank.stopped', blank.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank.maxDurationReached:
            routineTimer.addTime(-blank.maxDuration)
        elif blank.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "TrialQnA" ---
        # create an object to store info about Routine TrialQnA
        TrialQnA = data.Routine(
            name='TrialQnA',
            components=[TrialQnA_text, TrialQnA_Ans, TrialQnA_text2],
        )
        TrialQnA.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for TrialQnA_Ans
        TrialQnA_Ans.keys = []
        TrialQnA_Ans.rt = []
        _TrialQnA_Ans_allKeys = []
        # store start times for TrialQnA
        TrialQnA.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        TrialQnA.tStart = globalClock.getTime(format='float')
        TrialQnA.status = STARTED
        thisExp.addData('TrialQnA.started', TrialQnA.tStart)
        TrialQnA.maxDuration = None
        # keep track of which components have finished
        TrialQnAComponents = TrialQnA.components
        for thisComponent in TrialQnA.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TrialQnA" ---
        thisExp.currentRoutine = TrialQnA
        TrialQnA.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisLoopSD, 'status') and thisLoopSD.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *TrialQnA_text* updates
            
            # if TrialQnA_text is starting this frame...
            if TrialQnA_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrialQnA_text.frameNStart = frameN  # exact frame index
                TrialQnA_text.tStart = t  # local t and not account for scr refresh
                TrialQnA_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrialQnA_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                TrialQnA_text.status = STARTED
                TrialQnA_text.setAutoDraw(True)
            
            # if TrialQnA_text is active this frame...
            if TrialQnA_text.status == STARTED:
                # update params
                pass
            
            # *TrialQnA_Ans* updates
            waitOnFlip = False
            
            # if TrialQnA_Ans is starting this frame...
            if TrialQnA_Ans.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrialQnA_Ans.frameNStart = frameN  # exact frame index
                TrialQnA_Ans.tStart = t  # local t and not account for scr refresh
                TrialQnA_Ans.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrialQnA_Ans, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TrialQnA_Ans.started')
                # update status
                TrialQnA_Ans.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(TrialQnA_Ans.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(TrialQnA_Ans.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if TrialQnA_Ans.status == STARTED and not waitOnFlip:
                theseKeys = TrialQnA_Ans.getKeys(keyList=['left','right','space'], ignoreKeys=["escape"], waitRelease=False)
                _TrialQnA_Ans_allKeys.extend(theseKeys)
                if len(_TrialQnA_Ans_allKeys):
                    TrialQnA_Ans.keys = _TrialQnA_Ans_allKeys[-1].name  # just the last key pressed
                    TrialQnA_Ans.rt = _TrialQnA_Ans_allKeys[-1].rt
                    TrialQnA_Ans.duration = _TrialQnA_Ans_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *TrialQnA_text2* updates
            
            # if TrialQnA_text2 is starting this frame...
            if TrialQnA_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrialQnA_text2.frameNStart = frameN  # exact frame index
                TrialQnA_text2.tStart = t  # local t and not account for scr refresh
                TrialQnA_text2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrialQnA_text2, 'tStartRefresh')  # time at next scr refresh
                # update status
                TrialQnA_text2.status = STARTED
                TrialQnA_text2.setAutoDraw(True)
            
            # if TrialQnA_text2 is active this frame...
            if TrialQnA_text2.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=TrialQnA,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                TrialQnA.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if TrialQnA.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in TrialQnA.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TrialQnA" ---
        for thisComponent in TrialQnA.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for TrialQnA
        TrialQnA.tStop = globalClock.getTime(format='float')
        TrialQnA.tStopRefresh = tThisFlipGlobal
        thisExp.addData('TrialQnA.stopped', TrialQnA.tStop)
        # check responses
        if TrialQnA_Ans.keys in ['', [], None]:  # No response was made
            TrialQnA_Ans.keys = None
        loopSD.addData('TrialQnA_Ans.keys',TrialQnA_Ans.keys)
        if TrialQnA_Ans.keys != None:  # we had a response
            loopSD.addData('TrialQnA_Ans.rt', TrialQnA_Ans.rt)
            loopSD.addData('TrialQnA_Ans.duration', TrialQnA_Ans.duration)
        # the Routine "TrialQnA" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank" ---
        # create an object to store info about Routine blank
        blank = data.Routine(
            name='blank',
            components=[polygon_centr],
        )
        blank.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for blank
        blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank.tStart = globalClock.getTime(format='float')
        blank.status = STARTED
        thisExp.addData('blank.started', blank.tStart)
        blank.maxDuration = None
        # keep track of which components have finished
        blankComponents = blank.components
        for thisComponent in blank.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank" ---
        thisExp.currentRoutine = blank
        blank.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisLoopSD, 'status') and thisLoopSD.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_centr* updates
            
            # if polygon_centr is starting this frame...
            if polygon_centr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_centr.frameNStart = frameN  # exact frame index
                polygon_centr.tStart = t  # local t and not account for scr refresh
                polygon_centr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_centr, 'tStartRefresh')  # time at next scr refresh
                # update status
                polygon_centr.status = STARTED
                polygon_centr.setAutoDraw(True)
            
            # if polygon_centr is active this frame...
            if polygon_centr.status == STARTED:
                # update params
                pass
            
            # if polygon_centr is stopping this frame...
            if polygon_centr.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_centr.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_centr.tStop = t  # not accounting for scr refresh
                    polygon_centr.tStopRefresh = tThisFlipGlobal  # on global time
                    polygon_centr.frameNStop = frameN  # exact frame index
                    # update status
                    polygon_centr.status = FINISHED
                    polygon_centr.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=blank,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                blank.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if blank.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in blank.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank" ---
        for thisComponent in blank.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank
        blank.tStop = globalClock.getTime(format='float')
        blank.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blank.stopped', blank.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank.maxDurationReached:
            routineTimer.addTime(-blank.maxDuration)
        elif blank.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        # mark thisLoopSD as finished
        if hasattr(thisLoopSD, 'status'):
            thisLoopSD.status = FINISHED
        # if awaiting a pause, pause now
        if loopSD.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            loopSD.status = STARTED
        thisExp.nextEntry()
        
    # completed 2 repeats of 'loopSD'
    loopSD.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "Goodbye" ---
    # create an object to store info about Routine Goodbye
    Goodbye = data.Routine(
        name='Goodbye',
        components=[text_Ending, key_resp_Ending],
    )
    Goodbye.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_Ending
    key_resp_Ending.keys = []
    key_resp_Ending.rt = []
    _key_resp_Ending_allKeys = []
    # store start times for Goodbye
    Goodbye.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Goodbye.tStart = globalClock.getTime(format='float')
    Goodbye.status = STARTED
    thisExp.addData('Goodbye.started', Goodbye.tStart)
    Goodbye.maxDuration = None
    # keep track of which components have finished
    GoodbyeComponents = Goodbye.components
    for thisComponent in Goodbye.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Goodbye" ---
    thisExp.currentRoutine = Goodbye
    Goodbye.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_Ending* updates
        
        # if text_Ending is starting this frame...
        if text_Ending.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Ending.frameNStart = frameN  # exact frame index
            text_Ending.tStart = t  # local t and not account for scr refresh
            text_Ending.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Ending, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_Ending.status = STARTED
            text_Ending.setAutoDraw(True)
        
        # if text_Ending is active this frame...
        if text_Ending.status == STARTED:
            # update params
            pass
        
        # *key_resp_Ending* updates
        waitOnFlip = False
        
        # if key_resp_Ending is starting this frame...
        if key_resp_Ending.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_Ending.frameNStart = frameN  # exact frame index
            key_resp_Ending.tStart = t  # local t and not account for scr refresh
            key_resp_Ending.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_Ending, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_Ending.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_Ending.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_Ending.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_Ending.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_Ending.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_Ending_allKeys.extend(theseKeys)
            if len(_key_resp_Ending_allKeys):
                key_resp_Ending.keys = _key_resp_Ending_allKeys[-1].name  # just the last key pressed
                key_resp_Ending.rt = _key_resp_Ending_allKeys[-1].rt
                key_resp_Ending.duration = _key_resp_Ending_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Goodbye,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            Goodbye.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if Goodbye.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in Goodbye.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Goodbye" ---
    for thisComponent in Goodbye.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Goodbye
    Goodbye.tStop = globalClock.getTime(format='float')
    Goodbye.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Goodbye.stopped', Goodbye.tStop)
    # check responses
    if key_resp_Ending.keys in ['', [], None]:  # No response was made
        key_resp_Ending.keys = None
    thisExp.addData('key_resp_Ending.keys',key_resp_Ending.keys)
    if key_resp_Ending.keys != None:  # we had a response
        thisExp.addData('key_resp_Ending.rt', key_resp_Ending.rt)
        thisExp.addData('key_resp_Ending.duration', key_resp_Ending.duration)
    thisExp.nextEntry()
    # the Routine "Goodbye" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    # stop any playback components
    if thisExp.currentRoutine is not None:
        for comp in thisExp.currentRoutine.getPlaybackComponents():
            comp.stop()
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
