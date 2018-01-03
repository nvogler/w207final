# MIDS W207 Final Project
# Kaggle San Francisco Crime Classification Competition

https://www.kaggle.com/c/sf-crime

## Initial Features
- Category     -Category of the crime incident. This is the target variable for prediction
- Dates        -Timestamp of the crime incident
- DayOfWeek    -The day of the week
- PdDistrict   -Name of the Police Department District
- Address      -The approximate street address of the crime incident 
- X            -Longitude
- Y            -Latitude

## Engineered Features

- 'X' and 'Y' coordinates were trimmed to four digits of significance and paired to allow larger ‘plots’ of land to be accurately related
- Holidays were identified using the Pandas built-in calendar for US holidays
- Dates feature was broken into the following:
  -- Hour of the Day
  -- Day of the week (dummy variable)
  -- Week of the year 

Matplotlib to visualize parameter optimization and identify knees
   
## Baseline Model
#### K-NN
Our baseline model for this analysis was a K-NN model with K=50.

## Additional Models
#### Neural Network
Optimizations and methods:
- Keras (on top of TensorFlow) for NNs
- Sigmoid activation and ReLU based models
- Modeled with and without dropouts

#### Random Forests
Final Parameters:

Optimizations and methods:
- Boosting
- Bagging
- GridSearchCV for parameter optimization
    

