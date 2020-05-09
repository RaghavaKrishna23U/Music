"""
    This code helps musicians list the notes and chords(triads)
    for any choice of Key in the major and minor scales
"""
import sys

from music_notes import PROGRESSION, NOTES_IN_SCALE, CHROMATIC_NOTES


def rearrange_chromatic(key, required_scale):
    """
        Parses the key and scale and maps it to numerical entities.
        Returns the chromatic with the selected key as note 1
    """
    new_chromatic = {}
    scale_local = NOTES_IN_SCALE[required_scale]
    temp_iterator = root_note_position = CHROMATIC_NOTES.get(key)
    out_of_scale = 12 - root_note_position
    count = 1

    while temp_iterator <= 12:
        root_note = \
            [note for note, position in CHROMATIC_NOTES.items() if position == temp_iterator][0]
        new_chromatic[root_note] = count
        count += 1
        temp_iterator += 1

    for i in range(1, root_note_position, 1):
        root_note = [note for note, position in CHROMATIC_NOTES.items() if position == i][0]
        new_chromatic[root_note] = i + out_of_scale + 1
        count += 1

    # print(transposed_chromatic)
    return new_chromatic, scale_local


def list_notes_in_scale(new_chromatic, scale_local):
    """
        Uses the new chromatic scale and lists the notes
        associated in the key and scale
    """
    list_of_notes = []
    for note_number in scale_local:
        note = [note for note, position in new_chromatic.items() if position == note_number][0]
        list_of_notes.append(note)
    return list_of_notes


def chord_progression(scale_local, notes_local):
    """
        Parses the dictionary to find the chords
        and notes in the chords for the scale
    """
    chord_sequences = PROGRESSION[scale_local]['chords']
    chord_notes = PROGRESSION[scale_local]['notes']
    number_of_chords = len(chord_sequences)
    print("Here is the list of chords you can play: ")
    for i in range(0, number_of_chords):
        print(" %s %s has notes: %s, %s, %s" % (notes_local[i],
                                                chord_sequences[i],
                                                notes_local[chord_notes[i][0] - 1],
                                                notes_local[chord_notes[i][1] - 1],
                                                notes_local[chord_notes[i][2] - 1]))


if __name__ == '__main__':
    KEY = str(sys.argv[1]).upper()
    INPUT_SCALE = str(sys.argv[2]).lower()
    TRANSPOSED, SCALE = rearrange_chromatic(KEY, INPUT_SCALE)
    NOTES = list_notes_in_scale(TRANSPOSED, SCALE)
    print('The notes in %s %s are: %s' % (KEY, INPUT_SCALE, str(NOTES)))
    chord_progression(INPUT_SCALE, NOTES)
