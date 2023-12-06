#!/usr/bin/env python
# coding: utf-8

# Import everything at one place

# In[26]:


import numpy as np
import matplotlib.pylab as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import metrics
import sklearn


# # First, load the dataset, 'y2020_temp_precip_percent_satisfactory.csv'

# In[27]:


# y2020_temp_precip_percent_satisfactory.csv file can be stored from github or like below
y2020_temp_precip_percent_satisfactory = pd.read_csv('~/project/y2020_temp_precip_percent_satisfactory.csv') 
y2020_temp_precip_percent_satisfactory.head()


# # Prepare data:
# 
# Focusing on 'Trip Distance' variable, guessing that the feature variables 'Average_Temperature', 'Tot_Precip', 'Percent.Satisfactory', 'Vehicle.Type' affect target variable 'Trip Distance' for ALL 3 types of vehicles OR only for each type of veicle at a time? Can "vehicle type" be a feature variable"
# 
# A "sweet spot" of 'Trip Duration' to indicate "0"(short distance/less favorable) and "1"(long distance/more favorable) is set to 900 meters in this case
# 

# In[34]:


#create a new column 'favorability', a binary variable:
y2020_temp_precip_percent_satisfactory['favorability'] = np.where(y2020_temp_precip_percent_satisfactory['Trip.Duration'] >= 200, 1, 0)

y2020_temp_precip_percent_satisfactory.head()


# In[44]:


# Data cleaning and feature selection
features = ['Trip.Duration', 'Trip.Distance']
X = y2020_temp_precip_percent_satisfactory[features]
y = y2020_temp_precip_percent_satisfactory['Vehicle.Type']


# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# # Training
# Using Neural Network and Random Forest Classififiers to traine datasets: 

# In[46]:


from sklearn.ensemble import RandomForestClassifier

# Train the Random Forest model, CHECK TO SEE WHICH MAX_DEPTH TO USE??????????????????????????????????????????????????
rf_model = RandomForestClassifier(max_depth=6)
rf_model.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)  

print(rf_predictions)


# In[47]:


from sklearn.neural_network import MLPClassifier
# Train the Neural Network model
nn_model = MLPClassifier()
nn_model.fit(X_train, y_train)
nn_predictions = nn_model.predict(X_test) 

print(nn_predictions)


# # Model Evaluation
# sklearn.metrics.recall_score
# sklearn.metrics.precision_score
# confusion matrix??

# In[57]:


# Evaluate the performance using sklearn.metrics.accuracy_score:
from sklearn.metrics import accuracy_score

rf_accuracy = accuracy_score(y_test, rf_predictions)
nn_accuracy = accuracy_score(y_test, nn_predictions)

print('Random forest''s accuracy score: ', rf_accuracy)
print('Neural Network''s accuracy score: ', nn_accuracy)


# In[59]:


# Evaluate the performance using sklearn.metrics.precision_score:
from sklearn.metrics import recall_score

rf_precision_score = recall_score(y_test, rf_predictions, average='micro')
nn_precision_score = recall_score(y_test, nn_predictions, average='micro')

print('Random forest''s recall score: ', rf_precision_score)
print('Neural Network''s recall score: ', nn_precision_score)


# In[55]:


# using confusion matrix for Random Forest model: 
disp_rf = metrics.plot_confusion_matrix(rf_model, X_test, y_test, colorbar=False)
disp_rf.figure_.suptitle("Confusion Matrix for Random Forest model")
print(f"Confusion matrix:\n{disp_rf.confusion_matrix}")

plt.show()


# In[56]:


# using confusion matrix Neural Network model:
disp_nn = metrics.plot_confusion_matrix(nn_model, X_test, y_test, colorbar=False)
disp_nn.figure_.suptitle("Confusion Matrix for Neural Network classifier")
print(f"Confusion matrix:\n{disp_nn.confusion_matrix}")

plt.show()


# In[54]:


# using confusion matrix Logistic regression model:
disp_lr = metrics.plot_confusion_matrix(LR_classifier, X_test, y_test, colorbar=False)
disp_lr.figure_.suptitle("Confusion Matrix for Logistic regression model")
print(f"Confusion matrix:\n{disp_lr.confusion_matrix}")

plt.show()


# In[ ]:




