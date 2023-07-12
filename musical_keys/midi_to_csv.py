import pandas as pd
import py_midicsv as pm
import os

source =  'musical_keys/midi'
dest = 'musical_keys/csv'

for file in os.listdir(source):
    path = os.path.join(source, file)
    try: 
        with open(path, "rb") as f:
            csv_string = pm.midi_to_csv(f)

            df = pd.DataFrame(csv_string)
            df.columns = ['0']

            new = df['0'].str.split(',', expand = True)
            destination = os.path.join(dest, file[:-4] + 'csv')
            new.to_csv(destination, index=False)
    except:
        pass
        
    f.close()




