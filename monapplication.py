import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import pickle

data=pickle.load(open(r"C:\Users\Home\Desktop\Obesity_prediction.sav","rb"))
df=data["df"]
final_df=data["finaldf"]
selected = option_menu(
    menu_title=None,  # Correct parameter name
    options=["Acceuil", "Visualisation", "Prediction"],  # Correct spelling of 'Menu'
    icons=["house", "bar-chart", "robot"],  # Adding icons (optional)
    menu_icon="cast",  # Icon for the menu (optional)
    default_index=0,  # Default selected index (optional)
    orientation="horizontal"  # Set orientation to horizontal
)

# Display content based on selected menu item
if selected == "Acceuil":
    st.title("Prédire si vous étes en danger")
    st.info("C'est une application web pour visualiser des données et prédire le risque de l'obeesité.")
    a1, a2, a3,a4=st.columns(4)
    a1.metric("Max de l'Age",df["Age"].max())
    a4.metric("Le niveau de poids tendence",df["NObeyesdad"].max())
    a3.metric("Max de poids",df["Weight"].max())
    a2.metric("Min de poids",df["Weight"].min())

elif selected == "Visualisation":
    st.title("Visualisation des données")
    st.write("Choisissez le type de visualisation")
    selectedVisual = option_menu(
    menu_title=None,  # Correct parameter name
    options=["Niveau de poids", "Relations",],  # Correct spelling of 'Menu'
    default_index=0,  # Default selected index (optional)
)




    if selectedVisual=="Niveau de poids":
      level=st.selectbox("Choisissez le niveau de poids",("Obesity_Type_I","Obesity_Type_III","Obesity_Type_II","Overweight_Level_I","Overweight_Level_II","Normal_Weight","Insufficient_Weight"),index=None,placeholder="choisissez un niveau")
      def vislevel(level):
            if level:
                  dfi=df[df["NObeyesdad"] == level][["Age","Weight","Gender"]]
                  st.scatter_chart(dfi,x="Age",y="Weight",color="Gender")


      vislevel(level) 
    elif selectedVisual=="Relations":



      Level=st.selectbox("Choisissez le niveau de poids",("Obesity_Type_I","Obesity_Type_III","Obesity_Type_II","Overweight_Level_I","Overweight_Level_II","Normal_Weight","Insufficient_Weight"),index=None,placeholder="choisissez un niveau")
      def vislevel(level):
            if Level:
                  dfi=df[df["NObeyesdad"] == Level][["Age","Gender","CAEC","Weight","Height","family_history_with_overweight"]]
                  levelDf=({
                "Weight":dfi["Weight"],
                "Height":dfi["Height"],
                "Gender":dfi["Gender"],
                "family_history_with_overweight":dfi["family_history_with_overweight"],
                "CAEC":dfi["CAEC"],
                "x":dfi["Age"].index
          })
                  st.scatter_chart(levelDf,x="Weight",y="x",color="family_history_with_overweight")
                  st.bar_chart(levelDf,x="Weight",y="x",color="CAEC")
                  st.scatter_chart(levelDf,x="Weight",y="x",color="family_history_with_overweight")



      vislevel(Level) 

    










elif selected == "Prediction":
    st.title("Prédictions")
    st.write("Contenu de la page de prédiction")
    col1, col2 = st.columns(2)
    with col1:
        Age=st.number_input("Age", value=14, placeholder="Entrez votre age!")
        Height=st.number_input("Taille",value=1.4,placeholder="Entrez votre taille")
        family_history_with_overweight=st.selectbox("Est ce que le surpoids est hériditaire dans votre famille?",("yes", "no"),index=None,placeholder="choisissez votre cas")
        family_history_with_overweight= 1 if family_history_with_overweight =="yes" else 0
        FCVC=st.number_input("Combien la quantité des legumes  vous manger dans vos repas?",value=0) 
        CAEC = st.select_slider("Est ce que vous mangez des snacks entre les repas?", 
                        options=["no", "Sometimes", "Frequently", "Always"])

        if CAEC == "Sometimes":
             CAEC = 2
        elif CAEC == "Frequently":
             CAEC = 1
        elif CAEC == "Always":
             CAEC = 0
        elif CAEC == "no":
             CAEC = 3
        CH2O=st.number_input("Combien d'eau vous buvez par jour",value=1.0)
        TUE=st.number_input("Combien de fois vous utilisez des appareils informatiques?",value=0.0)
        CALC=st.select_slider("Vous buvez des boissons alcolisées?",options=["no", "Sometimes", "Frequently", "Always"])
        if CALC == "no":
                CALC= 3
        elif CALC == "Sometimes":
                CALC = 2
        elif CALC == "Frequently":
                CALC = 1
        elif CALC == "Always":
                CALC = 0
    with col2:
        Weight=st.number_input("Poids",value=36,placeholder="Entrez votre poids")
        Gender=st.radio("Sexe",key="Gender",options=["Male","Female"],index=None)
        Gender=1 if Gender=="Male"  else 0
        FAVC=st.radio("Est ce que vous manger des repas riches en calories  frequement?",index=None,key="FAVC",options=["yes","no"]) 
        FAVC= 1 if FAVC =="yes" else 0
        NCP=st.number_input("Combien de repas principale vous manger par jour",value=1.0)
        SMOKE=st.radio("Est ce que vous fumez?",index=None,key="SMOKE",options=["yes","no"]) 
        SMOKE= 1 if SMOKE =="yes" else 0
        SCC=st.radio("Est ce que vous suivez les calories que vous consomez par jour?",index=None,key="SCC",options=["yes","no"]) 
        SCC= 1 if SCC =="yes" else 0
        FAF=st.number_input("Combien de fois vous faites du sport par semaine?",value=0.0)
        MTRANS=st.selectbox("Quel moyen de transport vous utilisez qotidiennement?",("Public_Transportation","Walking","Automobile","Motorbike","Bike"),index=None,placeholder="choisissez un moyen")
        if MTRANS == "Public_Transportation":
                MTRANS = 3
        elif MTRANS == "Walking":
                MTRANS = 4
        elif MTRANS == "Automobile":
                MTRANS = 0
        elif MTRANS == "Motorbike":
                MTRANS = 2
        elif MTRANS==  "Bike":
                MTRANS=1     
    inputs=pd.DataFrame({
          
              
              "Gender":Gender,
              "CALC":CALC,
              "FAVC":FAVC,
              "SCC":SCC,
              "SMOKE":SMOKE,
              "family_history_with_overweight":family_history_with_overweight,
              "CAEC":CAEC,
              "MTRANS":MTRANS,
              "Age":Age,
              "Height":Height,
              "Weight":Weight,
              "FCVC":FCVC,
              "NCP":NCP,
              "CH2O":CH2O,
              "FAF":FAF,
              "TUE":TUE
              }
              ,index=[0])
    p=st.button("Prédire!")
    model=data["model"]
    if p:
          result=model.predict(inputs)
          if result==3:
                st.warning("Obesity_Type_II")
          elif result==2:
                st.warning("Obesity_Type_I")   
          elif result==4:
                st.warning("Obesity_Type_III")   
          elif result==6:
                st.info("Overweight_Level_II")
          elif result==5:
                st.info("Overweight_Level_I") 
          elif result==1:
                st.success("Normal weighit") 
          elif result==0:
                st.warning("Insufficient_Weight")                
        


