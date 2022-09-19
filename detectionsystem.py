# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 17:26:10 2022

@author: kalul
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 17:23:22 2022

@author: kalul
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('D:/model deployment/trained_model.sav', 'rb'))

# Creating a function for prediction

def DDoS_Prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The data contains no DDoS Attacks'
    else:
      return 'The data contains DDoS Attacks'
  
def main():
    #Giving a title
    st.title('DDoS Attack Prediction Web App')
    
    # getting the input data from the user
    with st.form(key='columns_in_form'):
       c1, c2, c3, c4 = st.columns(4)
       with c1:
         pktcount = st.text_input('Packet Count')
         bytecount = st.text_input('Byte Count')
         dur = st.text_input('Duration')
       with c2:
         dur_nse = st.text_input('Duration of n_second')
         tot_dur = st.text_input('Total Duration')
         flows = st.text_input('Total flows')
       with c3:
         pktperflow = st.text_input('Packet per flow')
         byteperflow = st.text_input('Byte per flow')
         pktrate = st.text_input('Packet Rate')
       with c4:
         port_no = st.text_input('Port number')
         tx_bytes = st.text_input('Transmitted bytes')
         rx_bytes = st.text_input('Received bytes')
         tx_kbps = st.text_input('Transmitted kilobytes')
          
         submitButton = st.form_submit_button(label = 'DDoS Test Result')
    #code for prediction
 #code for prediction
       network = ''
 
 # creating a button for Prediction
 
    if st.button('DDoS Test Result'):
     network = DDoS_Prediction(float('pktcount', 'bytecount', 'dur',
    'dur_nsec', 'tot_dur', 'flows', 'pktperflow', 'byteperflow', 'pktrate', 'port_no', 'tx_bytes',
    'rx_bytes', 'tx_kbps'))
     
     
     st.success(network)
    
   
