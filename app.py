
import streamlit as st
import pandas as pd
import joblib
import json

st.set_page_config(
    page_title="Laptop Price Predictor",
    layout="centered",
    initial_sidebar_state="expanded"
)


model = joblib.load("laptop_model.pkl")

with open("model_info.json") as f:
    metadata = json.load(f)

accuracy = metadata["r2_score"]


st.markdown("""
<style>
body {background-color: #0E1117; color: white;}
</style>
""", unsafe_allow_html=True)


st.title("💻 Laptop Price Prediction App")
st.markdown("Predict laptop price using Machine Learning")

st.subheader(f"📊 Model Accuracy: {accuracy}%")


company_list = ['Apple','HP','Acer','Asus','Dell','Lenovo','Chuwi','MSI',
                'Microsoft','Toshiba','Huawei','Xiaomi','Vero','Razer',
                'Mediacom','Samsung','Google','Fujitsu','LG']

type_list = ['Ultrabook','Notebook','Netbook','Gaming',
             '2 in 1 Convertible','Workstation']

os_list = ['macOS','No OS','Windows 10','Mac OS X','Linux','Android',
           'Windows 10 S','Chrome OS','Windows 7']

screen_list = ['Standard','Full HD','Quad HD+','4K Ultra HD']

yes_no = ['Yes','No']

cpu_company_list = ['Intel','AMD','Samsung']

primary_type = ['SSD','Flash Storage','HDD','Hybrid']

secondary_type = ['No','HDD','SSD','Hybrid']

gpu_company = ['Intel','AMD','Nvidia','ARM']


st.sidebar.header("Enter Laptop Details")


Company = st.sidebar.selectbox("Company", company_list)
TypeName = st.sidebar.selectbox("Type", type_list)
OS = st.sidebar.selectbox("Operating System", os_list)
Screen = st.sidebar.selectbox("Screen Type", screen_list)
Touchscreen = st.sidebar.selectbox("Touchscreen", yes_no)
IPSpanel = st.sidebar.selectbox("IPS Panel", yes_no)
RetinaDisplay = st.sidebar.selectbox("Retina Display", yes_no)
CPU_company = st.sidebar.selectbox("CPU Company", cpu_company_list)
PrimaryStorageType = st.sidebar.selectbox("Primary Storage Type", primary_type)
SecondaryStorageType = st.sidebar.selectbox("Secondary Storage Type", secondary_type)
GPU_company = st.sidebar.selectbox("GPU Company", gpu_company)


Inches = st.sidebar.slider("Screen Size (Inches)", 10.0, 18.5, 15.6)
Ram = st.sidebar.slider("RAM (GB)", 2, 64, 8)
Weight = st.sidebar.slider("Weight (kg)", 0.6, 4.8, 2.0)
ScreenW = st.sidebar.slider("Screen Width", 1300, 4000, 1920)
ScreenH = st.sidebar.slider("Screen Height", 700, 2200, 1080)
CPU_freq = st.sidebar.slider("CPU Frequency (GHz)", 0.9, 3.7, 2.5)
PrimaryStorage = st.sidebar.slider("Primary Storage (GB)", 8, 2048, 256)
SecondaryStorage = st.sidebar.slider("Secondary Storage (GB)", 0, 2048, 0)


if st.button("🔮 Predict Price"):

    input_data = pd.DataFrame([{

        "Company": Company,
        "TypeName": TypeName,
        "OS": OS,
        "Screen": Screen,
        "Touchscreen": Touchscreen,
        "IPSpanel": IPSpanel,
        "RetinaDisplay": RetinaDisplay,
        "CPU_company": CPU_company,
        "PrimaryStorageType": PrimaryStorageType,
        "SecondaryStorageType": SecondaryStorageType,
        "GPU_company": GPU_company,

        "Inches": Inches,
        "Ram": Ram,
        "Weight": Weight,
        "ScreenW": ScreenW,
        "ScreenH": ScreenH,
        "CPU_freq": CPU_freq,
        "PrimaryStorage": PrimaryStorage,
        "SecondaryStorage": SecondaryStorage
    }])

    prediction = model.predict(input_data)[0]

    st.success(f"💰 Estimated Price: € {round(prediction,2)}")
    st.info(f"📈 Model Accuracy: {accuracy}%")
