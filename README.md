# YouTube Dislike Dataset Analysis

## Overview
This project analyzes a YouTube dislike dataset to understand video engagement patterns, channel activity, and the relationship between views, likes, dislikes, and comments. The project includes data cleaning, exploratory data analysis, visualization, SQL storage, and predictive modeling using Linear Regression.

The dataset was processed using Python and Pandas. Missing values were removed, the `published_at` column was converted into datetime format, and a new `published_month` column was created to analyze monthly video publishing trends. The analysis also identifies top channels by video count, videos with the highest and lowest likes, videos with the highest and lowest dislikes, and the number of videos published each month.

Visualizations were created to study the relationship between views and dislikes, views and comments, correlation among engagement metrics, and view count trends over time. The project also stores the dataset in a SQLite database and retrieves records using SQL queries.

A Linear Regression model was built to predict `view_count` using `likes`, `dislikes`, and `comment_count` as input features. Model performance was evaluated using Mean Squared Error and R-squared score.

## Key Features
- Loaded and explored YouTube dislike dataset
- Checked dataset shape, data types, summary statistics, and missing values
- Removed null values for cleaner analysis
- Converted published date into datetime format
- Created month-based publishing analysis
- Found unique videos, channels, and channel titles
- Identified top 10 and bottom 10 channels by video count
- Found videos with maximum and minimum likes
- Found videos with maximum and minimum dislikes
- Visualized relationship between views and dislikes
- Visualized relationship between views and comments
- Created correlation heatmap for views, likes, dislikes, and comments
- Analyzed views over time
- Stored dataset in SQLite database
- Built Linear Regression model to predict view count
- Created a reusable predictive modeling class

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SQLite
- Jupyter Notebook

## Machine Learning Model
- Linear Regression

## Features Used for Prediction
- Likes
- Dislikes
- Comment Count

## Target Variable
- View Count

## Visualizations
- Scatter plot: Views vs Dislikes
- Scatter plot: Views vs Comments
- Correlation heatmap
- Line plot: Views over time

## Future Improvements
- Add more advanced models such as Random Forest and XGBoost
- Perform feature engineering using title length, tags, and publish time
- Add sentiment analysis on video titles or comments
- Build an interactive dashboard using Streamlit
- Improve database queries with advanced SQL analysis
- Add model comparison with multiple regression algorithms

## Author
Aswin S
