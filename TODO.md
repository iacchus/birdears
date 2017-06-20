# birdears

## TODO

### Classes

Classes:

**[maybe] Make a class for response (to be used by question.check\_question)**

### Documentation


### Features

MAKE SOMEHING FOR IMPROVISING ON PRE-MADE HARMONIES**

**plugins/extensions, easy way of users extending the software by using the api,
maybe providing frontend tools**

think on an interface, or a well written api that allows many interfaces:

* ~~cli (maybe centering things)~~ ✓;
* **tui (urwid);**
* **gui (kivy)**

**track correct/wrong answers by type, mode, tonic, date etc, maybe using sqlite3
db so that the user can track it's progress.** ~~(https://dataset.readthedocs.io/en/latest/)~~
(https://pypi.python.org/pypi/sqlitedict), the other has heavy dependencies.

Question base should accept aarguments intelligently, for example, ~~`tonic` can
be a string or a list~~, or a tuple, so he can sort one of the elements as tonic;
~~`octave` can be int or tuple, so that the octave will be chosen randomly by that
range~~, etc. This will give us tools to load questions from config files.

### Refactoring

**We should use some kind of config object to configure exercises, as they have
an extensive number of parameters and there are more to come.**

note: maybe you'd find this useful https://gist.github.com/rxaviers/7360908

**Encapsulate birdears.interfaces.commandline in a class.**

**We should use some random() method inside Interval to select some random
interval or namethe class as RandomInterval. First option is best and we should
be able to generate not random interval using Interval class.**

**Maybe register question classes in a global.**

**Maybe sequence can contain sequences play(): if type==sequence, then play()**

**Refactor API so that inside an interface (eg., the GUI) we don't have stuff
redunant to it (eg., commandline presentation on GUI when it imports the API)**

**GUI: we should do one widget for each type of exercise.**

**we can make sequence not musical agnostics, ie., containing only strings for notes
and chords, but alo semitones so that play() can send this for threaded UI
callbacks.**

### Etc

