"""
    Variables picked for mapping notes for selected key and scale
"""
CHROMATIC_NOTES = {'C': 1,
                   'C#': 2,
                   'D': 3,
                   'D#': 4,
                   'E': 5,
                   'F': 6,
                   'F#': 7,
                   'G': 8,
                   'G#': 9,
                   'A': 10,
                   'A#': 11,
                   'B': 12}
NOTES_IN_SCALE = {
    "major": [1, 3, 5, 6, 8, 10, 12],
    "minor": [1, 3, 4, 6, 8, 9, 11],
    "blues": [1, 4, 6, 7, 8, 11]
}

PROGRESSION = {
    "major": {
        "chords": ["major", "minor", "minor", "major", "major", "minor", "diminished"],
        "notes": [[1, 3, 5], [2, 4, 6], [3, 5, 7], [1, 4, 6], [2, 5, 7], [1, 3, 6], [2, 4, 7]]
    },
    "minor": {
        "chords": ["minor", "diminished", "major", "minor", "minor", "major", "major"],
        "notes": [[1, 3, 5], [2, 4, 6], [3, 5, 7], [1, 4, 6], [2, 5, 7], [1, 3, 6], [2, 4, 7]]
    }
}
