import numpy as np

# Is it bad i lowk had to search ts up

NOTE_NAMES = [
    'C', 'C#', 'D', 'D#', 'E', 'F', 'F#',
    'G', 'G#', 'A', 'A#', 'B'
    ]
    
    # Maybe I'll change it to flats but rn it's fine

def frequency_to_note_name(frequency):
    
    """ Converts a frequency to a note name. """
    if frequency <= 0 or frequency> 4186 or np.isinf(frequency) or np.isnan(frequency):
        return None, 0
    # If there is no frequency obv theres no note lol
    
    semitones = 12 * np.log2(frequency/440.0) # Calculate the number of semitones from A4 (440 Hz)
    nearest = round(semitones) # Rounding to nearest semitone
    cents_off = (semitones - nearest) * 100 # Calculate cents off from the nearest semitone
    note_index = int(semitones % 12) # Calculate the index for the note name
    # octave = (nearest + 9) // 12 + 4 # Calculate the octave number
    note_name = NOTE_NAMES[note_index] # Combine note name 
    
    return note_name, cents_off

""" I never use octaves ever so there is seriously no point """