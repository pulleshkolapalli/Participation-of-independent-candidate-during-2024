# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for plots
sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

# Load the dataset (handling encoding issues)
file_path = "C:\\Users\\anand\\Downloads\\ElectionData.csv"
try:
    df = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='latin1')

# Basic information about dataset
print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe(include='all'))

# Handling missing data
print("\nMissing Values Before:")
print(df.isnull().sum())

df.fillna(0, inplace=True)  # Fill NaN with 0 for simplicity

print("\nMissing Values After:")
print(df.isnull().sum())

# Objective 1: District-wise Voter Distribution Analysis
if 'Total' in df.columns:
    plt.figure()
    sns.histplot(df['Total'], bins=20, kde=True, color='skyblue')
    plt.title('District-wise Voter Distribution')
    plt.xlabel('Total Votes')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# Objective 2: Candidate Vote Share Comparison
if 'Code Name' in df.columns and 'Category' in df.columns and 'Total' in df.columns:
    vote_data = df[df['Code Name'] == 'S01_1']  # Example filter
    if not vote_data.empty:
        plt.figure()
        sns.barplot(x='Category', y='Total', hue='Category', data=vote_data, palette='pastel', legend=False)
        plt.title('Vote Share Comparison by Candidate Category')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# Objective 3: Winner Dominance Mapping
if 'Category' in df.columns:
    winners = df[df['Category'] == 'Candidates - Contested']
    winner_counts = winners['Category'].value_counts()

    if not winner_counts.empty:
        # Pie Chart
        plt.figure()
        plt.pie(winner_counts, labels=winner_counts.index, autopct='%1.1f%%')
        plt.title('Winner Dominance Pie Chart')
        plt.tight_layout()
        plt.show()

        # Bar Chart
        plt.figure()
        winner_counts.plot(kind='bar', color='orange')
        plt.title('Winner Dominance Bar Chart')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()

# Objective 4: Vote Correlation Insight
numerical_cols = ['Men', 'Women', 'Third Gender', 'Total']
available_cols = [col for col in numerical_cols if col in df.columns]

if len(available_cols) >= 2:
    corr = df[available_cols].corr()
    plt.figure()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap of Votes')
    plt.tight_layout()
    plt.show()

# Objective 5: Outlier Detection using Boxplot
if len(available_cols) >= 1:
    plt.figure()
    sns.boxplot(data=df[available_cols], palette='Set2')
    plt.title('Outlier Detection using Boxplot')
    plt.tight_layout()
    plt.show()

# Pairplot for variable relationships
if len(available_cols) >= 2:
    sns.pairplot(df[available_cols].sample(min(100, len(df))), diag_kind='kde')
    plt.suptitle('Pairplot of Voting Data', y=1.02)
    plt.show()

# Line Graph for Total votes
if 'Total' in df.columns:
    plt.figure()
    df['Total'].plot(kind='line', color='teal')
    plt.title('Line Graph of Total Votes')
    plt.xlabel('Index')
    plt.ylabel('Total Votes')
    plt.tight_layout()
    plt.show()

# Bar Graph for Category vs Total
if 'Category' in df.columns and 'Total' in df.columns:
    plt.figure()
    sns.barplot(x='Category', y='Total', hue='Category', data=df, palette='muted', legend=False)
    plt.title('Total Votes by Category')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
