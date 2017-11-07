import sys, os
import pandas
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

header = ["ID", "ARSON", "ASSAULT", "BAD CHECKS", "BRIBERY", "BURGLARY", "DISORDERLY CONDUCT", "DRIVING UNDER THE INFLUENCE", "DRUG/NARCOTIC", "DRUNKENNESS", "EMBEZZLEMENT", "EXTORTION", "FAMILY OFFENSES", "FORGERY/COUNTERFEITING", "FRAUD", "GAMBLING", "KIDNAPPING", "LARCENY/THEFT", "LIQUOR LAWS", "LOITERING", "MISSING PERSON", "NON-CRIMINAL", "OTHER OFFENSES", "PORNOGRAPHY/OBSCENE MAT", "PROSTITUTION", "RECOVERED VEHICLE", "ROBBERY", "RUNAWAY", "SECONDARY CODES", "SEX OFFENSES FORCIBLE", "SEX OFFENSES NON FORCIBLE", "STOLEN PROPERTY", "SUICIDE", "SUSPICIOUS OCC", "TREA", "TRESPASS", "VANDALISM", "VEHICLE THEFT", "WARRANTS", "WEAPON LAWS"]

# Load training data
df = pandas.read_csv("train.csv")

# Binarize with dummy variables
temp_df = df[['DayOfWeek', 'PdDistrict']]
temp_df = pandas.get_dummies(temp_df)

# Format datetime
time_df = pandas.to_datetime(df['Dates']).dt.hour

# Join columns
temp_df = pandas.DataFrame(df['Category']).join(pandas.DataFrame(time_df)).join(temp_df)

# Split into data/labels, train/dev
train_data = temp_df[temp_df.columns.difference(['Category'])]
train_labels = temp_df['Category']

#dev_data = temp_df[temp_df.columns.difference(['Category'])][-5000:]
#dev_labels = temp_df['Category'][-5000:]

# Load test data
df_test = pandas.read_csv("test.csv")

# Binarize with dummy variables
temp_df = df_test[['DayOfWeek', 'PdDistrict']]
temp_df = pandas.get_dummies(temp_df)

# Format datetime
time_df = pandas.to_datetime(df_test['Dates']).dt.hour

# Join columns
test_data = pandas.DataFrame(time_df).join(temp_df)

# Clean
df = temp_df = time_df = None 

# Train KNN Classifier
neigh = KNeighborsClassifier(n_neighbors=5)
# Fit
neigh.fit(train_data, train_labels) 
# Predict
result = neigh.predict(test_data)
result = pandas.DataFrame(result)
result = pandas.get_dummies(result, prefix='', prefix_sep='')
# Add null categories to make kaggle happy
result = result.T.reindex(header).T.fillna(0)

result.to_csv("output_knn.csv", compression='gzip', chunksize=1000)

#neigh.score(dev_data, dev_labels)

# Train RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)
# Fit
rfc.fit(train_data, train_labels)
# Predict
#rfc.score(dev_data, dev_labels)

#result = rfc.predict(test_data)
#result = pandas.DataFrame(result)
#result = pandas.get_dummies(result)

#result.to_csv("output_rfc.csv", compression='gzip', chunksize=1000)


