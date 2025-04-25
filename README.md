<h1 align="center">📊 Data analysis - Brasileirao 2023</h1>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white">
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white">
  <img src="https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white">
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white">
</div>

## 📖 Summary 

- [Main Objective](#-main-objective)
- [Development and Technologies Used](#-development-and-technologies-used)
- [How to Run](#-how-to-run)
- [Contact](#-contact)

## 🥅 Main Objective

The main goal of this project is to showcase my ability to collect, clean, and analyze real-world football data using Python and data visualization tools. Through this analysis, I explore some key statistics from the 2023 Brasileirão season to uncover patterns and insights about teams performance.

This project was developed using tools such as Python (for data processing), and libraries like Pandas, Matplotlib, and Seaborn (for visualizations and analytics).

More than just a technical exercise, this repository reflects my passion for football, data, and learning through practical, engaging projects. It’s also a space where I continue to grow and improve my skills as I expand the analysis with new features.

Whether you're a recruiter, a fellow data enthusiast, or a fan of the Brasileirão, feel free to explore the project and reach out with suggestions or ideas! ⚽📊

## 🔨 Development and Technologies Used

The project began with the definition of goals: analyze key statistics from the 2023 Brasileirão season. After evaluating data sources, I chose the API-Football API and retrieved data for all fixtures in JSON format. Due to API limitations, I worked with the full 2023 season.

Using Python, I created scripts to load and normalize the raw JSON data. The initial focus was to transform nested structures into clean, usable DataFrames from Pandas.

Once the data was loaded, I filtered relevant columns for every algorithm (such as team names, goals, round number, and match results). I wrote functions to process data for different analyses, including goal tracking and team performance over time.

With the data prepared, I developed core algorithms to calculate:
- Total goals per round.
- Goals scored and conceded per round for each team.
- Points accumulated per round for comparison between 2 teams.

Using matplotlib and seaborn, I created insightful visualizations:
- Bar charts for goals per round.
- Line plots comparing team points over time. These visualizations were designed to be clear and informative, highlighting patterns in team performance.

![image](https://github.com/user-attachments/assets/664d10ea-a6e1-4a5c-8cc8-07f2edd10d45)
![image](https://github.com/user-attachments/assets/138c38da-3042-4045-a6dd-4cfc4ff256c2)
![image](https://github.com/user-attachments/assets/cb25f932-0b47-4de5-aff4-a927a27d92d9)

The code was organized into modules (process_data.py, plot_stats.py, etc.) to ensure clean separation of logic and reusability. I followed good practices in naming, comments, and file organization (with src/ and data/ folders).

After local development, I initialized a Git repository, handled branching, and uploaded the project to GitHub.

## 💻 How to Run

### 📥 1. Clone this repository and navigate to the project folder
First, open the terminal and run the following command to clone the repository:  
```bash
git clone https://github.com/rfmotaa/Analise-Brasileirao/tree/main
cd Analise-Brasileirao
```

### 📂 2. Install the dependencies
```bash
pip install requirements.txt
```

### 💨 3. Run the Python file 
There is 3 main Python files for each algorithm and objective, run the file you want to view.
They are in the following order
- Points accumulated per round for comparison between 2 teams.
- Goals scored and conceded per round for each team.
- Total goals per round.
```bash
python src/Comparation.py
python src/Efficiecy.py
python src/Goals_by_round.py
```
Make sure the data/fixtures.json file is present and correctly structured before running the scripts.

## 📫 Contact

[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rfmotaa)

[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:rafaelssoni1000@gmail.com)

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rfmota/)

[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://www.instagram.com/rf_motaa/)
