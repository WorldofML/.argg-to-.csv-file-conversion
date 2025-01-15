import pandas as pd
from scipy.io import arff

data = arff.loadarff('.arff file directory')
train = pd.DataFrame(data[0])
train.to_csv('output_directory\output.csv', index=False)
