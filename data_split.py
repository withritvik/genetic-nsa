import pandas as pd
import numpy as np

data = pd.read_csv("Fishers Iris Data.csv") # Reading the data
data.drop('Case', axis=1, inplace=True) # Dropping the Case column

# Splitting the data into train and test data in a 2:1 ratio
input_train_data = data.sample(frac=0.67, random_state=200) 
input_test_data = data.drop(input_train_data.index)

output_train_data = pd.DataFrame(0, index=np.arange(len(input_train_data)), columns=np.arange(3)) # Creating a dataframe of 0s for the output train data
output_test_data = pd.DataFrame(0, index=np.arange(len(input_test_data)), columns=np.arange(3)) # Creating a dataframe of 0s for the output test data

for i in range(len(input_train_data)):
    output_train_data.iloc[i][input_train_data.iloc[i][0]] = 1 # Assigning 1 to the column of the output train data corresponding to the class of the input train data
    if i < len(input_test_data):
        output_test_data.iloc[i][input_test_data.iloc[i][0]] = 1 # Assigning 1 to the column of the output test data corresponding to the class of the input test data

# Exporting the Split Data
input_train_data.to_csv("input_train_data.csv", index=False)
input_test_data.to_csv("input_test_data.csv", index=False)
output_train_data.to_csv("output_train_data.csv", index=False)
output_test_data.to_csv("output_test_data.csv", index=False)