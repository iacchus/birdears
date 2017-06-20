# BirdEars

[![Maintenance](https://img.shields.io/maintenance/yes/2017.svg?style=flat)](https://github.com/iacchus/birdears/issues/new?title=Is+birdears+still+maintained&body=Please+file+an+issue+if+the+maintained+button+says+no)
[![Travis Build Status](https://img.shields.io/travis/iacchus/birdears.svg?style=flat&label=build)](https://travis-ci.org/iacchus/birdears)
[![Coveralls](https://img.shields.io/coveralls/iacchus/birdears.svg?style=flat&label=Coveralls)](https://coveralls.io/github/iacchus/birdears)
[![Codecov](https://img.shields.io/codecov/c/github/iacchus/birdears.svg?style=flat&label=Codecov)](https://codecov.io/gh/iacchus/birdears)
[![Code Climate coverage](https://img.shields.io/codeclimate/coverage/github/iacchus/birdears.svg?style=flat&label=Codeclimate)](https://codeclimate.com/github/iacchus/birdears)
[![Code Climate issues](https://img.shields.io/codeclimate/issues/github/iacchus/birdears.svg?style=flat&label=cclimate-issues)](https://codeclimate.com/github/iacchus/birdears/issues)
[![Code Climate gpa](https://img.shields.io/codeclimate/github/iacchus/birdears.svg?style=flat&label=cclimate-GPA)](https://codeclimate.com/github/iacchus/birdears)
[![Gitter](https://img.shields.io/gitter/room/birdears/Lobby.svg?style=flat)](https://gitter.im/birdears/Lobby)

[![GitHub (pre-)release](https://img.shields.io/github/release/iacchus/birdears/all.svg?style=flat)](https://github.com/iacchus/birdears/releases)
[![PyPI Status](https://img.shields.io/pypi/status/birdears.svg?style=flat&label=pypi-status)](https://pypi.python.org/pypi/birdears)
[![PyPI Version](https://img.shields.io/pypi/v/birdears.svg?style=flat)](https://pypi.python.org/pypi/birdears)
[![PyPI Python Versions](https://img.shields.io/pypi/pyversions/birdears.svg?style=flat)](https://pypi.python.org/pypi/birdears)
[![Waffle.io](https://img.shields.io/waffle/label/iacchus/birdears/in%20progress.svg?style=flat)](https://waffle.io/iacchus/birdears)
[![GitHub issues](https://img.shields.io/github/issues/iacchus/birdears.svg?style=flat&label=gh-issues)](https://github.com/iacchus/birdears/issues)
[![Documentation Status](https://readthedocs.org/projects/birdears/badge/?version=latest)](https://birdears.readthedocs.io/en/latest/?badge=latest)

<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Introduction](#introduction)
	- [birdears](#birdears)
	- [What is musical ear training](#what-is-musical-ear-training)
	- [Features](#features)
- [Installing](#installing)
	- [Installing the dependencies](#installing-the-dependencies)
		- [Arch Linux](#arch-linux)
	- [Installing birdears](#installing-birdears)
		- [In-depth installation](#in-depth-installation)
- [Running](#running)
- [Modes](#modes)
	- [melodic](#melodic)
		- [Description](#description)
		- [Command-line options](#command-line-options)
	- [harmonic](#harmonic)
		- [Description](#description)
		- [Command-line options](#command-line-options)
	- [dictation](#dictation)
		- [Description](#description)
		- [Command-line options](#command-line-options)
	- [instrumental](#instrumental)
		- [Description](#description)
		- [Command-line options](#command-line-options)
- [Loading from preset files](#loading-from-preset-files)
	- [Pre-made presets](#pre-made-presets)
		- [Pre-made presets description](#pre-made-presets-description)
	- [Creating new preset files](#creating-new-preset-files)
- [Contributing](#contributing)

<!-- /TOC -->

## Introduction


### birdears

`birdears` is a software written in Python 3 for ...

### What is musical ear training

It is a method..

### Features

* questions
* load from config file

## Installing

### Installing the dependencies

#### Arch Linux

```
sudo pacman -Syu sox python python-pip
```

### Installing birdears

`pip install --user --upgrade birdears`

#### In-depth installation

## Running

After installing just run:

`birdears --help`

## Modes

### melodic

#### Description

In this exercise birdears will play two notes, the tonic and the interval
melodically, ie., one after the other and you should reply which is the
correct distance between the two.

#### Command-line options

```
Usage: birdears melodic [options]

  Melodic interval recognition

Options:
  -m, --mode <mode>               Mode of the question.
  -t, --tonic <tonic>             Tonic of the question.
  -o, --octave <octave>           Octave of the question.
  -d, --descending                Whether the question interval is descending.
  -c, --chromatic                 If chosen, question has chromatic notes.
  -n, --n_octaves <n max>         Maximum number of octaves.
  -v, --valid_intervals <1,2,..>  A comma-separated list without spaces
                                  of valid scale degrees to be chosen for the
                                  question.
  -q, --user_durations <1,0.5,n..>
                                  A comma-separated list without
                                  spaces with PRECISLY 9 floating values. Or
                                  'n' for default              duration.
  -p, --prequestion_method <prequestion_method>
                                  The name of a pre-question method.
  -r, --resolution_method <resolution_method>
                                  The name of a resolution method.
  -h, --help                      Show this message and exit.

  In this exercise birdears will play two notes, the tonic and the interval
  melodically, ie., one after the other and you should reply which is the
  correct distance between the two.

  Valid values are as follows:

  -m <mode> is one of: major, dorian, phrygian, lydian, mixolydian, minor,
  locrian

  -t <tonic> is one of: A, A#, Ab, B, Bb, C, C#, Cb, D, D#, Db, E, Eb, F,
  F#, Fb, G, G#, Gb

  -p <prequestion_method> is one of: none, tonic_only, progression_i_iv_v_i

  -r <resolution_method> is one of: nearest_tonic, repeat_only
```

### harmonic

#### Description

In this exercise birdears will play two notes, the tonic and the interval
harmonically, ie., both on the same time and you should reply which is the
correct distance between the two.

#### Command-line options

```
Usage: birdears harmonic [options]

  Harmonic interval recognition

Options:
  -m, --mode <mode>               Mode of the question.
  -t, --tonic <note>              Tonic of the question.
  -o, --octave <octave>           Octave of the question.
  -d, --descending                Whether the question interval is descending.
  -c, --chromatic                 If chosen, question has chromatic notes.
  -n, --n_octaves <n max>         Maximum number of octaves.
  -v, --valid_intervals <1,2,..>  A comma-separated list without spaces
                                  of valid scale degrees to be chosen for the
                                  question.
  -q, --user_durations <1,0.5,n..>
                                  A comma-separated list without
                                  spaces with PRECISLY 9 floating values. Or
                                  'n' for default              duration.
  -p, --prequestion_method <prequestion_method>
                                  The name of a pre-question method.
  -r, --resolution_method <resolution_method>
                                  The name of a resolution method.
  -h, --help                      Show this message and exit.

  In this exercise birdears will play two notes, the tonic and the interval
  harmonically, ie., both on the same time and you should reply which is the
  correct distance between the two.

  Valid values are as follows:

  -m <mode> is one of: major, dorian, phrygian, lydian, mixolydian, minor,
  locrian

  -t <tonic> is one of: A, A#, Ab, B, Bb, C, C#, Cb, D, D#, Db, E, Eb, F,
  F#, Fb, G, G#, Gb

  -p <prequestion_method> is one of: none, tonic_only, progression_i_iv_v_i

  -r <resolution_method> is one of: nearest_tonic, repeat_only
```

### dictation

#### Description

In this exercise birdears will choose some random intervals and create a
melodic dictation with them. You should reply the correct intervals of the
melodic dictation.

#### Command-line options

```
Usage: birdears dictation [options]

  Melodic dictation

Options:
  -m, --mode <mode>               Mode of the question.
  -i, --max_intervals <n max>     Max random intervals for the dictation.
  -x, --n_notes <n notes>         Number of notes for the dictation.
  -t, --tonic <note>              Tonic of the question.
  -o, --octave <octave>           Octave of the question.
  -d, --descending                Wether the question interval is descending.
  -c, --chromatic                 If chosen, question has chromatic notes.
  -n, --n_octaves <n max>         Maximum number of octaves.
  -v, --valid_intervals <1,2,..>  A comma-separated list without spaces
                                  of valid scale degrees to be chosen for the
                                  question.
  -q, --user_durations <1,0.5,n..>
                                  A comma-separated list without
                                  spaces with PRECISLY 9 floating values. Or
                                  'n' for default              duration.
  -p, --prequestion_method <prequestion_method>
                                  The name of a pre-question method.
  -r, --resolution_method <resolution_method>
                                  The name of a resolution method.
  -h, --help                      Show this message and exit.

  In this exercise birdears will choose some random intervals and create a
  melodic dictation with them. You should reply the correct intervals of the
  melodic dictation.

  Valid values are as follows:

  -m <mode> is one of: major, dorian, phrygian, lydian, mixolydian, minor,
  locrian

  -t <tonic> is one of: A, A#, Ab, B, Bb, C, C#, Cb, D, D#, Db, E, Eb, F,
  F#, Fb, G, G#, Gb

  -p <prequestion_method> is one of: none, tonic_only, progression_i_iv_v_i

  -r <resolution_method> is one of: nearest_tonic, repeat_only
```

### instrumental

#### Description

In this exercise birdears will choose some random intervals and create a
melodic dictation with them. You should play the correct melody in you
musical instrument.

#### Command-line options

```
Usage: birdears instrumental [options]

  Instrumental melodic time-based dictation

Options:
  -m, --mode <mode>               Mode of the question.
  -w, --wait_time <seconds>       Time in seconds for next question/repeat.
  -u, --n_repeats <times>         Times to repeat question.
  -i, --max_intervals <n max>     Max random intervals for the dictation.
  -x, --n_notes <n notes>         Number of notes for the dictation.
  -t, --tonic <note>              Tonic of the question.
  -o, --octave <octave>           Octave of the question.
  -d, --descending                Wether the question interval is descending.
  -c, --chromatic                 If chosen, question has chromatic notes.
  -n, --n_octaves <n max>         Maximum number of octaves.
  -v, --valid_intervals <1,2,..>  A comma-separated list without spaces
                                  of valid scale degrees to be chosen for the
                                  question.
  -q, --user_durations <1,0.5,n..>
                                  A comma-separated list without
                                  spaces with PRECISLY 9 floating values. Or
                                  'n' for default              duration.
  -p, --prequestion_method <prequestion_method>
                                  The name of a pre-question method.
  -r, --resolution_method <resolution_method>
                                  The name of a resolution method.
  -h, --help                      Show this message and exit.

  In this exercise birdears will choose some random intervals and create a
  melodic dictation with them. You should play the correct melody in you
  musical instrument.

  Valid values are as follows:

  -m <mode> is one of: major, dorian, phrygian, lydian, mixolydian, minor,
  locrian

  -t <tonic> is one of: A, A#, Ab, B, Bb, C, C#, Cb, D, D#, Db, E, Eb, F,
  F#, Fb, G, G#, Gb

  -p <prequestion_method> is one of: none, tonic_only, progression_i_iv_v_i

  -r <resolution_method> is one of: nearest_tonic, repeat_only
```

## Loading from preset files

### Pre-made presets

Birdears cointains some pre-made presets in it's `presets/` subdirectory.

The study for beginners is recommended by following the numeric order of those files (000, 001, then 002 etc.)

#### Pre-made presets description

Maybe these things would go better in the readhedocs documentation.

### Creating new preset files

You can open the files cointained in birdears premade `presets/` folder to have
an ideia on how config files are made; it is simply the command line options
written in a form `toml` standard.


## Contributing

Those who want to contribute to this project can read [CONTRIBUTING.md](CONTRIBUTING.md).

* * *

```
readme should contain

[toc]

* introduction
  * feats

* screenshot(s)

* installing
  * dependencies
  * pip
    * what is pip
    * installing via pip
    * using a virtualenv
  * cloning the repository

* running

* modes
  * melodic
    * description
    * cli options (--help)
  * harmonic
    * description
    * cli options (--help)
  * dictation
    * description
    * cli options (--help)
  * instrumenetal
    * description
    * cli options (--help)

* loading from config file
  * presets

* * *

* development info
  as is in readme
  c
```
