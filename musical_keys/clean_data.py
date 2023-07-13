import pandas as pd
import os

# Extracts the musical key and notes from the converted csv file.
def extract(file, key_mapping):
    df = pd.read_csv(file)
    df.columns = [i for i in range(len(df.columns))]

    notes = df[df[2] == ' Note_on_c']
    key = df[df[2] == ' Key_signature']

    a, b = int(key[3].tolist()[0]), key[4].tolist()[0].strip()[1:-1]

    key_sig = key_mapping[b][a]
    return [key_sig] + notes[4].tolist()

# Creates a csv containg the notes/musical key of all our midi files
def clean():

    key_mapping = {'major':{
        0: 0, # C major
        1: 1, # C# Major
        2: 2, # D Major
        3: 3, # D# Major
        4: 4, # E Major
        5: 5, # F Major
        6: 6, # F# Major
        7: 7, # G Major
        -1: 11, # B Major
        -2: 10, # A# Major
        -3: 9, # A Major
        -4: 8, # G# major
        -5: 7, # G Major
        -6: 6, # F# Major
        -7: 5 # F Major
    }, 
    'minor': {
        0: 12, # C minor
        1: 13, # C# Minor
        2: 14, # D Minor
        3: 15, # D# Minor
        4: 16, # E Minor
        5: 17, # F Minor
        6: 18, # F# Minor
        7: 19, # G Minor
        -1: 23, # B Minor
        -2: 22, # A# Minor
        -3: 21, # A Minor
        -4: 20, # G# minor
        -5: 19, # G Minor
        -6: 18, # F# Minor
        -7: 17 # F Minor
    }}

    data = []
    invalid = 0

    for file in os.listdir('csv'):
        try:
            path = os.path.join('csv', file)
            data.append(extract(path, key_mapping))
        except:
            invalid += 1
            pass

    max_len = max(len(row) for row in data)
    min_len = min(len(row) for row in data)

    padded_data = [row + [None] * (max_len - len(row)) for row in data]

    df = pd.DataFrame(padded_data)
    #print('Invalid files: ', invalid)
    #print('Minimum Length: ', min_len)

    df.to_csv('clean_data/keys.csv', index = False, header = False)
    return