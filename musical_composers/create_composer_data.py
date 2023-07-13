import csv, os

# This file takes the raw data accessed from Kaggle (https://www.kaggle.com/datasets/vincentloos/classical-music-midi-as-csv) and converts it into a csv file usable
# for machine learning. 

# To control for frequency of each composer in the final dataset

DIRECTORY = 'dataset2/midi/ALL'

count = {
    'Bach':0,
    'Scarlatti':0,
    'Mozart':0,
    'Beethoven':0,
    'Chopin':0,
    'Schubert':0,
    'Vivaldi':0,
    'Haendel':0,
    'Haydn':0,
    'Schumann':0
}

# Create composer dictionary
key = {
    'Bach':0,
    'Scarlatti':1,
    'Mozart':2,
    'Beethoven':3,
    'Chopin':4,
    'Schubert':5,
    'Vivaldi':6,
    'Haendel':7,
    'Haydn':8,
    'Schumann':9
}

# Create the first row of our csv file containing the labeling of each column
labels = []
labels.append('composer')
for i in range(784):
    s = 'time_' + str(i)
    labels.append(s)

res = []
res.append(labels)
for filename in os.listdir(DIRECTORY):
    if filename.endswith('.csv'):
        name = filename.split(' - ')[0]
        if name not in key:
            continue
        if count[name] >= 50:
            continue
       
        data = [key[name]]
        with open(os.path.join(DIRECTORY, filename)) as f:
            reader = csv.reader(f)
            heading = next(reader)
            idx = 0
            for i, val in enumerate(heading):
                if val == 'time':
                    idx = i
            for line in reader:
                if line[1] != 'note_on':
                    continue
                data.append(int(line[idx]))
            if len(data) >= 785:
                res.append(data[:785])
                count[name] += 1
            f.close()

with open('composer_data/composer_data.csv', 'w', newline = '') as d:
    writer = csv.writer(d)
    writer.writerows(res)

    d.close()




