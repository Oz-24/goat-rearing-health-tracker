# Smart Livestock Health & Feed Efficiency Tracker

A lightweight, data-driven livestock monitoring script built using Python, Pandas, and NumPy. This repository serves as a portfolio project demonstrating foundational analytics workflows.

## 🐐 Project Motivation
In livestock management and sustainable farming, tracking animal Feed Conversion Ratios (FCR) is critical. FCR measures an animal's efficiency in converting feed mass into desired body weight. This application ingests herd health logs, cleans structural records containing missing field data points, and utilizes fast vectorized array transformations to dynamically highlight anomalous animal metabolic data patterns without using slow loop code blocks.

## 🛠️ Key Technical Implementations

### 1. Element-Wise Resource Calculations
To evaluate animal performance benchmarks instantly across the entire livestock cohort, metrics are translated directly into NumPy arrays. FCR values are resolved using array division operations:
⁠ python
df['Feed_Conversion_Ratio'] = feed_array / weight_gain_array
 ⁠

### 2. Automated Diagnostic Masking
Rather than using repetitive logical if-statements to check individual animals, the script leverages NumPy's vectorized ⁠ np.where() ⁠ framework to flag livestock showing symptoms of high consumption combined with low growth:
⁠ python
df['Health_Status'] = np.where(df['Feed_Conversion_Ratio'] > 15.0, 'MEDICAL CHECK', 'HEALTHY')

### 3. Missing Ledger Imputation
To compensate for real-world logging discrepancies (such as skipped scale measurements), the script implements Pandas-driven data cleaning (⁠ .fillna() ⁠) to impute missing rows with localized median benchmarks before statistical reductions are run.

## 🚀 Local Deployment Instructions

1.⁠ ⁠Clone this repository down to your computer:
   ⁠ bash
   git clone https://github.com
   cd goat-rearing-health-tracker
    ⁠

2.⁠ ⁠Run the main processing pipeline script:
   ⁠ bash
   python src/goat_analyzer.py
    ⁠

## 📊 Sample Program Outputs
Running the ledger pipeline generates the following calculations directly on the system terminal:
•⁠  ⁠*Total Daily Feed Consumed*: Summary of herd resource depletion (KG)
•⁠  ⁠*Herd Efficiency Mean*: Overall cohort conversion average index
•⁠  ⁠*Breed-Specific Analysis*: Aggregated efficiency indices isolating optimal lineage groups

