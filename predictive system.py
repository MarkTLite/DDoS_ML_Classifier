# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('D:/model deployment/trained_model.sav', 'rb'))


input_data = (0.2,-0.7,-0.86,1.9,1.75,2.8,0.587,0.51,0.76,-0.456,-1.54,0.98,0.78,0,1,0,0)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The data contains no DDoS Attacks ')
else:
  print('The data contains DDoS Attacks')