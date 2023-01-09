import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('model.pkl', 'rb'))


# creating a function for Prediction

def prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Negative'
    else:
      return 'Positive'
  
    
  
def main():
    def welcome(w):
        st.markdown(f'<p style="background-color:#f4c2c2 ;color:black;font-size:24px;border-radius:2%;text-align:center">{w}</p>', unsafe_allow_html=True)
    welcome("WELCOME ALL")

    def stream(s):
        st.markdown(f'<p style="background-color:tomato;padding:10px ;color:yellow;font-size:24px;border-radius:2%;text-align:center">{s}</p>', unsafe_allow_html=True)
    stream("STREAMLIT TIC TAC TOE ML APP")
    

    def head(url):
        st.markdown(f'<p style="background-color:#f4c2c2 ;color:black;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)

    head("(人◕‿◕) 𝔼𝕟𝕥𝕖𝕣 𝕧𝕒𝕝𝕦𝕖𝕤 𝕥𝕠 𝕔𝕙𝕖𝕔𝕜 (•◡•)")
    
    # getting the input data from the user
    
    top_left=float(st.number_input("top-left-square"))
    top_middle=float(st.number_input("top-middle-square"))
    top_right=float(st.number_input("top-right-square"))	
    middle_left=float(st.number_input("middle-left-square"))
    middle_middle=float(st.number_input("middle-middle-square"))
    middle_right=float(st.number_input("middle-right-square"))
    bottom_left=float(st.number_input("bottom-left-square"))
    bottom_middle=float(st.number_input("bottom-middle-square"))
    bottom_right=float(st.number_input("bottom-right-square"))
    
    
    # code for Prediction
    result = ''
    
    # creating a button for Prediction
    
    if st.button('PREDICT'):
        result = prediction([top_left,top_middle,top_right,middle_left,middle_middle,middle_right,bottom_left,bottom_middle,bottom_right])
        
    st.success(result)
    
    
if __name__ == '__main__':
    main()

def ty(url):
     st.markdown(f'<p style="background-color:pink;color:black;font-size:54px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)
ty('T♥H♥A♥N♥K♥ ♥Y♥O♥U')