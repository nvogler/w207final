# MIDS W207 Final Project
# Kaggle San Francisco Crime Classification Competition

https://www.kaggle.com/c/sf-crime

## Initial Features

## Engineered Features

- 'X' and 'Y' coordinates were trimmed to four digits of significance and paired to allow larger ‘plots’ of land to be accurately related
- Holidays were identified using the Pandas built-in calendar for US holidays

Principle Component Analysis was used initially for dimensionality reduction. Given the limited number of features relative to the sample size, significant reductions were not expected. PCA was used more or less to evaluate to quality of the additional features.

## Baseline Model
#### K-NN
Our baseline model for this analysis was a K-NN model with K=50.

## Additional Models
#### Logistic Regression
Final Parameters:

Optimizations and methods:
- L1 regularization for  dimensionality reduction
- L2 regularization using remaining features

#### Neural Network
Final Parameters:

Optimizations and methods:
- Keras (on top of TensorFlow) for NNs
- Sigmoid activation and ReLU based models
- Modeled with and without dropouts

#### Support Vector Machines

Final Parameters:

Optimizations and methods:
- Linear (not expecting great results) and non-linear kernels
- GridSearchCV for parameter optimization
#### Random Forests
Final Parameters:

Optimizations and methods:
- Boosting
- Bagging
- GridSearchCV for parameter optimization
    
    Matplotlib to visualize parameter optimization and identify knees
