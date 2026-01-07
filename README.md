# Cycling Performance Analysis 🚴‍♂️📊

## Statistical Analysis of Rider Performance in Professional Cycling

This repository contains the source code and data for a statistical analysis project investigating the relationship between cyclist physiology (**Rider Class**) and terrain (**Stage Class**).  
The project was developed as part of an application task for the **M.Sc. Data Science program at TU Dortmund University**.

---

## 📌 Project Overview
In professional cycling, a rider's value is often conditional on the terrain.  
This project applies statistical methods to quantify:

- Whether there are significant performance differences between rider classes (Sprinters, Climbers, All Rounders, etc.).
- Whether these differences depend on the stage profile (Flat, Hills, Mountain).

The analysis utilizes:
- **Two-Way ANOVA** to test for interaction effects.
- **Tukey's HSD** for post-hoc pairwise comparisons.

---

## 📂 Repository Structure
- `analysis_code.py` → Main Python script for data cleaning, statistical analysis, and visualization.
- `data_report.csv` → Dataset containing rider performance records.
- `requirements.txt` → List of Python dependencies required to run the code.
- `output/` → Generated after running the script. Contains:
  - Plots (`.png`)
  - Statistical results (`.csv`, `.txt`)

---

## 📊 Key Findings
- **Interaction Effect**: Highly significant interaction between Rider Class and Stage Class (*p < 0.001*), confirming that performance is strictly terrain-dependent.  
- **Specialization**: Sprinters dominate Flat stages but underperform significantly on Mountain stages.  
- **Versatility**: *All Rounders* proved to be the most versatile class, showing the highest average performance on Mountain stages in this simulation.  

---

## 🛠️ Methodology
- **Language**: Python 3.10+
- **Libraries**:
  - `pandas` → Data manipulation
  - `seaborn` & `matplotlib` → Visualization
  - `statsmodels` & `scipy` → Statistical testing

### Statistical Tests Applied
- Two-Way ANOVA (Analysis of Variance)  
- Shapiro-Wilk Test (Normality check)  
- Levene's Test (Homogeneity of Variance)  
- Tukey HSD (Post-hoc analysis)  

---

## 🚀 How to Run the Code

Clone the repository:
```bash
git clone https://github.com/MohamedAzzam4/tu-dortmund-application-task.git
cd tu-dortmund-application-task
