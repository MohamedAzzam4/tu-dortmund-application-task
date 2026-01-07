Cycling Performance Analysis 🚴‍♂️📊
Statistical Analysis of Rider Performance in Professional Cycling
This repository contains the source code and data for a statistical analysis project investigating the relationship between cyclist physiology ("Rider Class") and terrain ("Stage Class"). The project was developed as part of an application task for the M.Sc. Data Science program at TU Dortmund University.
📌 Project Overview
In professional cycling, a rider's value is often conditional on the terrain. This project uses statistical methods to quantify:
Whether there are significant performance differences between rider classes (Sprinters, Climbers, All Rounders, etc.).
Whether these differences depend on the stage profile (Flat, Hills, Mountain).
The analysis utilizes a Two-Way ANOVA to test for interaction effects and Tukey's HSD for post-hoc pairwise comparisons.
📂 Repository Structure
analysis_code.py: The main Python script that performs data cleaning, statistical analysis, and visualization.
data_report.csv: The dataset containing rider performance records.
requirements.txt: List of Python dependencies required to run the code.
output/: (Generated after running) Contains the generated plots (.png) and statistical results (.csv, .txt).
📊 Key Findings
Interaction Effect: There is a highly significant interaction between Rider Class and Stage Class ($p < 0.001$), confirming that performance is strictly dependent on the terrain.
Specialization: Sprinters dominate Flat stages but underperform significantly on Mountains.
Versatility: "All Rounders" proved to be the most versatile class, showing the highest average performance on Mountain stages in this simulation.
🛠️ Methodology
Language: Python 3.10+
Libraries: pandas (Data Manipulation), seaborn & matplotlib (Visualization), statsmodels & scipy (Statistical Testing).
Statistical Tests:
Two-Way ANOVA (Analysis of Variance)
Shapiro-Wilk Test (Normality check)
Levene's Test (Homogeneity of Variance)
Tukey HSD (Post-hoc analysis)
🚀 How to Run the Code
Clone the repository:
git clone [https://github.com/YOUR_USERNAME/cycling-performance-analysis.git](https://github.com/YOUR_USERNAME/cycling-performance-analysis.git)
cd cycling-performance-analysis


Install dependencies:
It is recommended to use a virtual environment.
pip install -r requirements.txt


Run the analysis script:
python analysis_code.py


Check the results:
The script will generate the following files in your directory:
figure_1_boxplot.png
figure_2_interaction.png
figure_3_residuals.png
figure_4_distribution.png
anova_results.csv
summary_statistics.csv
tukey_results.txt
👤 Author
Mohamed Abedelrhman Zaky Azzam Aspiring Data Scientist | M.Sc. Applicant
