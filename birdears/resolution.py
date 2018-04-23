from . import MAX_SEMITONES_RESOLVE_BELOW

from .interval import Interval

from .scale import DiatonicScale
from .scale import ChromaticScale

from .sequence import Sequence

from .note_and_pitch import get_pitch_by_number
from .note_and_pitch import Chord

from functools import wraps

RESOLUTION_METHODS = {}
# http://stackoverflow.com/questions/5910703/howto-get-all-methods-of-a-pyt\
# hon-class-with-given-decorator
# http://stackoverflow.com/questions/5707589/calling-functions-by-array-ind\
# ex-in-python/5707605#5707605


def register_resolution_method(f, *args, **kwargs):
    """Decorator for resolution method functions.

    Functions decorated with this decorator will be registered in the
    `RESOLUTION_METHODS` global dict.
    """

    @wraps(f)
    def decorator(*args, **kwargs):
        return f(*args, **kwargs)

    RESOLUTION_METHODS.update({f.__name__: f})

    return decorator


class Resolution:
    """This class implements methods for different types of question
    resolutions.

    A resolution is an answer to a question. It aims to create a mnemonic on
    how the inverval resvolver to the tonic.
    """

    def __init__(self, method, question):
        """Inits the resolution class.

        Args:
            method (str): The method used in the resolution.
            question (obj): Question object from which to generate the
            resolution sequence.
        """

        self.METHOD = RESOLUTION_METHODS[method]
        self.question = question

    def __call__(self, *args, **kwargs):
        """Calls the resolution method and pass arguments to it.

        Returns a `birdears.Sequence` object with the resolution generated by
        the.method.
        """
        return self.METHOD(question=self.question, *args, **kwargs)


@register_resolution_method
def nearest_tonic(question):
    """Resolution method that resolve the intervals to their nearest tonics.

    Args:
        question (obj): Question object from which to generate the
            resolution sequence. (this is provided by the `Prequestion` class
            when it is `__call__`ed)
    """

    # global DIATONIC_MODES, MAX_SEMITONES_RESOLVE_BELOW

    # mode = question.mode
    tonic_pitch = question.tonic_pitch
    scale = question.scale
    random_pitch = question.random_pitch

    duration = question.durations['resol']['duration']
    delay = question.durations['resol']['delay']
    pos_delay = question.durations['resol']['pos_delay']
    
    # this function will receive: tonic, scale and random_pitch (which may be
    # chromatic, ie., not in `scale`)

    # scale = DiatonicScale(tonic='C', mode='major', octave=4, n_octaves=2,
    # descending=True) # this comes from Jupyter testing
    
    #tonic_pitch = scale[0]
    #random_pitch = choice(scale)
    
    # lets create an scale with same tonic, in the octave of the random_pitch
    scale_random_pitch = DiatonicScale(tonic=tonic_pitch.note,
                                       octave=random_pitch.octave, n_octaves=1)
     
    
    interval = Interval(tonic_pitch, random_pitch)
    
    semitones = interval['distance']['semitones']
    
    direction = -1 if (semitones <= MAX_SEMITONES_RESOLVE_BELOW) else 1
    
    resolution = []
    
    if random_pitch not in scale_random_pitch:  # random_pitch is chromatic
        resolution.append(random_pitch)
        #  next ones above or below are in the diatonic for sure, then:
        nearest_diatonic_pitch = \
            get_pitch_by_number(int(random_pitch)+direction)
    else:
        nearest_diatonic_pitch = random_pitch  # random_pitch is diatonic
        
    print(str(random_pitch))
    print(str(nearest_diatonic_pitch))
    print(int(random_pitch))
    
    nearest_tonic_index = 0 if semitones <= MAX_SEMITONES_RESOLVE_BELOW else -1
    nearest_tonic_pitch = scale_random_pitch[nearest_tonic_index]
    
    tonic_index = scale_random_pitch.index(nearest_tonic_pitch)
    
    nearest_diatonic_pitch_index = \
        scale_random_pitch.index(nearest_diatonic_pitch)
    
    random_pitch_index = nearest_diatonic_pitch_index
    
    ohslice = slice(min(tonic_index, random_pitch_index), max(tonic_index,
                    nearest_diatonic_pitch_index)+1)
        
    resolution = scale_random_pitch[ohslice][::direction]
    
    if question.is_harmonic:
        resolution_harmonic = []
        
        for item in resolution:
            resolution_harmonic.append(Chord(tonic, item))
        
        resolution = resolution_harmonic
    
    # resolution
    return Sequence(elements=resolution, duration=duration, delay=delay,
                    pos_delay=pos_delay)


@register_resolution_method
# FIXME : it should both play preq and question
def repeat_only(question):
    """Resolution method that only repeats the sequence elements with given
    durations.

    Args:
        question (obj): Question object from which to generate the
            resolution sequence. (this is provided by the `Prequestion` class
            when it is `__call__`ed)
    """
    elements = question.question.elements
    
    duration = question.durations['resol']['duration']
    delay = question.durations['resol']['delay']
    pos_delay = question.durations['resol']['pos_delay']

    sequence_list = Sequence(elements, duration=duration, delay=delay,
                             pos_delay=pos_delay)

    return sequence_list
