import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing
from prediction import prediction


expected_order = ['Marital_status', 'Application_mode', 'Application_order', 'Course',
                  'Daytime_evening_attendance', 'Previous_qualification',
                  'Previous_qualification_grade', 'Admission_grade', 'Displaced',
                  'Educational_special_needs', 'Debtor', 'Tuition_fees_up_to_date',
                  'Gender', 'Scholarship_holder', 'Age_at_enrollment', 'International',
                  'Curricular_units_1st_sem_credited', 'Curricular_units_1st_sem_enrolled',
                  'Curricular_units_1st_sem_evaluations', 'Curricular_units_1st_sem_approved',
                  'Curricular_units_1st_sem_grade', 'Curricular_units_1st_sem_without_evaluations',
                  'Curricular_units_2nd_sem_credited', 'Curricular_units_2nd_sem_enrolled',
                  'Curricular_units_2nd_sem_evaluations', 'Curricular_units_2nd_sem_approved',
                  'Curricular_units_2nd_sem_grade', 'Curricular_units_2nd_sem_without_evaluations',
                  'Unemployment_rate', 'Inflation_rate', 'GDP']

data = pd.DataFrame()

def main():

    st.title("Student Dropout Predictor App")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("### Student General Info")
        show_student_general_info()

    with col2:
        st.write("### Student Academic Info")
        show_student_academic_info()

    with col3:
        st.write("### Student Miscellaneous Info")
        show_student_misc_info()

    with st.expander("View the Raw Data"):
        st.dataframe(data=data, width=800, height=10)

    if st.button('Predict'):
        new_data = data_preprocessing(data=data)
        with st.expander("View the Preprocessed Data"):
            st.dataframe(data=new_data, width=800, height=10)
        st.write("Dropout prediction : {}".format(prediction(new_data)))

def show_student_general_info():
    Marital_status = st.selectbox("Marital status",[1,2])
    data.loc[0, "Marital_status"] = Marital_status

    Application_mode = st.selectbox("Application mode",[1,2,5,7,10,15,16,17,18,26,27,39,42,43,44,51,53,57])
    data["Application_mode"] = Application_mode

    Application_order = st.selectbox("Application order",[1,2,3,4,5,6,9])
    data["Application_order"] = Application_order

    Course = st.selectbox("Course",[33,171,8014,9003,9070,9085,9119,9130,9147,9238,9254,9500,9556,9670,9773,9853,9991])
    data["Course"] = Course

    Daytime_evening_attendance = st.selectbox("Day/Evening Attendance",[1,0])
    data["Daytime_evening_attendance"] = Daytime_evening_attendance

    Previous_qualification = st.selectbox("Previous qualification",[1,2,3,4,5,6,9,10,12,14,15,19,38,39,40,42,43])
    data["Previous_qualification"] = Previous_qualification

    Previous_qualification_grade = st.number_input("Previous Grade", min_value=0, max_value=200)
    data["Previous_qualification_grade"] = Previous_qualification_grade

    Admission_grade = st.number_input("Admission Grade", min_value=0.0, max_value=200.0, format="%.1f")
    data["Admission_grade"] = Admission_grade

    Displaced  = st.selectbox("Displaced",[1,0])
    data["Displaced"] = Displaced

    Educational_special_needs = st.selectbox("Special needs",[1,0])
    data["Educational_special_needs"] = Educational_special_needs

    Debtor = st.selectbox("Debtor",[1,0])
    data["Debtor"] = Debtor
    
    Tuition_fees_up_to_date = st.selectbox("Tuition fees update",[1,0])
    data["Tuition_fees_up_to_date"] = Tuition_fees_up_to_date

    Gender = st.selectbox("Gender",[1,0])
    data["Gender"] = Gender

    Scholarship_holder = st.selectbox("Scholarship holder",[1,0])
    data["Scholarship_holder"] = Scholarship_holder

    Age_at_enrollment = st.number_input("Age at enrollment", min_value=10, max_value=150)
    data["Age_at_enrollment"] = Age_at_enrollment

    International = st.selectbox("International",[1,0])
    data["International"] = International

def show_student_academic_info():



    Curricular_units_1st_sem_credited = st.number_input("CU Credit 1st sem", min_value=0, max_value=50)
    data["Curricular_units_1st_sem_credited"] = Curricular_units_1st_sem_credited

    Curricular_units_1st_sem_enrolled = st.number_input("CU Enrolled 1st sem", min_value=0, max_value=50)
    data["Curricular_units_1st_sem_enrolled"] = Curricular_units_1st_sem_enrolled

    Curricular_units_1st_sem_evaluations = st.number_input("CU Eval 1st sem", min_value=0, max_value=50)
    data["Curricular_units_1st_sem_evaluations"] = Curricular_units_1st_sem_evaluations

    Curricular_units_1st_sem_approved = st.number_input("CU Approved 1st sem", min_value=0, max_value=50)
    data["Curricular_units_1st_sem_approved"] = Curricular_units_1st_sem_approved

    Curricular_units_1st_sem_grade = st.number_input("CU Grade 1st sem", min_value=0.0, max_value=50.0, format="%.1f")
    data["Curricular_units_1st_sem_grade"] = Curricular_units_1st_sem_grade

    Curricular_units_1st_sem_without_evaluations = st.number_input("CU w/o Eval 1st sem", min_value=0, max_value=50)
    data["Curricular_units_1st_sem_without_evaluations"] = Curricular_units_1st_sem_without_evaluations

    Curricular_units_2nd_sem_credited = st.number_input("CU Credit 2nd sem", min_value=0, max_value=50)
    data["Curricular_units_2nd_sem_credited"] = Curricular_units_2nd_sem_credited

    Curricular_units_2nd_sem_enrolled = st.number_input("CU Enrolled 2nd sem", min_value=0, max_value=50)
    data["Curricular_units_2nd_sem_enrolled"] = Curricular_units_2nd_sem_enrolled

    Curricular_units_2nd_sem_evaluations = st.number_input("CU Eval 2nd sem", min_value=0, max_value=50)
    data["Curricular_units_2nd_sem_evaluations"] = Curricular_units_2nd_sem_evaluations

    Curricular_units_2nd_sem_approved = st.number_input("CU Approved 2nd sem", min_value=0, max_value=50)
    data["Curricular_units_2nd_sem_approved"] = Curricular_units_2nd_sem_approved

    Curricular_units_2nd_sem_grade = st.number_input("CU Grade 2nd sem", min_value=0.0, max_value=50.0, format="%.1f")
    data["Curricular_units_2nd_sem_grade"] = Curricular_units_2nd_sem_grade

    Curricular_units_2nd_sem_without_evaluations = st.number_input("CU w/o Eval 2nd sem", min_value=0, max_value=50)
    data["Curricular_units_2nd_sem_without_evaluations"] = Curricular_units_2nd_sem_without_evaluations

def show_student_misc_info():

    Unemployment_rate = st.number_input("Unemployment rate", min_value=0.0, max_value=99.9, format="%.1f")
    data["Unemployment_rate"] = Unemployment_rate
    
    Inflation_rate = st.number_input("Inflation rate", min_value=0.0, max_value=99.0, format="%.1f")
    data["Inflation_rate"] = Inflation_rate

    GDP = st.number_input("GDP", min_value=-30.0, max_value=30.0, format="%.1f")
    data["GDP"] = GDP

if __name__ == "__main__":
    main()