import subprocess
import time

from .scale import ChromaticScale

class Sequence:
    """Register a Sequence of notes and/or chords.

    Attributes:
        elements (array_type): List of notes (strings) ou chords (list of
            strings) in this Sequence.
    """

    def __init__(self, elements, duration=2, delay=1.5, pos_delay=1):
        """Inits the Sequence with an array and sets the default times for
            playing / pausing the elements.

        Args:
            elements (array_type): List of elements in this sequence.
                (notes or chords)
            duration (float): Default playing time for each element in the
                sequence.
            delay (float): Default waiting time to play the next element
                in the sequence.
            pos_delay (float): Waiting time after playing the last element
                in the sequence.
        """

        self.duration = duration
        self.delay = delay
        self.pos_delay = pos_delay

        self.elements = list(elements)

    def append(self, elements):
        """Appends `elements` to Sequence.elements

        Args:
            elements (array_type): elements to be appended to the class.
        """
        self.elements.append(elements)

    def extend(self, elements):
        """Extends Sequence.elements with `elements`.

        Args:
            elements (array_type): elements extend the class with.
        """
        self.elements.extend(elements)

    def play(self):
        """Plays the Sequence elements of notes and/or chords and wait for
        `Sequence.pos_delay` seconds.
        """

        last_idx = len(self.elements) - 1

        for cur_idx,element in enumerate(self.elements):

            # lets leave the last element's delay for pos_delay:
            delay = self.delay if cur_idx != last_idx else 0

            if type(element) == str:
                self._play_note(element,delay=delay)
            elif type(element) == list:
                self._play_chord(element, delay=delay)

        if self.pos_delay:
            self._wait(self.pos_delay)

    # FIXME: implement octave here:
    def make_chord_progression(self, tonic, mode, degrees):
        """Appends triad chord(s) to the Sequence.

        Args:
            tonic(str): Tonic note of the scale.
            mode (str): Mode of the scale from which build the triads upon.
            degrees (array_type): List with integers represending the degrees
                of each triad.
        """
        scale = ChromaticScale(tonic=tonic)

        for degree in degrees:
            triad = scale.get_triad(mode=mode, degree=degree)
            self.elements.append(triad)

    def _play_note(self, note, duration=None, delay=None):
        """Plays a note.

        Args:
            note (str): The note and octave to be played. Eg.: 'C4'
            duration (float): Duration of the note in seconds.
            delay (float): Delay after the note in seconds.
        """
        # requires sox to be installed

        duration = self.duration if duration is None else duration
        delay = self.delay if delay is None else delay

        command = (
            "play -V1 -qn synth {duration} pluck {note}"
            " fade l 0 {duration} 2 reverb"
        ).format(note=note, duration=duration)

        try:
            subprocess.Popen(command.split())
        except:
            pass

        if delay:
            self._wait(delay)

    def _play_chord(self, chord, duration=None, delay=None):
        """Plays a chord.

        Args:
            chord (array_type): An array of pitches (notes and octaves)
                to be played, representing a chord. Eg.: ['C4', 'Eb4', 'G5']
            duration (float): Duration of the chord in seconds.
            delay (float): Delay after the chord in seconds.
        """

        duration = self.duration if duration is None else duration
        delay = self.delay if delay is None else delay

        chord_plucks = str()
        for note in chord:
            chord_plucks += " pluck {} ".format(note)

        command = (
            "play -V1 -qn synth {duration} {chord}"
            " fade l 0 {duration} 2 reverb"
        ).format(note=note, duration=duration, chord=chord_plucks)

        try:
            subprocess.Popen(command.split())
        except:
            pass

        if delay:
            self._wait(delay)

    def _wait(self, seconds):
        """Waits, ie., stops execution for some time.

        Args:
            seconds (float): Seconds to wait.
        """

        time.sleep(seconds)
