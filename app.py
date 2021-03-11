import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import tensorflow.keras
from keras.models import Sequential
from keras.layers import Dense,Dropout
from sklearn.preprocessing import MinMaxScaler
import h5py
from tensorflow.keras.callbacks import ModelCheckpoint,CSVLogger
import pickle
import streamlit as st 

def main():
    avocado_df=pd.read_csv('data/avocado.csv')
    st.title('아보카도 가격 예측기 앱')
    st.dataframe(avocado_df.head())









if __name__=='__main__':
    main()
