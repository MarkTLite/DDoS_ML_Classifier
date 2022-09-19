# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 10:28:48 2022

@Author: Kalulu Waako 
"""
from random import randint
import numpy as np
import pickle
import streamlit as st

# Creating a function for prediction
def DDoS_Prediction(input_data):

    # loading the saved model
    loaded_model = pickle.load(open('trained_model.sav', 'rb'))
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
    col1, col2, col3 = st.columns(3)
    
    # getting the input data from the user
    with col1:
      pktcount = st.text_input('Packet Count')
      bytecount = st.text_input('Byte Count')
      dur = st.text_input('Duration')
      dur_nsec = st.text_input('Duration of n_second')

    with col2:
      tot_dur = st.text_input('Total Duration')
      flows = st.text_input('Total flows')
      pktperflow = st.text_input('Packet per flow')
      byteperflow = st.text_input('Byte per flow')

    with col3:
      pktrate = st.text_input('Packet Rate')
      port_no = st.text_input('Port number')
      tx_bytes = st.text_input('Transmitted bytes')
      rx_bytes = st.text_input('Received bytes')
      tx_kbps = st.text_input('Transmitted kilobytes')
    
    #code for prediction
    network = ''
    
    # creating a button for Prediction
    if st.button('DDoS Test Result'):
        network = DDoS_Prediction(
          [float(pktcount),float(bytecount),float(dur), float(dur_nsec),float(tot_dur),
           float(flows), float(pktperflow), float(byteperflow),float(pktrate),
           float(port_no), float(tx_bytes),float(rx_bytes), float(tx_kbps), 
           float(randint(0,1)), float(randint(0,1)), float(randint(0,1)), float(randint(0,1))])
        
    st.success(network)

if __name__ == '__main__':
    main()
