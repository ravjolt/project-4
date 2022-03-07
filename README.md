# Demystifying Machine Learning in Healthcare

## Overview

Machine Learning is used to uncover patterns and predict a variety of results that can perform complex functions in an efficient manner. This is very useful, particularly in the medical field where Machine Learning can be implemented to predict diseases.

As such, we have taken an existing dataset of cardiologist patients to build a platform that will predict if an individual is at-risk of a heart attack based on the patient's health condition.

## Goals:

1. Pre-process the existing dataset
2. Gather basic statistical information and infer.
3. Train three different types of Machine Learning models, analyze the results, and choose the best model.

## Technical Specifications:

1. Amazon AWS
2. Python - Google Colab
3. Libraries
4. Matplotlib
5. Pandas
6. Numpy
7. Seaborn
8. Sklearn
9. HTML/CSS/

### Results:

1. Pre-process
   Preprocessing

![dataset.jpg](https://github.com/ghhyc/Project-4/blob/main/images/dataset.JPG)

Postprocessing

![dataset2.jpg](https://github.com/ghhyc/Project-4/blob/main/images/dataset2.JPG)

2. Basic Inference from dataset
   Correlation Analysis - a basic visual to determine if relationships between categories can be made to determine if an individual is prone to heart attack.

   Heat map

   ![heatmap.jpg](https://github.com/ghhyc/Project-4/blob/main/images/heatmpap.JPG)

   Pairplot

   ![pairplot.jpg](https://github.com/ghhyc/Project-4/blob/main/images/pairplot.JPG)

   ### Model Comparison:

   Three models were choosen.

   \*\*Support Vector Machine - For flexibility in which it can solve both regression and classification.

   \*\*RandomForest Classifier - Also flexibile where it can perform both regression and classification tasks.

   \*\*Category Boosting (catboost) - Handling Categorical features automatically: We can use CatBoost without any explicit pre-processing to convert categories into numbers.

   F1-score on Cross-Validation (CV) - Measuring test accuracy with test data

   ![model_comparison.jpg](https://github.com/ghhyc/Project-4/blob/main/images/model_comparision.JPG)

   Verify F1-scores using test data

   ![f1_verify.jpg](https://github.com/ghhyc/Project-4/blob/main/images/f1_verify.JPG)

   AUC-ROC curve - yet another method to verify performance of models.

   ![roc_curve.jpg](https://github.com/ghhyc/Project-4/blob/main/images/roc_curve.JPG)

   **FINAL RESULTS**

   ![final.jpg](https://github.com/ghhyc/Project-4/blob/main/images/final.JPG)

## Heart disease predictor

    We trained a RandomForest model on a sample of the hospital data, and then created a web application that uses this model to predict
    whether or not a patient has heart disease.

    Here is an example of positive prediction

    ![positive_example.png](https://github.com/ghhyc/Project-4/blob/main/images/positive_example.png)

    Here is an example of negative prediction

    ![negative_example.png](https://github.com/ghhyc/project-4/blob/main/images/negative_example.png)
