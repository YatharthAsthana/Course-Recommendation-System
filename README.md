# Course-Recommendation-System
I have harnessed the power of Cosine Similarity and CountVectorizer for precise recommendations, with JavaScript leading our Exploratory Data Analysis. This robust webpage is crafted using Flask, ensuring seamless user interaction. 
Objective of the project
To build an intelligent recommendation system that suggests courses based on user preferences and similarities between courses. The system uses the Udemy dataset for reference to offer relevant course recommendations.

Technologies and Tools Used
Machine Learning: The recommendation algorithm leverages Cosine Similarity and CountVectorizer to analyze and determine the similarity between courses based on their descriptions, titles, and other textual content.
Exploratory Data Analysis (EDA): JavaScript is utilized for interactive data visualizations and EDA to understand the dataset better and uncover patterns and insights.
Web Framework: The entire application is built using Flask, a lightweight web framework in Python, enabling seamless integration of the machine learning model and providing an interactive web interface for users.

Methodology
Data Preprocessing: The Udemy dataset is cleaned and preprocessed to remove any inconsistencies or irrelevant information.
Feature Extraction: CountVectorizer is used to convert course descriptions into a matrix of token counts.
Similarity Calculation: Cosine Similarity is employed to calculate the similarity between courses. Courses with higher similarity scores are considered more relevant to the user's interest.
User Interface: A user-friendly web interface is created using Flask, allowing users to input their course preferences and receive tailored recommendations.

Key Features
Personalized Recommendations: Users receive course suggestions based on their input, enhancing their learning experience.
Interactive Visualizations: JavaScript-powered visualizations help users understand the dataset and the recommendation process.
Scalability: The system is designed to handle a growing number of courses and users efficiently.
