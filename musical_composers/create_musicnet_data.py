import csv, os

# This file takes the raw data accessed from Kaggle (https://www.kaggle.com/datasets/imsparsh/musicnet-dataset) and converts it into a csv file usable
# for machine learning. 

INSTRUMENT = 'Solo Piano' # to sort by muscial instrument
DIRECTORY = 'musicnet/musicnet/train_labels'
BEATS_PER_MEASURE = 4 # to account for length of individual notes
MAX_PER_COMPOSER = 10000 # used to cap number of works represented per composer in the dataset

# Create composer and instrument dictionary
composers = {}
instruments = {}

with open('musicnet_metadata.csv') as f:
    reader = csv.reader(f)
    heading = next(reader)
    for line in reader:
        composers[int(line[0])] = line[1]
        instruments[int(line[0])] = line[4]
    f.close()

# Create composer dictionary

key = {
    'Schubert':0,
    'Mozart':1,
    'Dvorak':2,
    'Cambini':3,
    'Haydn':4,
    'Brahms':5,
    'Faure':6,
    'Ravel':7,
    'Bach':8,
    'Beethoven':9
}

count = {n:0 for n in range(10)} # To control for frequency of each composer in the final dataset

# Create the first row of our csv file containing the labeling of each column
labels = []
labels.append('composer')
for i in range(784):
    s = 'note_' + str(i)
    labels.append(s)


res = []
res.append(labels)
for filename in os.listdir(DIRECTORY):
    if filename.endswith('.csv'):
        if instruments[int(filename[:-4])] != INSTRUMENT:
            continue
        data = [key[composers[int(filename[:-4])]]] # First column contains number 0-9 representing the composer of the piece
        with open(os.path.join(DIRECTORY, filename)) as f:
            reader = csv.reader(f)
            heading = next(reader)
            for line in reader:
                for _ in range(round(BEATS_PER_MEASURE*float(line[5]))):
                    data.append(int(line[3]))
                    if len(data) == 785 and count[key[composers[data[0]]]] < MAX_PER_COMPOSER:
                        res.append(data.copy())
                        data = [int(filename[:-4]) % 12]
                        count[key[composers[data[0]]]] += 1
            f.close()
    

with open('composer_data/musicnet_data.csv', 'w', newline = '') as d:
    writer = csv.writer(d)
    writer.writerows(res)

    d.close()










