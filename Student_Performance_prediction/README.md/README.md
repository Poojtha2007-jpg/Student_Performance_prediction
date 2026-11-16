Student Performance Prediction

Project Overview

Student Performance Prediction is a Machine Learning application developed using Python and Streamlit.

The application predicts a student's final academic grade out of 20 based on different student details and displays a performance category.

Objectives

- Predict students' final academic performance.
- Apply Machine Learning techniques to student data.
- Provide an easy-to-use web interface.
- Display predicted grades and performance categories.

Technologies Used

- Python
- Machine Learning
- Random Forest Regressor
- Streamlit
- Pandas
- Scikit-learn
- Jupyter Notebook

Dataset

Dataset: Student Mathematics Performance (student-mat.csv)

The application collects student information, including:

- Age
- Mother's and father's education
- Travel time
- Weekly study time
- Past class failures
- Nursery school attendance
- Interest in higher education
- Internet access
- Relationship status

Machine Learning Model

The project uses a Random Forest Regressor model, as identified in the project analysis notebook.

The trained model is saved in the model folder.

Application Features

- Student detail input form
- Final grade prediction out of 20
- Performance classification
- Interactive Streamlit interface

Performance Categories

- 15 and above: Excellent Performance
- 12 and above: Good Performance
- 10 and above: Average Performance
- Below 10: Needs Improvement

Project Folder Structure

- app/ – Streamlit application
- dataset/ – Student dataset
- model/ – Trained machine learning model
- notebooks/ – Data analysis notebook
- screenshots/ – Application screenshots

How to Run the Application

1. Install Python and the required libraries.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

python -m streamlit run app/app.py

5. Open the local URL displayed in the terminal.

Conclusion

This project demonstrates how Machine Learning can be used to predict student academic performance through an interactive web application.