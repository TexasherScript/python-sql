# Profile Exploratory Project
_________________________________________________________________________________________________________________________
### Project Description
This project is designed to help users learn the fundamentals of data analytics by exploring a vast dataset using Python and SQL. The goal is to analyze profiles within the dataset, derive insights, and visualize key trends. This project will guide users through setting up the environment, importing the dataset, performing analysis, and creating documentation
_________________________________________________________________________________________________________________________
## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Setting Up Your Environment](#setting-up-your-environment)
3. [Using the Kaggle API](#using-the-kaggle-api)
4. [Running the Notebook For Data Cleaning](#running-the-notebook)
5. [Connecting to PostgreSQL](#connecting-to-postgresql)
6. [Contributing](#contributing)
7. [License](#license)

__________________________________________________________________________________________________________________________________________
## 1. Prerequisites

To complete this assignment, you'll need the following:

- **Git**: Download and install [Git](https://git-scm.com/downloads) with Git Bash for version control.
- **GitHub Account**: Create a GitHub account and clone the repository.
- **Kaggle Account**: Sign up on [Kaggle](https://www.kaggle.com/), and generate an API key to access datasets.
- **Python Environment**: Install Python (version 3.x) and Jupyter Notebook.
- **Pandas Library**: Install Pandas for data manipulation.
- **PostgreSQL (optional)**: If you wish to store and query your cleaned data using PostgreSQL, install PostgreSQL and set up a local or remote instance.
__________________________________________________________________________________________________________________________________________
## 2. Setting Up Your Environment

1.**Project Organization**:
   #### Example of what my git bash terminal looks like once running
   ## kyobe@ADXPS MINGW64 ~/Downloads/herScript/python-sql 
   ## $

   **In my downloads I have a folder dedicated to all things herScript saved in my folder, but also wanted to store this project in a folder within the herscript folder**
   **NOTE You are not expected to have a nested folder like mine set above** 

2. **Clone the Repository**:   
   ### in Git Bash :  
   ```bash 
   $ cd 
   $ git clone https://github.com/TexasherScript/python-sql
   cd python-sql  **Note that before you clone be sure to have a folder on your machine dedicated to this project!** 

3. **Install Dependencies: install the necessary Python libraries:**
   ```bash
   Copy code
   $ pip install -r requirements.txt
   Install Jupyter Notebook (if not already installed) or run jupiter notebooks on Google Colab:

__________________________________________________________________________________________________________________________________________
### 3. Using the Kaggle API
Install the Kaggle API: If you don't have the Kaggle API installed, you can install it using pip:

bash
Copy code
pip install kaggle
Set Up the Kaggle API:

Go to Kaggle and generate a new API token.
Download the kaggle.json file.
Move the file to your ~/.kaggle/ directory (this is done automatically in the notebook if you upload the kaggle.json file).
Ensure the API is properly authenticated by running the following in your notebook or terminal:
bash
Copy code
kaggle datasets list
Download Your Dataset: Update the dataset name in the notebook (your-dataset-here) and run the cell to download your dataset:

bash
Copy code
kaggle datasets download -d your-dataset-here --unzip -p ./data 

__________________________________________________________________________________________________________________________________________
### 4. Running the Notebook
To start Assignment 1: Data Cleaning, open the provided Jupyter notebook:

Start Jupyter Notebook:

bash
Copy code
jupyter notebook
Open the Notebook:

Navigate to the notebook titled Assignment_1_Data_Cleaning.ipynb.
Follow the steps in the notebook to:
Download the dataset from Kaggle using the Kaggle API.
Load the dataset into a Pandas DataFrame.
Perform data cleaning (handle missing values, remove duplicates, data type conversion, etc.).
Apply transformations to prepare the dataset for analysis.
Save the cleaned dataset.
__________________________________________________________________________________________________________________________________________
### 5. Connecting to PostgreSQL
For those who wish to take the extra step and store their cleaned dataset in PostgreSQL, follow these instructions:

Set Up PostgreSQL:

Install PostgreSQL on your system or use a remote instance.
Create a new database and user.
Connect to PostgreSQL: Use Python libraries such as psycopg2 or SQLAlchemy to connect to the database from the notebook. An example connection script is included in the notebook to guide you through querying and storing your data:

python
Copy code
import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="your_database",
    user="your_user",
    password="your_password"
)
Run SQL Queries: You can interact with your cleaned data using SQL queries directly within the notebook.
__________________________________________________________________________________________________________________________________________

### 6. Contributing
If you want to contribute to this project, feel free to fork the repository and submit a pull request. We welcome all improvements, bug fixes, and new feature suggestions!

Fork the repository.
Create a feature branch: git checkout -b my-new-feature
Commit your changes: git commit -am 'Add some feature'
Push to the branch: git push origin my-new-feature
Submit a pull request!
__________________________________________________________________________________________________________________________________________

## 7. License
This project is licensed under the MIT License. See the LICENSE file for details.


