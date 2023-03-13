# Student Performance Prediction Dashboard

This project is a web application built using Panel and Plotly that allows users to explore a dataset of student performance and build multiple regression models to predict academic outcomes.

Panel is an open-source Python library that lets you create custom interactive web apps and dashboards by connecting user-defined widgets to plots, images, tables, or text
# Installation

To install the necessary packages, run the following command:
```
pip install -r requirements.txt
```  
# Usage

To view the website, run the following command
```
panel serve dashboard.py ai.py --index=templates/index.html
```  
This will launch the Panel home in your web browser. The other two other are :

# Dashboard

This page provides an exploratory data analysis (EDA) of the student performance dataset. Users can interact with a variety of visualizations to explore patterns in the data, including:

- Box plots of all the target variables
- Histograms of the distribution of each variable
- A correlation heatmap of the variables
- UMAP representation

# Machine Learning
## Model Building

This page allows users to build multiple regression models to predict student performance. Users can  choose from a range of regression algorithms, their corresponding hyperparameters and evaluate the performance of the model using a variety of metrics.

# Contact

If you have any questions or comments about this project, please contact the project owners.
