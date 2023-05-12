import csv, os

# This file takes the raw data accessed from Kaggle (https://www.kaggle.com/datasets/vincentloos/classical-music-midi-as-csv) and converts it into a csv file usable
# for machine learning. 

# Create dictionary mapping every muscial key to an integer from 0-23

DIRECTORY = 'dataset2/midi/ALL'

key = {
    'A':9,
    'B':11,
    'C':0,
    'D':2,
    'E':4,
    'F':5,
    'G':7,
    'A#':10,
    'B#':0,
    'C#':1,
    'D#':3,
    'E#':5,
    'F#':6,
    'G#':8,
    'Ab':8,
    'Bb':10,
    'Cb':11,
    'Db':1,
    'Eb':3,
    'Fb':4,
    'Gb':6,
    'Am':21,
    'Bm':23,
    'Cm':12,
    'Dm':14,
    'Em':16,
    'Fm':17,
    'Gm':19,
    'A#m':22,
    'B#m':12,
    'C#m':13,
    'D#m':15,
    'E#m':17,
    'F#m':18,
    'G#m':20,
    'Abm':20,
    'Bbm':22,
    'Cbm':23,
    'Dbm':13,
    'Ebm':15,
    'Fbm':16,
    'Gbm':18,
}

# Create the first row of our csv file containing the labeling of each column
labels = []
labels.append('key')
for i in range(784):
    s = 'note_' + str(i)
    labels.append(s)

res = []
res.append(labels)
for filename in os.listdir(DIRECTORY):
    if filename.endswith('.csv'):
        data = []
        with open(os.path.join(DIRECTORY, filename)) as f:
            reader = csv.reader(f)
            heading = next(reader)
            k_idx = 0
            n_idx = 0
            for i, val in enumerate(heading):
                if val == 'key':
                    k_idx = i
                if val == 'note':
                    n_idx = i
            for line in reader:
                if line[1] == 'key_signature':
                    data.append(key[line[k_idx]])
                    break
            for line in reader:
                if line[1] != 'note_on':
                    continue
                data.append(int(line[n_idx]) % 12)
            if len(data) >= 785:
                res.append(data[:785])
            f.close()

with open('key_data.csv', 'w', newline = '') as d:
    writer = csv.writer(d)
    writer.writerows(res)

    d.close()




