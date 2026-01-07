import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy import stats

# Set plot style for academic report
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 12, 'font.family': 'serif'})

def load_and_clean_data(filepath):
    """
    Loads data handling the space separation and quotes.
    """
    print(f"--- Loading Data from {filepath} ---")
    try:
        # The data uses space delimiters but wraps strings in quotes.
        df = pd.read_csv(filepath, sep=' ', quotechar='"')
        print("Data loaded successfully.")
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    
    # Check for missing values
    missing = df.isnull().sum()
    print("\nMissing Values:\n", missing)
    
    # Ensure categorical ordering (optional but good for plots)
    stage_order = ['flat', 'hills', 'mount']
    # Adjust rider_order based on data if needed, but categorical typing is generally good practice
    
    # Filter only if categories exist in data to avoid errors
    existing_stages = [x for x in stage_order if x in df['stage_class'].unique()]
    if existing_stages:
        df['stage_class'] = pd.Categorical(df['stage_class'], categories=existing_stages, ordered=True)
    
    return df

def perform_descriptive_analysis(df):
    """
    Generates summary tables and visualizations (Task a).
    """
    print("\n--- Descriptive Analysis ---")
    
    # Summary Statistics: Mean and SD of points by Rider Class and Stage Class
    summary = df.groupby(['rider_class', 'stage_class'], observed=True)['points'].agg(['mean', 'std', 'count', 'median'])
    print("Summary Table (Means & SD):")
    print(summary)
    summary.to_csv("summary_statistics.csv")
    
    # Visualization 1: Boxplot (Distribution)
    plt.figure(figsize=(12, 8))
    sns.boxplot(data=df, x='stage_class', y='points', hue='rider_class', palette='viridis')
    plt.title('Distribution of Points Scored by Stage and Rider Class')
    plt.ylabel('Points')
    plt.xlabel('Stage Classification')
    plt.legend(title='Rider Class', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('figure_1_boxplot.png')
    print("Saved figure_1_boxplot.png")

    # Visualization 2: Interaction Plot (Mean Performance)
    plt.figure(figsize=(10, 6))
    sns.pointplot(data=df, x='stage_class', y='points', hue='rider_class', errorbar=('ci', 95), capsize=.1, palette='viridis')
    plt.title('Interaction Effect: Mean Points by Condition')
    plt.ylabel('Mean Points')
    plt.xlabel('Stage Classification')
    plt.tight_layout()
    plt.savefig('figure_2_interaction.png')
    print("Saved figure_2_interaction.png")

    # Visualization 4: Overall Distribution of Points (New Addition)
    plt.figure(figsize=(10, 6))
    sns.histplot(df['points'], bins=30, kde=False, color='skyblue', edgecolor='black')
    plt.title('Overall Distribution of Points Scored')
    plt.xlabel('Points')
    plt.ylabel('Frequency')
    plt.yscale('log') # Log scale helps see the small number of high scores vs many zeros
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('figure_4_distribution.png')
    print("Saved figure_4_distribution.png")

def perform_inferential_analysis(df):
    """
    Performs Two-Way ANOVA and Assumptions check (Task b).
    """
    print("\n--- Inferential Analysis (Two-Way ANOVA) ---")
    
    # 1. Fit the model
    # Model: points = Rider_Class + Stage_Class + (Rider_Class * Stage_Class)
    model = ols('points ~ C(rider_class) + C(stage_class) + C(rider_class):C(stage_class)', data=df).fit()
    
    # 2. ANOVA Table
    anova_table = sm.stats.anova_lm(model, typ=2)
    print("ANOVA Results:")
    print(anova_table)
    anova_table.to_csv("anova_results.csv")
    
    # 3. Check Assumptions (Normality of Residuals)
    residuals = model.resid
    shapiro_test = stats.shapiro(residuals)
    print(f"\nShapiro-Wilk Test for Normality: W={shapiro_test.statistic:.4f}, p={shapiro_test.pvalue:.4f}")
    
    # Visualization 3: Histogram of residuals
    plt.figure(figsize=(8, 6))
    sns.histplot(residuals, kde=True)
    plt.title('Histogram of Model Residuals')
    plt.xlabel('Residual Value')
    plt.savefig('figure_3_residuals.png')
    print("Saved figure_3_residuals.png")
    
    # 4. Post-hoc Analysis (Tukey HSD)
    # We combine classes to test the interaction specifically
    print("\n--- Post-Hoc Analysis (Tukey HSD) ---")
    df['interaction_group'] = df['rider_class'].astype(str) + " - " + df['stage_class'].astype(str)
    tukey = pairwise_tukeyhsd(endog=df['points'], groups=df['interaction_group'], alpha=0.05)
    
    # Save Tukey results to text file
    with open("tukey_results.txt", "w", encoding="utf-8") as f:
        f.write(str(tukey.summary()))
    print("Saved tukey_results.txt")

if __name__ == "__main__":
    # Ensure the csv file is in the same directory
    df = load_and_clean_data('data_report.csv')
    
    if df is not None:
        perform_descriptive_analysis(df)
        perform_inferential_analysis(df)
        print("\nAnalysis Complete. Check the generated PNG and CSV files for your report.")