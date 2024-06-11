import joblib
import numpy as np
import pandas as pd
import os

model_raw = "https://github.com/hudasf/Dashboard-Jaya-Institute/raw/main/model/"
main_dir = "D:/Tech/python/jayainstitut/"

encoder_Application_order = joblib.load("model/encoder_Application_order.joblib")
encoder_Application_mode = joblib.load("model/encoder_Application_mode.joblib")
encoder_Course = joblib.load("model/encoder_Course.joblib")
encoder_Daytime_evening_attendance = joblib.load("model/encoder_Daytime_evening_attendance.joblib")
encoder_Debtor = joblib.load("model/encoder_Debtor.joblib")
encoder_Displaced = joblib.load("model/encoder_Displaced.joblib")
encoder_Educational_special_needs = joblib.load("model/encoder_Educational_special_needs.joblib")
encoder_Gender = joblib.load("model/encoder_Gender.joblib")
encoder_International = joblib.load("model/encoder_International.joblib")
encoder_Marital_status = joblib.load("model/encoder_Marital_status.joblib")
encoder_Previous_qualification = joblib.load("model/encoder_Previous_qualification.joblib")
encoder_Scholarship_holder = joblib.load("model/encoder_Scholarship_holder.joblib")
encoder_Tuition_fees_up_to_date = joblib.load("model/encoder_Tuition_fees_up_to_date.joblib")

scaler_Admission_grade = joblib.load("model/scaler_Admission_grade.joblib")
scaler_Age_at_enrollment = joblib.load("model/scaler_Age_at_enrollment.joblib")
scaler_Curricular_units_1st_sem_approved = joblib.load("model/scaler_Curricular_units_1st_sem_approved.joblib")
scaler_Curricular_units_1st_sem_credited = joblib.load("model/scaler_Curricular_units_1st_sem_credited.joblib")
scaler_Curricular_units_1st_sem_enrolled = joblib.load("model/scaler_Curricular_units_1st_sem_enrolled.joblib")
scaler_Curricular_units_1st_sem_evaluations = joblib.load("model/scaler_Curricular_units_1st_sem_evaluations.joblib")
scaler_Curricular_units_1st_sem_grade = joblib.load("model/scaler_Curricular_units_1st_sem_grade.joblib")
scaler_Curricular_units_1st_sem_without_evaluations = joblib.load("model/scaler_Curricular_units_1st_sem_without_evaluations.joblib")
scaler_Curricular_units_2nd_sem_approved = joblib.load("model/scaler_Curricular_units_2nd_sem_approved.joblib")
scaler_Curricular_units_2nd_sem_credited = joblib.load("model/scaler_Curricular_units_2nd_sem_credited.joblib")
scaler_Curricular_units_2nd_sem_enrolled = joblib.load("model/scaler_Curricular_units_2nd_sem_enrolled.joblib")
scaler_Curricular_units_2nd_sem_evaluations = joblib.load("model/scaler_Curricular_units_2nd_sem_evaluations.joblib")
scaler_Curricular_units_2nd_sem_grade = joblib.load("model/scaler_Curricular_units_2nd_sem_grade.joblib")
scaler_Curricular_units_2nd_sem_without_evaluations = joblib.load("model/scaler_Curricular_units_2nd_sem_without_evaluations.joblib")
scaler_GDP = joblib.load("model/scaler_GDP.joblib")
scaler_Inflation_rate = joblib.load("model/scaler_Inflation_rate.joblib")
scaler_Previous_qualification_grade = joblib.load("model/scaler_Previous_qualification_grade.joblib")
scaler_Unemployment_rate = joblib.load("model/scaler_Unemployment_rate.joblib")


def data_preprocessing(data):

    # data = data.copy()
    df = pd.DataFrame()
    
    df["Marital_status"] = encoder_Marital_status.transform(data["Marital_status"]) 
    df["Application_mode"] = encoder_Application_mode.transform(data["Application_mode"]) 
    df["Application_order"] = encoder_Application_order.transform(data["Application_order"])
    df["Course"] = encoder_Course.transform(data["Course"])
    df["Daytime_evening_attendance"] = encoder_Daytime_evening_attendance.transform(data["Daytime_evening_attendance"])  
    df["Previous_qualification"] = encoder_Previous_qualification.transform(data["Previous_qualification"]) 
    df["Previous_qualification_grade"] = scaler_Previous_qualification_grade.transform(np.asarray(data["Previous_qualification_grade"]).reshape(-1,1))[0]
    df["Admission_grade"] = scaler_Admission_grade.transform(np.asarray(data["Admission_grade"]).reshape(-1, 1))[0] 
    df["Displaced"] = encoder_Displaced.transform(data["Displaced"]) 
    df["Educational_special_needs"] = encoder_Educational_special_needs.transform(data["Educational_special_needs"])
    df["Debtor"] = encoder_Debtor.transform(data["Debtor"]) 
    df["Tuition_fees_up_to_date"] = encoder_Tuition_fees_up_to_date.transform(data["Tuition_fees_up_to_date"]) 
    df["Gender"] = encoder_Gender.transform(data["Gender"]) 
    df["Scholarship_holder"] = encoder_Scholarship_holder.transform(data["Scholarship_holder"]) 
    df["Age_at_enrollment"] = scaler_Age_at_enrollment.transform(np.asarray(data["Age_at_enrollment"]).reshape(-1,1))[0]
    df["International"] = encoder_International.transform(data["International"]) 
    
    
              
    df["Curricular_units_1st_sem_credited"] = scaler_Curricular_units_1st_sem_credited.transform(np.asarray(data["Curricular_units_1st_sem_credited"]).reshape(-1,1))[0]
    df["Curricular_units_1st_sem_enrolled"] = scaler_Curricular_units_1st_sem_enrolled.transform(np.asarray(data["Curricular_units_1st_sem_enrolled"]).reshape(-1,1))[0]
    df["Curricular_units_1st_sem_evaluations"] = scaler_Curricular_units_1st_sem_evaluations.transform(np.asarray(data["Curricular_units_1st_sem_evaluations"]).reshape(-1,1))[0]
    df["Curricular_units_1st_sem_approved"] = scaler_Curricular_units_1st_sem_approved.transform(np.asarray(data["Curricular_units_1st_sem_approved"]).reshape(-1,1))[0]
    df["Curricular_units_1st_sem_grade"] = scaler_Curricular_units_1st_sem_grade.transform(np.asarray(data["Curricular_units_1st_sem_grade"]).reshape(-1,1))[0]
    df["Curricular_units_1st_sem_without_evaluations"] = scaler_Curricular_units_1st_sem_without_evaluations.transform(np.asarray(data["Curricular_units_1st_sem_without_evaluations"]).reshape(-1,1))[0]
    df["Curricular_units_2nd_sem_credited"] = scaler_Curricular_units_2nd_sem_credited.transform(np.asarray(data["Curricular_units_2nd_sem_credited"]).reshape(-1,1))[0]
    df["Curricular_units_2nd_sem_enrolled"] = scaler_Curricular_units_2nd_sem_enrolled.transform(np.asarray(data["Curricular_units_2nd_sem_enrolled"]).reshape(-1,1))[0]
    df["Curricular_units_2nd_sem_evaluations"] = scaler_Curricular_units_2nd_sem_evaluations.transform(np.asarray(data["Curricular_units_2nd_sem_evaluations"]).reshape(-1,1))[0]
    df["Curricular_units_2nd_sem_approved"] = scaler_Curricular_units_2nd_sem_approved.transform(np.asarray(data["Curricular_units_2nd_sem_approved"]).reshape(-1,1))[0]
    df["Curricular_units_2nd_sem_grade"] = scaler_Curricular_units_2nd_sem_grade.transform(np.asarray(data["Curricular_units_2nd_sem_grade"]).reshape(-1,1))[0]
    df["Curricular_units_2nd_sem_without_evaluations"] = scaler_Curricular_units_2nd_sem_without_evaluations.transform(np.asarray(data["Curricular_units_2nd_sem_without_evaluations"]).reshape(-1,1))[0]
    df["Unemployment_rate"] = scaler_Unemployment_rate.transform(np.asarray(data["Unemployment_rate"]).reshape(-1,1))[0]
    df["Inflation_rate"] = scaler_Inflation_rate.transform(np.asarray(data["Inflation_rate"]).reshape(-1,1))[0]
    df["GDP"] = scaler_GDP.transform(np.asarray(data["GDP"]).reshape(-1,1))[0]

    return df