import pickle
import pandas as pd
import streamlit as st

file_path = 'xgboost_model.pkl'

with open(file_path, 'rb') as f:
    xg_loaded = pickle.load(f)


df_dict = pickle.load(open('df_dict.pkl', 'rb'))
df = pd.DataFrame(df_dict)

st.title("House Price Prediction Webapp :chart:")

bedrooms_ = st.selectbox("Select number of bedroom", df['bedrooms'].sort_values().unique())
bathrooms_ = st.selectbox("Select number of bathroom", df['bathrooms'].sort_values().unique())
sqftlot_ = st.number_input("Select a square footage of the lot", df['sqft_lot'].min(), df['sqft_lot'].max()) 
floors_ = st.selectbox("Select number of floors", df['floors'].sort_values().unique())

waterfront_ = st.selectbox("Select number of bedroom", ['yes', 'no'])
if waterfront_ == 'yes':
    waterfront_ = 1
else:
    waterfront_ = 0

view_= st.selectbox("Select in what rate the view you want", df['view'].sort_values().unique())
condition_ = st.selectbox("Select in what rate the conidition you want", ['Excellent', 'Above Average', 'Average', 'Below Average', 'Poor'])
if condition_ == 'Excellent':
    condition_ = 5
elif condition_ == 'Above Average':
    condition_ = 4
elif condition_ == 'Average':
    condition_ = 3
elif condition_ == 'Below Average':
    condition_ = 2
elif condition_ == 'Poor':
    condition_ = 1
 

sqft_basement_ = st.number_input("Select a square footage of the basement", df['yr_built'].min(), df['sqft_basement'].max()) 
yr_built_ = st.number_input("Select a square footage of the basement", df['sqft_basement'].min(), df['sqft_basement'].max()) 
lat_ = st.selectbox("Select latitude value", df['lat'].sort_values().unique()) 
long_ =	st.selectbox("Select longitude value", df['long'].sort_values().unique()) 
is_renovated_ = st.selectbox("Are you want renovated house", ['yes', 'no'])
if is_renovated_ == 'yes':
    is_renovated_ = 1
else:
    is_renovated_ = 0

data = {
    'bedrooms': [bedrooms_],
    'bathrooms': [bathrooms_],
    'sqft_lot': [sqftlot_],
    'floors': [floors_],
    'waterfront': [waterfront_],
    'view': [view_],
    'condition': [condition_],
    'sqft_basement': [sqft_basement_],
    'yr_built': [yr_built_],
    'lat': [lat_],
    'long': [long_],
    'is_renovated': [is_renovated_]
}

df_new = pd.DataFrame(data)

# Now you can predict using the loaded XGBoost model
y_prediction = xg_loaded.predict(df_new)

if st.button(f"**Predict Price**"):
    # Display the predicted price
    st.markdown(f"## Price of the house is : <span style='font-size:36px'>{y_prediction[0]}</span>", unsafe_allow_html=True)