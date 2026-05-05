# Name: Bryan Sandor
# Class: Stat 554
# Title: Final Project

# Read in some data into a pandas dataframe to sample from
import pandas as pd
finalPowerDF = pd.read_csv("power_streaming_data.csv")

# Now a for loop to sample a few rows and output them to a data set
# Put a pause of 20 seconds in as well
import numpy as np
import time

for i in range(0, 20):
    # randomly sample a few rows
    samplePowerDF = finalPowerDF.loc[np.random.randint(finalPowerDF.shape[0], size = 5)]
    # write the sample to a new .csv file in the desired folder
    samplePowerDF.to_csv("finalProjStream/power_streaming_data" + str(i) + ".csv", index = False, header = False)
    # pause for 20 seconds before the next iteration
    time.sleep(20)