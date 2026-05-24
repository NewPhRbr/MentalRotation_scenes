/**************************** 
 * Mentalrotationfinal *
 ****************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.1.0.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'MentalRotationFinal';  // from the Builder filename that created this script
let expInfo = {
  'participant': '',
  'session': '001',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function () { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(HelloRoutineBegin());
flowScheduler.add(HelloRoutineEachFrame());
flowScheduler.add(HelloRoutineEnd());
flowScheduler.add(InstructionMRRoutineBegin());
flowScheduler.add(InstructionMRRoutineEachFrame());
flowScheduler.add(InstructionMRRoutineEnd());
flowScheduler.add(InstructionQnARoutineBegin());
flowScheduler.add(InstructionQnARoutineEachFrame());
flowScheduler.add(InstructionQnARoutineEnd());
flowScheduler.add(InstTestRoutineBegin());
flowScheduler.add(InstTestRoutineEachFrame());
flowScheduler.add(InstTestRoutineEnd());
const testTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(testTrialsLoopBegin(testTrialsLoopScheduler));
flowScheduler.add(testTrialsLoopScheduler);
flowScheduler.add(testTrialsLoopEnd);





flowScheduler.add(InstBeginRoutineBegin());
flowScheduler.add(InstBeginRoutineEachFrame());
flowScheduler.add(InstBeginRoutineEnd());
const loopSDLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(loopSDLoopBegin(loopSDLoopScheduler));
flowScheduler.add(loopSDLoopScheduler);
flowScheduler.add(loopSDLoopEnd);





flowScheduler.add(GoodbyeRoutineBegin());
flowScheduler.add(GoodbyeRoutineEachFrame());
flowScheduler.add(GoodbyeRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    { 'name': 'rot60drwhoL.jpg', 'path': 'resources/rot60drwhoL' },
    { 'name': 'rot60drwhoR.jpg', 'path': 'resources/rot60drwhoR' },
    { 'name': 'rot110drwhoL.jpg', 'path': 'resources/rot110drwhoL' },
    { 'name': 'rot110drwhoR.jpg', 'path': 'resources/rot110drwhoR' },
    { 'name': 'rot160drwhoL.jpg', 'path': 'resources/rot160drwhoL' },
    { 'name': 'rot160drwhoR.jpg', 'path': 'resources/rot160drwhoR' },
    { 'name': 'rot200drwhoL.jpg', 'path': 'resources/rot200drwhoL' },
    { 'name': 'rot200drwhoR.jpg', 'path': 'resources/rot200drwhoR' },
    { 'name': 'rot250drwhoL.jpg', 'path': 'resources/rot250drwhoL' },
    { 'name': 'rot250drwhoR.jpg', 'path': 'resources/rot250drwhoR' },
    { 'name': 'rot300drwhoL.jpg', 'path': 'resources/rot300drwhoL' },
    { 'name': 'rot300drwhoR.jpg', 'path': 'resources/rot300drwhoR' },
    { 'name': 'stimuliLeft.png', 'path': 'resources/stimuliLeft' },
    { 'name': 'stimuliRight.png', 'path': 'resources/stimuliRight' },
    { 'name': 'default.png', 'path': 'resources/default.png' },
    { 'name': 'condition_file_1.xlsx', 'path': 'resources/condition_file_1.xlsx' },
    { 'name': 'condition_file_2.xlsx', 'path': 'resources/condition_file_2.xlsx' },
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2026.1.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);



  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var HelloClock;
var helloText;
var helloKey;
var InstructionMRClock;
var InstMR_text;
var InstMR_keyresp;
var InstMR_image;
var InstMR_stimulus;
var InstructionQnAClock;
var InstQnA_text;
var InstQnA_keyresp;
var InstTestClock;
var InstTest_text;
var InstTest_keyresp;
var TestTrialMRClock;
var TestTrialMR_keyresp;
var TestTrialMR_stimulus;
var TestTrialMR_image;
var TestTrialMR_text;
var blankClock;
var polygon_centr;
var TestTrialQnAClock;
var TestTrialQnA_text;
var TestTrialQnA_Ans;
var TestTrialQnA_text2;
var InstBeginClock;
var InstBegin_text;
var InstBegin_keyresp;
var TrialSDClock;
var TrialSD_keyresp;
var TrialSD_stimulus;
var TrialSD_image;
var TrialSD_text;
var TrialQnAClock;
var TrialQnA_text;
var TrialQnA_Ans;
var TrialQnA_text2;
var GoodbyeClock;
var text_Ending;
var key_resp_Ending;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Hello"
  HelloClock = new util.Clock();
  helloText = new visual.TextStim({
    win: psychoJS.window,
    name: 'helloText',
    text: 'Дорогой испытуемый! \n\nМы изучаем особенности пространственного мышления и хотим выяснить, как люди представляют людей и объекты под разными углами. В данном эксперименте вам предстоит увидеть ряд изображений и после каждого ответить на поставленные вопросы. \nПеред началом вы увидите подробную инструкцию и пример задачи. \n\nЧтобы продолжить, нажмите ПРОБЕЛ.',
    font: 'Arial',
    units: 'height',
    pos: [0, 0], draggable: false, height: 0.03, wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'), opacity: 1,
    depth: 0.0
  });

  helloKey = new core.Keyboard({ psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true });

  // Initialize components for Routine "InstructionMR"
  InstructionMRClock = new util.Clock();
  InstMR_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstMR_text',
    text: 'Вы увидите ряд изображений, на которых человек сидит за столом. Перед человеком в центре стола расположен прямоугольный планшет, и вокруг планшета расположены 4 точки справа, слева, спереди и сзади.\n\nПри показе изображения одна из точек будет загораться. Под изображением вам также будет схематично представлен пример зажигания точек.\n\nВашей задачей будет определить как можно быстрее, СОВПАДАЕТ ЛИ ситуация на изображении с представленным примером.\n\nЕсли изображение и пример РАЗЛИЧАЮТСЯ, нажмите клавишу "<=”. Если они ОДИНАКОВЫЕ, нажмите клавишу “=>”.\n\nДля продолжения нажмите ПРОБЕЛ.',
    font: 'Arial',
    units: undefined,
    pos: [0, (- 0.25)], draggable: false, height: 0.025, wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'), opacity: undefined,
    depth: 0.0
  });

  InstMR_keyresp = new core.Keyboard({ psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true });

  InstMR_image = new visual.ImageStim({
    win: psychoJS.window,
    name: 'InstMR_image', units: 'height',
    image: 'rot60drwhoL.jpg', mask: undefined,
    anchor: 'center',
    ori: 0.0,
    pos: [0, 0.2],
    draggable: false,
    size: [0.5, 0.35],
    color: new util.Color([1, 1, 1]), opacity: undefined,
    flipHoriz: false, flipVert: false,
    texRes: 128.0, interpolate: true, depth: -2.0
  });
  InstMR_stimulus = new visual.ImageStim({
    win: psychoJS.window,
    name: 'InstMR_stimulus', units: 'height',
    image: 'stimuliLeft.png', mask: undefined,
    anchor: 'center',
    ori: 0.0,
    pos: [0, 0],
    draggable: false,
    size: [0.08, 0.03],
    color: new util.Color([1, 1, 1]), opacity: undefined,
    flipHoriz: false, flipVert: false,
    texRes: 128.0, interpolate: true, depth: -3.0
  });
  // Initialize components for Routine "InstructionQnA"
  InstructionQnAClock = new util.Clock();
  InstQnA_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstQnA_text',
    text: 'После ответа на изображения вам нужно оценить, как вы решали задачу. В основном есть 2 типа решения задач: либо через мысленное "поворачивание объектов" до тех пор, пока не получится произвести сравнение, либо через "представление чужой точки зрения" и того, слева или справа по отношению к смотрящему находится зажженая точка.\n\nЕсли в задаче до вопроса вы определили сходство или различие, мысленно поворачивая объекты на столе до нужного угла, нажмите клавишу "<=”.\nЕсли вы определили сходство или различие, представляя себя на чужом месте, нажмите клавишу "=>”. \nЕсли ни один из вариантов не кажется правильным, нажмите клавишу "пробел".\n\nДалее вы потренируетесь на нескольких примерах. Если вы ознакомились с инструкцией, нажмите ПРОБЕЛ.\n',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0], draggable: false, height: 0.025, wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'), opacity: undefined,
    depth: 0.0
  });

  InstQnA_keyresp = new core.Keyboard({ psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true });

  // Initialize components for Routine "InstTest"
  InstTestClock = new util.Clock();
  InstTest_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstTest_text',
    text: 'Перед основной частью эксперимента вы потренируетесь на 4 задачах. Результаты этих задач не будут учитываться.\nВам понадобятся клавиши: "<=", "=>", "пробел".\n\nНе торопитесь, убедитесь, что вы полностью понимаете, что вам нужно делать. Если у вас возникают вопросы, задавайте их экспериментатору.\n\nЕсли готовы приступить, нажмите ПРОБЕЛ.',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0], draggable: false, height: 0.03, wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'), opacity: undefined,
    depth: 0.0
  });

  InstTest_keyresp = new core.Keyboard({ psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true });

  // Initialize components for Routine "TestTrialMR"
  TestTrialMRClock = new util.Clock();
  TestTrialMR_keyresp = new core.Keyboard({ psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true });

  TestTrialMR_stimulus = new visual.ImageStim({
    win: psychoJS.window,
    name: 'TestTrialMR_stimulus', units: 'height',
    image: 'default.png', mask: undefined,
    anchor: 'center',
    ori: 0.0,
    pos: [0, (- 0.27)],
    draggable: false,
    size: [0.08, 0.03],
    color: new util.Color([1, 1, 1]), opacity: undefined,
    flipHoriz: false, flipVert: false,
    texRes: 128.0, interpolate: true, depth: -1.0
  });
  TestTrialMR_image = new visual.ImageStim({
    win: psychoJS.window,
    name: 'TestTrialMR_image', units: undefined,
    image: 'default.png', mask: undefined,
    anchor: 'center',
    ori: 0.0,
    pos: [0, 0],
    draggable: false,
    size: [0.7, 0.5],
    color: new util.Color([1, 1, 1]), opacity: undefined,
    flipHoriz: false, flipVert: false,
    texRes: 128.0, interpolate: true, depth: -2.0
  });
  TestTrialMR_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'TestTrialMR_text',
    text: "нажмите '<=' для ДРУГОЕ         нажмите '=>' для ТО ЖЕ",
    font: 'Arial',
    units: undefined,
    pos: [0, (- 0.4)], draggable: false, height: 0.03, wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'), opacity: undefined,
    depth: -3.0
  });

  // Initialize components for Routine "blank"
  blankClock = new util.Clock();
  polygon_centr = new visual.ShapeStim({
    win: psychoJS.window, name: 'polygon_centr',
    vertices: 'cross', size: [0.1, 0.1],
    ori: 0.0,
    pos: [0, 0],
    draggable: false,
    anchor: 'center',
    lineWidth: 1.0,
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    colorSpace: 'rgb',
    opacity: undefined,
    depth: 0,
    interpolate: true,
  });

  // Initialize components for Routine "TestTrialQnA"
  TestTrialQnAClock = new util.Clock();
  TestTrialQnA_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'TestTrialQnA_text',
    text: 'Как вы решали?\n\n\n<= поворачивая объекты                представляя точку зрения=> ',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0], draggable: false, height: 0.03, wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'), opacity: undefined,
    depth: 0.0
  });

  TestTrialQnA_Ans = new core.Keyboard({ psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true });

  TestTrialQnA_text2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'TestTrialQnA_text2',
    text: 'другое\n||\nv',
    font: 'Open Sans',
    units: undefined,
    pos: [0, (- 0.2)], draggable: false, height: 0.03, wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'), opacity: undefined,
    depth: -2.0
  });

  // Initialize components for Routine "InstBegin"
  InstBeginClock = new util.Clock();
  InstBegin_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstBegin_text',
    text: 'Сейчас начнется основная часть эксперимента.\nБудьте внимательны, не отвлекайтесь.\n\nЧтобы начать, нажмите ПРОБЕЛ.',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0], draggable: false, height: 0.03, wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'), opacity: undefined,
    depth: 0.0
  });

  InstBegin_keyresp = new core.Keyboard({ psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true });

  // Initialize components for Routine "TrialSD"
  TrialSDClock = new util.Clock();
  TrialSD_keyresp = new core.Keyboard({ psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true });

  TrialSD_stimulus = new visual.ImageStim({
    win: psychoJS.window,
    name: 'TrialSD_stimulus', units: 'height',
    image: 'default.png', mask: undefined,
    anchor: 'center',
    ori: 0.0,
    pos: [0, (- 0.27)],
    draggable: false,
    size: [0.08, 0.03],
    color: new util.Color([1, 1, 1]), opacity: undefined,
    flipHoriz: false, flipVert: false,
    texRes: 128.0, interpolate: true, depth: -1.0
  });
  TrialSD_image = new visual.ImageStim({
    win: psychoJS.window,
    name: 'TrialSD_image', units: undefined,
    image: 'default.png', mask: undefined,
    anchor: 'center',
    ori: 0.0,
    pos: [0, 0],
    draggable: false,
    size: [0.7, 0.5],
    color: new util.Color([1, 1, 1]), opacity: undefined,
    flipHoriz: false, flipVert: false,
    texRes: 128.0, interpolate: true, depth: -2.0
  });
  TrialSD_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrialSD_text',
    text: "нажмите '<=' для ДРУГОЕ         нажмите '=>' для ТО ЖЕ",
    font: 'Arial',
    units: undefined,
    pos: [0, (- 0.4)], draggable: false, height: 0.03, wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'), opacity: undefined,
    depth: -3.0
  });

  // Initialize components for Routine "TrialQnA"
  TrialQnAClock = new util.Clock();
  TrialQnA_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrialQnA_text',
    text: 'Как вы решали?\n\n\n<= поворачивая объекты                представляя точку зрения=> ',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0], draggable: false, height: 0.03, wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'), opacity: undefined,
    depth: 0.0
  });

  TrialQnA_Ans = new core.Keyboard({ psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true });

  TrialQnA_text2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrialQnA_text2',
    text: 'другое\n||\nv',
    font: 'Open Sans',
    units: undefined,
    pos: [0, (- 0.2)], draggable: false, height: 0.03, wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'), opacity: undefined,
    depth: -2.0
  });

  // Initialize components for Routine "Goodbye"
  GoodbyeClock = new util.Clock();
  text_Ending = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Ending',
    text: 'Спасибо за участие в эксперименте!\nОбратитесь к экспериментатору для дальнейших инструкций.',
    font: 'Arial',
    units: undefined,
    pos: [0, 0], draggable: false, height: 0.08, wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'), opacity: undefined,
    depth: 0.0
  });

  key_resp_Ending = new core.Keyboard({ psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true });

  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine

  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var HelloMaxDurationReached;
var _helloKey_allKeys;
var HelloMaxDuration;
var HelloComponents;
function HelloRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'Hello' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    HelloClock.reset();
    routineTimer.reset();
    HelloMaxDurationReached = false;
    // update component parameters for each repeat
    helloKey.keys = undefined;
    helloKey.rt = undefined;
    _helloKey_allKeys = [];
    psychoJS.experiment.addData('Hello.started', globalClock.getTime());
    HelloMaxDuration = null
    // keep track of which components have finished
    HelloComponents = [];
    HelloComponents.push(helloText);
    HelloComponents.push(helloKey);

    for (const thisComponent of HelloComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function HelloRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Hello' ---
    // get current time
    t = HelloClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *helloText* updates
    if (t >= 0.0 && helloText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      helloText.tStart = t;  // (not accounting for frame time here)
      helloText.frameNStart = frameN;  // exact frame index

      helloText.setAutoDraw(true);
    }


    // if helloText is active this frame...
    if (helloText.status === PsychoJS.Status.STARTED) {
    }


    // *helloKey* updates
    if (t >= 0.0 && helloKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      helloKey.tStart = t;  // (not accounting for frame time here)
      helloKey.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function () { helloKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function () { helloKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function () { helloKey.clearEvents(); });
    }

    // if helloKey is active this frame...
    if (helloKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = helloKey.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space',
        waitRelease: false
      });
      _helloKey_allKeys = _helloKey_allKeys.concat(theseKeys);
      if (_helloKey_allKeys.length > 0) {
        helloKey.keys = _helloKey_allKeys[_helloKey_allKeys.length - 1].name;  // just the last key pressed
        helloKey.rt = _helloKey_allKeys[_helloKey_allKeys.length - 1].rt;
        helloKey.duration = _helloKey_allKeys[_helloKey_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({ keyList: ['escape'] }).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of HelloComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function HelloRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Hello' ---
    for (const thisComponent of HelloComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Hello.stopped', globalClock.getTime());
    helloKey.stop();
    // the Routine "Hello" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var InstructionMRMaxDurationReached;
var _InstMR_keyresp_allKeys;
var InstructionMRMaxDuration;
var InstructionMRComponents;
function InstructionMRRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'InstructionMR' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    InstructionMRClock.reset();
    routineTimer.reset();
    InstructionMRMaxDurationReached = false;
    // update component parameters for each repeat
    InstMR_keyresp.keys = undefined;
    InstMR_keyresp.rt = undefined;
    _InstMR_keyresp_allKeys = [];
    psychoJS.experiment.addData('InstructionMR.started', globalClock.getTime());
    InstructionMRMaxDuration = null
    // keep track of which components have finished
    InstructionMRComponents = [];
    InstructionMRComponents.push(InstMR_text);
    InstructionMRComponents.push(InstMR_keyresp);
    InstructionMRComponents.push(InstMR_image);
    InstructionMRComponents.push(InstMR_stimulus);

    for (const thisComponent of InstructionMRComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstructionMRRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'InstructionMR' ---
    // get current time
    t = InstructionMRClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *InstMR_text* updates
    if (t >= 0.0 && InstMR_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstMR_text.tStart = t;  // (not accounting for frame time here)
      InstMR_text.frameNStart = frameN;  // exact frame index

      InstMR_text.setAutoDraw(true);
    }


    // if InstMR_text is active this frame...
    if (InstMR_text.status === PsychoJS.Status.STARTED) {
    }


    // *InstMR_keyresp* updates
    if (t >= 0.0 && InstMR_keyresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstMR_keyresp.tStart = t;  // (not accounting for frame time here)
      InstMR_keyresp.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function () { InstMR_keyresp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function () { InstMR_keyresp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function () { InstMR_keyresp.clearEvents(); });
    }

    // if InstMR_keyresp is active this frame...
    if (InstMR_keyresp.status === PsychoJS.Status.STARTED) {
      let theseKeys = InstMR_keyresp.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space',
        waitRelease: false
      });
      _InstMR_keyresp_allKeys = _InstMR_keyresp_allKeys.concat(theseKeys);
      if (_InstMR_keyresp_allKeys.length > 0) {
        InstMR_keyresp.keys = _InstMR_keyresp_allKeys[_InstMR_keyresp_allKeys.length - 1].name;  // just the last key pressed
        InstMR_keyresp.rt = _InstMR_keyresp_allKeys[_InstMR_keyresp_allKeys.length - 1].rt;
        InstMR_keyresp.duration = _InstMR_keyresp_allKeys[_InstMR_keyresp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }


    // *InstMR_image* updates
    if (t >= 0.0 && InstMR_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstMR_image.tStart = t;  // (not accounting for frame time here)
      InstMR_image.frameNStart = frameN;  // exact frame index

      InstMR_image.setAutoDraw(true);
    }


    // if InstMR_image is active this frame...
    if (InstMR_image.status === PsychoJS.Status.STARTED) {
    }


    // *InstMR_stimulus* updates
    if (t >= 0.0 && InstMR_stimulus.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstMR_stimulus.tStart = t;  // (not accounting for frame time here)
      InstMR_stimulus.frameNStart = frameN;  // exact frame index

      InstMR_stimulus.setAutoDraw(true);
    }


    // if InstMR_stimulus is active this frame...
    if (InstMR_stimulus.status === PsychoJS.Status.STARTED) {
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({ keyList: ['escape'] }).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstructionMRComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionMRRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'InstructionMR' ---
    for (const thisComponent of InstructionMRComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('InstructionMR.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(InstMR_keyresp.corr, level);
    }
    psychoJS.experiment.addData('InstMR_keyresp.keys', InstMR_keyresp.keys);
    if (typeof InstMR_keyresp.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('InstMR_keyresp.rt', InstMR_keyresp.rt);
      psychoJS.experiment.addData('InstMR_keyresp.duration', InstMR_keyresp.duration);
      routineTimer.reset();
    }

    InstMR_keyresp.stop();
    // the Routine "InstructionMR" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var InstructionQnAMaxDurationReached;
var _InstQnA_keyresp_allKeys;
var InstructionQnAMaxDuration;
var InstructionQnAComponents;
function InstructionQnARoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'InstructionQnA' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    InstructionQnAClock.reset();
    routineTimer.reset();
    InstructionQnAMaxDurationReached = false;
    // update component parameters for each repeat
    InstQnA_keyresp.keys = undefined;
    InstQnA_keyresp.rt = undefined;
    _InstQnA_keyresp_allKeys = [];
    psychoJS.experiment.addData('InstructionQnA.started', globalClock.getTime());
    InstructionQnAMaxDuration = null
    // keep track of which components have finished
    InstructionQnAComponents = [];
    InstructionQnAComponents.push(InstQnA_text);
    InstructionQnAComponents.push(InstQnA_keyresp);

    for (const thisComponent of InstructionQnAComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstructionQnARoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'InstructionQnA' ---
    // get current time
    t = InstructionQnAClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *InstQnA_text* updates
    if (t >= 0.0 && InstQnA_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstQnA_text.tStart = t;  // (not accounting for frame time here)
      InstQnA_text.frameNStart = frameN;  // exact frame index

      InstQnA_text.setAutoDraw(true);
    }


    // if InstQnA_text is active this frame...
    if (InstQnA_text.status === PsychoJS.Status.STARTED) {
    }


    // *InstQnA_keyresp* updates
    if (t >= 0.0 && InstQnA_keyresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstQnA_keyresp.tStart = t;  // (not accounting for frame time here)
      InstQnA_keyresp.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function () { InstQnA_keyresp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function () { InstQnA_keyresp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function () { InstQnA_keyresp.clearEvents(); });
    }

    // if InstQnA_keyresp is active this frame...
    if (InstQnA_keyresp.status === PsychoJS.Status.STARTED) {
      let theseKeys = InstQnA_keyresp.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space',
        waitRelease: false
      });
      _InstQnA_keyresp_allKeys = _InstQnA_keyresp_allKeys.concat(theseKeys);
      if (_InstQnA_keyresp_allKeys.length > 0) {
        InstQnA_keyresp.keys = _InstQnA_keyresp_allKeys[_InstQnA_keyresp_allKeys.length - 1].name;  // just the last key pressed
        InstQnA_keyresp.rt = _InstQnA_keyresp_allKeys[_InstQnA_keyresp_allKeys.length - 1].rt;
        InstQnA_keyresp.duration = _InstQnA_keyresp_allKeys[_InstQnA_keyresp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({ keyList: ['escape'] }).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstructionQnAComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionQnARoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'InstructionQnA' ---
    for (const thisComponent of InstructionQnAComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('InstructionQnA.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(InstQnA_keyresp.corr, level);
    }
    psychoJS.experiment.addData('InstQnA_keyresp.keys', InstQnA_keyresp.keys);
    if (typeof InstQnA_keyresp.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('InstQnA_keyresp.rt', InstQnA_keyresp.rt);
      psychoJS.experiment.addData('InstQnA_keyresp.duration', InstQnA_keyresp.duration);
      routineTimer.reset();
    }

    InstQnA_keyresp.stop();
    // the Routine "InstructionQnA" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var InstTestMaxDurationReached;
var _InstTest_keyresp_allKeys;
var InstTestMaxDuration;
var InstTestComponents;
function InstTestRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'InstTest' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    InstTestClock.reset();
    routineTimer.reset();
    InstTestMaxDurationReached = false;
    // update component parameters for each repeat
    InstTest_keyresp.keys = undefined;
    InstTest_keyresp.rt = undefined;
    _InstTest_keyresp_allKeys = [];
    psychoJS.experiment.addData('InstTest.started', globalClock.getTime());
    InstTestMaxDuration = null
    // keep track of which components have finished
    InstTestComponents = [];
    InstTestComponents.push(InstTest_text);
    InstTestComponents.push(InstTest_keyresp);

    for (const thisComponent of InstTestComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstTestRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'InstTest' ---
    // get current time
    t = InstTestClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *InstTest_text* updates
    if (t >= 0.0 && InstTest_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstTest_text.tStart = t;  // (not accounting for frame time here)
      InstTest_text.frameNStart = frameN;  // exact frame index

      InstTest_text.setAutoDraw(true);
    }


    // if InstTest_text is active this frame...
    if (InstTest_text.status === PsychoJS.Status.STARTED) {
    }


    // *InstTest_keyresp* updates
    if (t >= 0.0 && InstTest_keyresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstTest_keyresp.tStart = t;  // (not accounting for frame time here)
      InstTest_keyresp.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function () { InstTest_keyresp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function () { InstTest_keyresp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function () { InstTest_keyresp.clearEvents(); });
    }

    // if InstTest_keyresp is active this frame...
    if (InstTest_keyresp.status === PsychoJS.Status.STARTED) {
      let theseKeys = InstTest_keyresp.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space',
        waitRelease: false
      });
      _InstTest_keyresp_allKeys = _InstTest_keyresp_allKeys.concat(theseKeys);
      if (_InstTest_keyresp_allKeys.length > 0) {
        InstTest_keyresp.keys = _InstTest_keyresp_allKeys[_InstTest_keyresp_allKeys.length - 1].name;  // just the last key pressed
        InstTest_keyresp.rt = _InstTest_keyresp_allKeys[_InstTest_keyresp_allKeys.length - 1].rt;
        InstTest_keyresp.duration = _InstTest_keyresp_allKeys[_InstTest_keyresp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({ keyList: ['escape'] }).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstTestComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstTestRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'InstTest' ---
    for (const thisComponent of InstTestComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('InstTest.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(InstTest_keyresp.corr, level);
    }
    psychoJS.experiment.addData('InstTest_keyresp.keys', InstTest_keyresp.keys);
    if (typeof InstTest_keyresp.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('InstTest_keyresp.rt', InstTest_keyresp.rt);
      psychoJS.experiment.addData('InstTest_keyresp.duration', InstTest_keyresp.duration);
      routineTimer.reset();
    }

    InstTest_keyresp.stop();
    // the Routine "InstTest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var testTrials;
function testTrialsLoopBegin(testTrialsLoopScheduler, snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop

    // set up handler to look after randomisation of conditions etc
    testTrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'condition_file_2.xlsx', '12:16'),
      seed: undefined, name: 'testTrials'
    });
    psychoJS.experiment.addLoop(testTrials); // add the loop to the experiment
    currentLoop = testTrials;  // we're now the current loop

    // Schedule all the trials in the trialList:
    for (const thisTestTrial of testTrials) {
      snapshot = testTrials.getSnapshot();
      testTrialsLoopScheduler.add(importConditions(snapshot));
      testTrialsLoopScheduler.add(TestTrialMRRoutineBegin(snapshot));
      testTrialsLoopScheduler.add(TestTrialMRRoutineEachFrame());
      testTrialsLoopScheduler.add(TestTrialMRRoutineEnd(snapshot));
      testTrialsLoopScheduler.add(blankRoutineBegin(snapshot));
      testTrialsLoopScheduler.add(blankRoutineEachFrame());
      testTrialsLoopScheduler.add(blankRoutineEnd(snapshot));
      testTrialsLoopScheduler.add(TestTrialQnARoutineBegin(snapshot));
      testTrialsLoopScheduler.add(TestTrialQnARoutineEachFrame());
      testTrialsLoopScheduler.add(TestTrialQnARoutineEnd(snapshot));
      testTrialsLoopScheduler.add(blankRoutineBegin(snapshot));
      testTrialsLoopScheduler.add(blankRoutineEachFrame());
      testTrialsLoopScheduler.add(blankRoutineEnd(snapshot));
      testTrialsLoopScheduler.add(testTrialsLoopEndIteration(testTrialsLoopScheduler, snapshot));
    }

    return Scheduler.Event.NEXT;
  }
}


async function testTrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(testTrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length > 0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function testTrialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  };
}


var loopSD;
function loopSDLoopBegin(loopSDLoopScheduler, snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop

    // set up handler to look after randomisation of conditions etc
    loopSD = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 2, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'condition_file_2.xlsx',
      seed: undefined, name: 'loopSD'
    });
    psychoJS.experiment.addLoop(loopSD); // add the loop to the experiment
    currentLoop = loopSD;  // we're now the current loop

    // Schedule all the trials in the trialList:
    for (const thisLoopSD of loopSD) {
      snapshot = loopSD.getSnapshot();
      loopSDLoopScheduler.add(importConditions(snapshot));
      loopSDLoopScheduler.add(TrialSDRoutineBegin(snapshot));
      loopSDLoopScheduler.add(TrialSDRoutineEachFrame());
      loopSDLoopScheduler.add(TrialSDRoutineEnd(snapshot));
      loopSDLoopScheduler.add(blankRoutineBegin(snapshot));
      loopSDLoopScheduler.add(blankRoutineEachFrame());
      loopSDLoopScheduler.add(blankRoutineEnd(snapshot));
      loopSDLoopScheduler.add(TrialQnARoutineBegin(snapshot));
      loopSDLoopScheduler.add(TrialQnARoutineEachFrame());
      loopSDLoopScheduler.add(TrialQnARoutineEnd(snapshot));
      loopSDLoopScheduler.add(blankRoutineBegin(snapshot));
      loopSDLoopScheduler.add(blankRoutineEachFrame());
      loopSDLoopScheduler.add(blankRoutineEnd(snapshot));
      loopSDLoopScheduler.add(loopSDLoopEndIteration(loopSDLoopScheduler, snapshot));
    }

    return Scheduler.Event.NEXT;
  }
}


async function loopSDLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loopSD);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length > 0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function loopSDLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  };
}


var TestTrialMRMaxDurationReached;
var _TestTrialMR_keyresp_allKeys;
var TestTrialMRMaxDuration;
var TestTrialMRComponents;
function TestTrialMRRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'TestTrialMR' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    TestTrialMRClock.reset();
    routineTimer.reset();
    TestTrialMRMaxDurationReached = false;
    // update component parameters for each repeat
    TestTrialMR_keyresp.keys = undefined;
    TestTrialMR_keyresp.rt = undefined;
    _TestTrialMR_keyresp_allKeys = [];
    TestTrialMR_stimulus.setImage(stimulifile);
    TestTrialMR_image.setImage(imagefile);
    psychoJS.experiment.addData('TestTrialMR.started', globalClock.getTime());
    TestTrialMRMaxDuration = null
    // keep track of which components have finished
    TestTrialMRComponents = [];
    TestTrialMRComponents.push(TestTrialMR_keyresp);
    TestTrialMRComponents.push(TestTrialMR_stimulus);
    TestTrialMRComponents.push(TestTrialMR_image);
    TestTrialMRComponents.push(TestTrialMR_text);

    for (const thisComponent of TestTrialMRComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TestTrialMRRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'TestTrialMR' ---
    // get current time
    t = TestTrialMRClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *TestTrialMR_keyresp* updates
    if (t >= 0.0 && TestTrialMR_keyresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TestTrialMR_keyresp.tStart = t;  // (not accounting for frame time here)
      TestTrialMR_keyresp.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function () { TestTrialMR_keyresp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function () { TestTrialMR_keyresp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function () { TestTrialMR_keyresp.clearEvents(); });
    }

    // if TestTrialMR_keyresp is active this frame...
    if (TestTrialMR_keyresp.status === PsychoJS.Status.STARTED) {
      let theseKeys = TestTrialMR_keyresp.getKeys({
        keyList: typeof ['left', 'right'] === 'string' ? [['left', 'right']] : ['left', 'right'],
        waitRelease: false
      });
      _TestTrialMR_keyresp_allKeys = _TestTrialMR_keyresp_allKeys.concat(theseKeys);
      if (_TestTrialMR_keyresp_allKeys.length > 0) {
        TestTrialMR_keyresp.keys = _TestTrialMR_keyresp_allKeys[_TestTrialMR_keyresp_allKeys.length - 1].name;  // just the last key pressed
        TestTrialMR_keyresp.rt = _TestTrialMR_keyresp_allKeys[_TestTrialMR_keyresp_allKeys.length - 1].rt;
        TestTrialMR_keyresp.duration = _TestTrialMR_keyresp_allKeys[_TestTrialMR_keyresp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }


    // *TestTrialMR_stimulus* updates
    if (t >= 0.0 && TestTrialMR_stimulus.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TestTrialMR_stimulus.tStart = t;  // (not accounting for frame time here)
      TestTrialMR_stimulus.frameNStart = frameN;  // exact frame index

      TestTrialMR_stimulus.setAutoDraw(true);
    }


    // if TestTrialMR_stimulus is active this frame...
    if (TestTrialMR_stimulus.status === PsychoJS.Status.STARTED) {
    }


    // *TestTrialMR_image* updates
    if (t >= 0.0 && TestTrialMR_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TestTrialMR_image.tStart = t;  // (not accounting for frame time here)
      TestTrialMR_image.frameNStart = frameN;  // exact frame index

      TestTrialMR_image.setAutoDraw(true);
    }


    // if TestTrialMR_image is active this frame...
    if (TestTrialMR_image.status === PsychoJS.Status.STARTED) {
    }


    // *TestTrialMR_text* updates
    if (t >= 0.0 && TestTrialMR_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TestTrialMR_text.tStart = t;  // (not accounting for frame time here)
      TestTrialMR_text.frameNStart = frameN;  // exact frame index

      TestTrialMR_text.setAutoDraw(true);
    }


    // if TestTrialMR_text is active this frame...
    if (TestTrialMR_text.status === PsychoJS.Status.STARTED) {
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({ keyList: ['escape'] }).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TestTrialMRComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TestTrialMRRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'TestTrialMR' ---
    for (const thisComponent of TestTrialMRComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('TestTrialMR.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(TestTrialMR_keyresp.corr, level);
    }
    psychoJS.experiment.addData('TestTrialMR_keyresp.keys', TestTrialMR_keyresp.keys);
    if (typeof TestTrialMR_keyresp.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('TestTrialMR_keyresp.rt', TestTrialMR_keyresp.rt);
      psychoJS.experiment.addData('TestTrialMR_keyresp.duration', TestTrialMR_keyresp.duration);
      routineTimer.reset();
    }

    TestTrialMR_keyresp.stop();
    // the Routine "TestTrialMR" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var blankMaxDurationReached;
var blankMaxDuration;
var blankComponents;
function blankRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'blank' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    blankClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    blankMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('blank.started', globalClock.getTime());
    blankMaxDuration = null
    // keep track of which components have finished
    blankComponents = [];
    blankComponents.push(polygon_centr);

    for (const thisComponent of blankComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function blankRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'blank' ---
    // get current time
    t = blankClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *polygon_centr* updates
    if (t >= 0.0 && polygon_centr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_centr.tStart = t;  // (not accounting for frame time here)
      polygon_centr.frameNStart = frameN;  // exact frame index

      polygon_centr.setAutoDraw(true);
    }


    // if polygon_centr is active this frame...
    if (polygon_centr.status === PsychoJS.Status.STARTED) {
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (polygon_centr.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      polygon_centr.tStop = t;  // not accounting for scr refresh
      polygon_centr.frameNStop = frameN;  // exact frame index
      // update status
      polygon_centr.status = PsychoJS.Status.FINISHED;
      polygon_centr.setAutoDraw(false);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({ keyList: ['escape'] }).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of blankComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function blankRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'blank' ---
    for (const thisComponent of blankComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('blank.stopped', globalClock.getTime());
    if (routineForceEnded) {
      routineTimer.reset();
    } else if (blankMaxDurationReached) {
      blankClock.add(blankMaxDuration);
    } else {
      blankClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var TestTrialQnAMaxDurationReached;
var _TestTrialQnA_Ans_allKeys;
var TestTrialQnAMaxDuration;
var TestTrialQnAComponents;
function TestTrialQnARoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'TestTrialQnA' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    TestTrialQnAClock.reset();
    routineTimer.reset();
    TestTrialQnAMaxDurationReached = false;
    // update component parameters for each repeat
    TestTrialQnA_Ans.keys = undefined;
    TestTrialQnA_Ans.rt = undefined;
    _TestTrialQnA_Ans_allKeys = [];
    psychoJS.experiment.addData('TestTrialQnA.started', globalClock.getTime());
    TestTrialQnAMaxDuration = null
    // keep track of which components have finished
    TestTrialQnAComponents = [];
    TestTrialQnAComponents.push(TestTrialQnA_text);
    TestTrialQnAComponents.push(TestTrialQnA_Ans);
    TestTrialQnAComponents.push(TestTrialQnA_text2);

    for (const thisComponent of TestTrialQnAComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TestTrialQnARoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'TestTrialQnA' ---
    // get current time
    t = TestTrialQnAClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *TestTrialQnA_text* updates
    if (t >= 0.0 && TestTrialQnA_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TestTrialQnA_text.tStart = t;  // (not accounting for frame time here)
      TestTrialQnA_text.frameNStart = frameN;  // exact frame index

      TestTrialQnA_text.setAutoDraw(true);
    }


    // if TestTrialQnA_text is active this frame...
    if (TestTrialQnA_text.status === PsychoJS.Status.STARTED) {
    }


    // *TestTrialQnA_Ans* updates
    if (t >= 0.0 && TestTrialQnA_Ans.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TestTrialQnA_Ans.tStart = t;  // (not accounting for frame time here)
      TestTrialQnA_Ans.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function () { TestTrialQnA_Ans.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function () { TestTrialQnA_Ans.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function () { TestTrialQnA_Ans.clearEvents(); });
    }

    // if TestTrialQnA_Ans is active this frame...
    if (TestTrialQnA_Ans.status === PsychoJS.Status.STARTED) {
      let theseKeys = TestTrialQnA_Ans.getKeys({
        keyList: typeof ['left', 'right', 'space'] === 'string' ? [['left', 'right', 'space']] : ['left', 'right', 'space'],
        waitRelease: false
      });
      _TestTrialQnA_Ans_allKeys = _TestTrialQnA_Ans_allKeys.concat(theseKeys);
      if (_TestTrialQnA_Ans_allKeys.length > 0) {
        TestTrialQnA_Ans.keys = _TestTrialQnA_Ans_allKeys[_TestTrialQnA_Ans_allKeys.length - 1].name;  // just the last key pressed
        TestTrialQnA_Ans.rt = _TestTrialQnA_Ans_allKeys[_TestTrialQnA_Ans_allKeys.length - 1].rt;
        TestTrialQnA_Ans.duration = _TestTrialQnA_Ans_allKeys[_TestTrialQnA_Ans_allKeys.length - 1].duration;
        // was this correct?
        if (TestTrialQnA_Ans.keys == '') {
          TestTrialQnA_Ans.corr = 1;
        } else {
          TestTrialQnA_Ans.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }


    // *TestTrialQnA_text2* updates
    if (t >= 0.0 && TestTrialQnA_text2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TestTrialQnA_text2.tStart = t;  // (not accounting for frame time here)
      TestTrialQnA_text2.frameNStart = frameN;  // exact frame index

      TestTrialQnA_text2.setAutoDraw(true);
    }


    // if TestTrialQnA_text2 is active this frame...
    if (TestTrialQnA_text2.status === PsychoJS.Status.STARTED) {
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({ keyList: ['escape'] }).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TestTrialQnAComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TestTrialQnARoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'TestTrialQnA' ---
    for (const thisComponent of TestTrialQnAComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('TestTrialQnA.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (TestTrialQnA_Ans.keys === undefined) {
      if (['None', 'none', undefined].includes('')) {
        TestTrialQnA_Ans.corr = 1;  // correct non-response
      } else {
        TestTrialQnA_Ans.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(TestTrialQnA_Ans.corr, level);
    }
    psychoJS.experiment.addData('TestTrialQnA_Ans.keys', TestTrialQnA_Ans.keys);
    psychoJS.experiment.addData('TestTrialQnA_Ans.corr', TestTrialQnA_Ans.corr);
    if (typeof TestTrialQnA_Ans.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('TestTrialQnA_Ans.rt', TestTrialQnA_Ans.rt);
      psychoJS.experiment.addData('TestTrialQnA_Ans.duration', TestTrialQnA_Ans.duration);
      routineTimer.reset();
    }

    TestTrialQnA_Ans.stop();
    // the Routine "TestTrialQnA" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var InstBeginMaxDurationReached;
var _InstBegin_keyresp_allKeys;
var InstBeginMaxDuration;
var InstBeginComponents;
function InstBeginRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'InstBegin' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    InstBeginClock.reset();
    routineTimer.reset();
    InstBeginMaxDurationReached = false;
    // update component parameters for each repeat
    InstBegin_keyresp.keys = undefined;
    InstBegin_keyresp.rt = undefined;
    _InstBegin_keyresp_allKeys = [];
    psychoJS.experiment.addData('InstBegin.started', globalClock.getTime());
    InstBeginMaxDuration = null
    // keep track of which components have finished
    InstBeginComponents = [];
    InstBeginComponents.push(InstBegin_text);
    InstBeginComponents.push(InstBegin_keyresp);

    for (const thisComponent of InstBeginComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstBeginRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'InstBegin' ---
    // get current time
    t = InstBeginClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *InstBegin_text* updates
    if (t >= 0.0 && InstBegin_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstBegin_text.tStart = t;  // (not accounting for frame time here)
      InstBegin_text.frameNStart = frameN;  // exact frame index

      InstBegin_text.setAutoDraw(true);
    }


    // if InstBegin_text is active this frame...
    if (InstBegin_text.status === PsychoJS.Status.STARTED) {
    }


    // *InstBegin_keyresp* updates
    if (t >= 0.0 && InstBegin_keyresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstBegin_keyresp.tStart = t;  // (not accounting for frame time here)
      InstBegin_keyresp.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function () { InstBegin_keyresp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function () { InstBegin_keyresp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function () { InstBegin_keyresp.clearEvents(); });
    }

    // if InstBegin_keyresp is active this frame...
    if (InstBegin_keyresp.status === PsychoJS.Status.STARTED) {
      let theseKeys = InstBegin_keyresp.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space',
        waitRelease: false
      });
      _InstBegin_keyresp_allKeys = _InstBegin_keyresp_allKeys.concat(theseKeys);
      if (_InstBegin_keyresp_allKeys.length > 0) {
        InstBegin_keyresp.keys = _InstBegin_keyresp_allKeys[_InstBegin_keyresp_allKeys.length - 1].name;  // just the last key pressed
        InstBegin_keyresp.rt = _InstBegin_keyresp_allKeys[_InstBegin_keyresp_allKeys.length - 1].rt;
        InstBegin_keyresp.duration = _InstBegin_keyresp_allKeys[_InstBegin_keyresp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({ keyList: ['escape'] }).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstBeginComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstBeginRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'InstBegin' ---
    for (const thisComponent of InstBeginComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('InstBegin.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(InstBegin_keyresp.corr, level);
    }
    psychoJS.experiment.addData('InstBegin_keyresp.keys', InstBegin_keyresp.keys);
    if (typeof InstBegin_keyresp.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('InstBegin_keyresp.rt', InstBegin_keyresp.rt);
      psychoJS.experiment.addData('InstBegin_keyresp.duration', InstBegin_keyresp.duration);
      routineTimer.reset();
    }

    InstBegin_keyresp.stop();
    // the Routine "InstBegin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var TrialSDMaxDurationReached;
var _TrialSD_keyresp_allKeys;
var TrialSDMaxDuration;
var TrialSDComponents;
function TrialSDRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'TrialSD' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    TrialSDClock.reset();
    routineTimer.reset();
    TrialSDMaxDurationReached = false;
    // update component parameters for each repeat
    TrialSD_keyresp.keys = undefined;
    TrialSD_keyresp.rt = undefined;
    _TrialSD_keyresp_allKeys = [];
    TrialSD_stimulus.setImage(stimulifile);
    TrialSD_image.setImage(imagefile);
    psychoJS.experiment.addData('TrialSD.started', globalClock.getTime());
    TrialSDMaxDuration = null
    // keep track of which components have finished
    TrialSDComponents = [];
    TrialSDComponents.push(TrialSD_keyresp);
    TrialSDComponents.push(TrialSD_stimulus);
    TrialSDComponents.push(TrialSD_image);
    TrialSDComponents.push(TrialSD_text);

    for (const thisComponent of TrialSDComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TrialSDRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'TrialSD' ---
    // get current time
    t = TrialSDClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *TrialSD_keyresp* updates
    if (t >= 0.0 && TrialSD_keyresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrialSD_keyresp.tStart = t;  // (not accounting for frame time here)
      TrialSD_keyresp.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function () { TrialSD_keyresp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function () { TrialSD_keyresp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function () { TrialSD_keyresp.clearEvents(); });
    }

    // if TrialSD_keyresp is active this frame...
    if (TrialSD_keyresp.status === PsychoJS.Status.STARTED) {
      let theseKeys = TrialSD_keyresp.getKeys({
        keyList: typeof ['left', 'right'] === 'string' ? [['left', 'right']] : ['left', 'right'],
        waitRelease: false
      });
      _TrialSD_keyresp_allKeys = _TrialSD_keyresp_allKeys.concat(theseKeys);
      if (_TrialSD_keyresp_allKeys.length > 0) {
        TrialSD_keyresp.keys = _TrialSD_keyresp_allKeys[_TrialSD_keyresp_allKeys.length - 1].name;  // just the last key pressed
        TrialSD_keyresp.rt = _TrialSD_keyresp_allKeys[_TrialSD_keyresp_allKeys.length - 1].rt;
        TrialSD_keyresp.duration = _TrialSD_keyresp_allKeys[_TrialSD_keyresp_allKeys.length - 1].duration;
        // was this correct?
        if (TrialSD_keyresp.keys == corrAns) {
          TrialSD_keyresp.corr = 1;
        } else {
          TrialSD_keyresp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }


    // *TrialSD_stimulus* updates
    if (t >= 0.0 && TrialSD_stimulus.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrialSD_stimulus.tStart = t;  // (not accounting for frame time here)
      TrialSD_stimulus.frameNStart = frameN;  // exact frame index

      TrialSD_stimulus.setAutoDraw(true);
    }


    // if TrialSD_stimulus is active this frame...
    if (TrialSD_stimulus.status === PsychoJS.Status.STARTED) {
    }


    // *TrialSD_image* updates
    if (t >= 0.0 && TrialSD_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrialSD_image.tStart = t;  // (not accounting for frame time here)
      TrialSD_image.frameNStart = frameN;  // exact frame index

      TrialSD_image.setAutoDraw(true);
    }


    // if TrialSD_image is active this frame...
    if (TrialSD_image.status === PsychoJS.Status.STARTED) {
    }


    // *TrialSD_text* updates
    if (t >= 0.0 && TrialSD_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrialSD_text.tStart = t;  // (not accounting for frame time here)
      TrialSD_text.frameNStart = frameN;  // exact frame index

      TrialSD_text.setAutoDraw(true);
    }


    // if TrialSD_text is active this frame...
    if (TrialSD_text.status === PsychoJS.Status.STARTED) {
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({ keyList: ['escape'] }).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TrialSDComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TrialSDRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'TrialSD' ---
    for (const thisComponent of TrialSDComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('TrialSD.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (TrialSD_keyresp.keys === undefined) {
      if (['None', 'none', undefined].includes(corrAns)) {
        TrialSD_keyresp.corr = 1;  // correct non-response
      } else {
        TrialSD_keyresp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(TrialSD_keyresp.corr, level);
    }
    psychoJS.experiment.addData('TrialSD_keyresp.keys', TrialSD_keyresp.keys);
    psychoJS.experiment.addData('TrialSD_keyresp.corr', TrialSD_keyresp.corr);
    if (typeof TrialSD_keyresp.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('TrialSD_keyresp.rt', TrialSD_keyresp.rt);
      psychoJS.experiment.addData('TrialSD_keyresp.duration', TrialSD_keyresp.duration);
      routineTimer.reset();
    }

    TrialSD_keyresp.stop();
    // the Routine "TrialSD" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var TrialQnAMaxDurationReached;
var _TrialQnA_Ans_allKeys;
var TrialQnAMaxDuration;
var TrialQnAComponents;
function TrialQnARoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'TrialQnA' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    TrialQnAClock.reset();
    routineTimer.reset();
    TrialQnAMaxDurationReached = false;
    // update component parameters for each repeat
    TrialQnA_Ans.keys = undefined;
    TrialQnA_Ans.rt = undefined;
    _TrialQnA_Ans_allKeys = [];
    psychoJS.experiment.addData('TrialQnA.started', globalClock.getTime());
    TrialQnAMaxDuration = null
    // keep track of which components have finished
    TrialQnAComponents = [];
    TrialQnAComponents.push(TrialQnA_text);
    TrialQnAComponents.push(TrialQnA_Ans);
    TrialQnAComponents.push(TrialQnA_text2);

    for (const thisComponent of TrialQnAComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TrialQnARoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'TrialQnA' ---
    // get current time
    t = TrialQnAClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *TrialQnA_text* updates
    if (t >= 0.0 && TrialQnA_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrialQnA_text.tStart = t;  // (not accounting for frame time here)
      TrialQnA_text.frameNStart = frameN;  // exact frame index

      TrialQnA_text.setAutoDraw(true);
    }


    // if TrialQnA_text is active this frame...
    if (TrialQnA_text.status === PsychoJS.Status.STARTED) {
    }


    // *TrialQnA_Ans* updates
    if (t >= 0.0 && TrialQnA_Ans.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrialQnA_Ans.tStart = t;  // (not accounting for frame time here)
      TrialQnA_Ans.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function () { TrialQnA_Ans.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function () { TrialQnA_Ans.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function () { TrialQnA_Ans.clearEvents(); });
    }

    // if TrialQnA_Ans is active this frame...
    if (TrialQnA_Ans.status === PsychoJS.Status.STARTED) {
      let theseKeys = TrialQnA_Ans.getKeys({
        keyList: typeof ['left', 'right', 'space'] === 'string' ? [['left', 'right', 'space']] : ['left', 'right', 'space'],
        waitRelease: false
      });
      _TrialQnA_Ans_allKeys = _TrialQnA_Ans_allKeys.concat(theseKeys);
      if (_TrialQnA_Ans_allKeys.length > 0) {
        TrialQnA_Ans.keys = _TrialQnA_Ans_allKeys[_TrialQnA_Ans_allKeys.length - 1].name;  // just the last key pressed
        TrialQnA_Ans.rt = _TrialQnA_Ans_allKeys[_TrialQnA_Ans_allKeys.length - 1].rt;
        TrialQnA_Ans.duration = _TrialQnA_Ans_allKeys[_TrialQnA_Ans_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }


    // *TrialQnA_text2* updates
    if (t >= 0.0 && TrialQnA_text2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrialQnA_text2.tStart = t;  // (not accounting for frame time here)
      TrialQnA_text2.frameNStart = frameN;  // exact frame index

      TrialQnA_text2.setAutoDraw(true);
    }


    // if TrialQnA_text2 is active this frame...
    if (TrialQnA_text2.status === PsychoJS.Status.STARTED) {
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({ keyList: ['escape'] }).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TrialQnAComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TrialQnARoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'TrialQnA' ---
    for (const thisComponent of TrialQnAComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('TrialQnA.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(TrialQnA_Ans.corr, level);
    }
    psychoJS.experiment.addData('TrialQnA_Ans.keys', TrialQnA_Ans.keys);
    if (typeof TrialQnA_Ans.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('TrialQnA_Ans.rt', TrialQnA_Ans.rt);
      psychoJS.experiment.addData('TrialQnA_Ans.duration', TrialQnA_Ans.duration);
      routineTimer.reset();
    }

    TrialQnA_Ans.stop();
    // the Routine "TrialQnA" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var GoodbyeMaxDurationReached;
var _key_resp_Ending_allKeys;
var GoodbyeMaxDuration;
var GoodbyeComponents;
function GoodbyeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'Goodbye' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    GoodbyeClock.reset();
    routineTimer.reset();
    GoodbyeMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_Ending.keys = undefined;
    key_resp_Ending.rt = undefined;
    _key_resp_Ending_allKeys = [];
    psychoJS.experiment.addData('Goodbye.started', globalClock.getTime());
    GoodbyeMaxDuration = null
    // keep track of which components have finished
    GoodbyeComponents = [];
    GoodbyeComponents.push(text_Ending);
    GoodbyeComponents.push(key_resp_Ending);

    for (const thisComponent of GoodbyeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function GoodbyeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Goodbye' ---
    // get current time
    t = GoodbyeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *text_Ending* updates
    if (t >= 0.0 && text_Ending.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Ending.tStart = t;  // (not accounting for frame time here)
      text_Ending.frameNStart = frameN;  // exact frame index

      text_Ending.setAutoDraw(true);
    }


    // if text_Ending is active this frame...
    if (text_Ending.status === PsychoJS.Status.STARTED) {
    }


    // *key_resp_Ending* updates
    if (t >= 0.0 && key_resp_Ending.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_Ending.tStart = t;  // (not accounting for frame time here)
      key_resp_Ending.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function () { key_resp_Ending.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function () { key_resp_Ending.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function () { key_resp_Ending.clearEvents(); });
    }

    // if key_resp_Ending is active this frame...
    if (key_resp_Ending.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_Ending.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space',
        waitRelease: false
      });
      _key_resp_Ending_allKeys = _key_resp_Ending_allKeys.concat(theseKeys);
      if (_key_resp_Ending_allKeys.length > 0) {
        key_resp_Ending.keys = _key_resp_Ending_allKeys[_key_resp_Ending_allKeys.length - 1].name;  // just the last key pressed
        key_resp_Ending.rt = _key_resp_Ending_allKeys[_key_resp_Ending_allKeys.length - 1].rt;
        key_resp_Ending.duration = _key_resp_Ending_allKeys[_key_resp_Ending_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({ keyList: ['escape'] }).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of GoodbyeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function GoodbyeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Goodbye' ---
    for (const thisComponent of GoodbyeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Goodbye.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_Ending.corr, level);
    }
    psychoJS.experiment.addData('key_resp_Ending.keys', key_resp_Ending.keys);
    if (typeof key_resp_Ending.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('key_resp_Ending.rt', key_resp_Ending.rt);
      psychoJS.experiment.addData('key_resp_Ending.duration', key_resp_Ending.duration);
      routineTimer.reset();
    }

    key_resp_Ending.stop();
    // the Routine "Goodbye" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
  };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({ message: message, isCompleted: isCompleted });

  return Scheduler.Event.QUIT;
}
