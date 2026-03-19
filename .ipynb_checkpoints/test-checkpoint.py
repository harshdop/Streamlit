import streamlit as st


st.title("Do You have your Health Report?")
st.text("A quick 30 second analysis can prevent you from long term heart issues.")

with st.form("heart_analysis"):

    age = st.slider("What is you Age?", min_value = 10, max_value = 120)
    st.write('')

    sex_options =  {"Male" : 1, "Female" : 0}
    sex = st.selectbox("Select you Sex",list(sex_options.keys()))
    sex_numeric = sex_options[sex]
    st.write('')

    cp_options = {'Typical Angina': 0 , 'Atypical Angina' : 1, 'Non Typical Angina' : 2, 'Asymptomatic' : 3}
    cp = st.selectbox("Have you recently experienced any chest pain", list(cp_options.keys()))
    cp_numeric = cp_options[cp]
    st.write('')

    trestbps = st.slider("What is your Resting Blood Pressure? (mm/Hg)", min_value = 90, max_value = 200)

    st.write('')
    chol = st.slider("Select your Cholestrol Level?", min_value = 10, max_value = 1000)
    st.write('')

    fbs_options = {'>120 mm/Hg' : 0, '<120 mm/Hg' : 1}
    fbs = st.selectbox("Select your FBS Level?", list(fbs_options.keys()))
    fbs_numeric = fbs_options[fbs]
    st.write('')

    restecg_options = {'Normal' : 0, 'ST-T wave abnormality' : 1, 'Left ventricular hypertrophy' : 2}
    restecg = st.selectbox("Select your Resting ECG Level?", list(restecg_options.keys()))
    restecg_numeric = restecg_options[restecg]

    st.write('')

    thalach = st.slider("What is your Maximum Heart Rate", min_value = 30, max_value = 300)
    st.write('')

    exang_options = {'No' : 0 , 'Yes' : 1}
    exang = st.selectbox("Do you experience pain during exercise", list(exang_options.keys()))
    exang_numeric = exang_options[exang]
    st.write('')

    oldpeak = st.slider("Enter your Old Peak Value", min_value = 0.0, max_value = 100.0)
    oldpeak = oldpeak*10

    st.write('')

    slope_options = {'Upsloping' : 0, 'Downsloping' : 2, 'Flat' : 1}
    slope = st.selectbox("Select your Slope", list(slope_options.keys()))
    slope_numeric = slope_options[slope]
    st.write('')

    ca = st.selectbox("Select Number of Heart Vessels" ,[0,1,2,3,4] )



    thal_options = {'Unknown/Missing' : 0, 'Normal' : 1, 'Fixed Defect' : 2, 'Reversible Defect' : 3}
    thal = st.selectbox("Select your Health Report", list(thal_options.keys()))
    thal_numeric = thal_options[thal]

    submitted = st.form_submit_button("Submit")
    if submitted:
        user_input = [[age, sex_numeric, cp_numeric, trestbps, chol, fbs_numeric, restecg_numeric, thalach, exang_numeric, oldpeak, slope_numeric,ca, thal_numeric]]
        st.write(user_input)




