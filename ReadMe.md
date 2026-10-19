# HR Employee Attrition Analysis

## Project Overview

This project analyzes employee attrition using Python, Pandas, and Matplotlib. It explores employee data to identify patterns associated with employees leaving an organization and presents the findings through summary tables and visualizations.

The goal is to demonstrate practical data analysis skills and translate data into insights that could help HR teams investigate employee retention.

## Business Questions

- What is the overall employee attrition rate?
- Which job roles have the highest attrition rates?
- How is attrition associated with working overtime?
- How does job satisfaction relate to attrition?
- How does attrition vary across monthly income groups?
- How do job satisfaction and overtime together relate to attrition?

## Dataset

The dataset was obtained from Kaggle:

- **Title:** IBM HR Analytics Employee Attrition & Performance
- **Source:** Kaggle
- **Uploader:** pavansubhash
- **Dataset link:** https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

The dataset contains fictional employee records and is used here for educational and analytical purposes.

Please consult the original Kaggle page for the current dataset license and attribution requirements.

## Tools and Technologies

- **Python** — programming and analysis
- **Pandas** — data manipulation, grouping, and aggregation
- **Matplotlib** — data visualization
- **VS Code** — development environment
- **Git and GitHub** — version control and project sharing

## Analysis Performed

### 1. Overall Attrition

Calculated the number of employees who left and the overall attrition rate.

### 2. Attrition by Job Role

Compared employee attrition rates across job roles to identify groups with higher observed turnover.

### 3. Attrition by Overtime

Compared attrition rates between employees who work overtime and those who do not.

### 4. Attrition by Job Satisfaction

Investigated differences in attrition rates across job satisfaction scores.

### 5. Attrition by Monthly Income

Divided employees into four income groups and compared their attrition rates.

### 6. Job Satisfaction and Overtime

Compared attrition rates across job satisfaction scores, split by overtime status.

## Key Findings

The exploratory analysis indicated the following patterns:

- Attrition rates differed across job roles.
- Employees working overtime had a higher observed attrition rate than employees who did not.
- Employees with a job satisfaction score of 1 had the highest observed attrition rate among the satisfaction groups.
- Lower-income groups showed higher observed attrition rates than higher-income groups.
- The combined analysis highlighted low job satisfaction and overtime as factors worth investigating together.

These findings are descriptive associations. They do not establish that any particular factor causes employees to leave. Exact rates and group sizes can be verified by running the analysis script.

## Visualizations

The script generates the following charts:

| Chart | Description |
|---|---|
| `charts/attrition_by_role.png` | Attrition rates by job role |
| `charts/attrition_by_overtime.png` | Attrition rates by overtime status |
| `charts/attrition_satisfaction_overtime.png` | Attrition rates by job satisfaction and overtime |
| `charts/attrition_by_income.png` | Attrition rates by monthly income group |

## Project Structure

```text
hr-attrition-analysis/
├── hr_data.csv
├── analysis.py
├── README.md
├── role_summary.csv
├── overtime_summary.csv
├── satisfaction_overtime_summary.csv
├── income_summary.csv
└── charts/
    ├── attrition_by_role.png
    ├── attrition_by_overtime.png
    ├── attrition_satisfaction_overtime.png
    └── attrition_by_income.png
```

The CSV summary files and chart images are generated when the script runs.

## How to Run the Project

### Prerequisites

Install Python and the required libraries.

```bash
python -m pip install pandas matplotlib
```

### Run the analysis

Make sure `hr_data.csv` is in the project directory, then run:

```bash
python analysis.py
```

The script prints summary tables, exports CSV files, and saves the charts in the `charts/` directory.

## Limitations

- This is exploratory data analysis, not a causal study.
- Differences in attrition may be associated with several interacting factors.
- Group sizes should be considered when comparing percentages.
- Further statistical testing would be needed to assess the strength and uncertainty of the observed relationships.
- Predictive modeling would require a separate evaluation process and appropriate validation metrics.

## Future Improvements

- Investigate additional variables such as age, job level, tenure, and work environment.
- Perform statistical analysis of the observed differences.
- Build and evaluate a machine-learning model to predict employee attrition.
- Develop an interactive dashboard to present findings.
- Add model evaluation metrics such as precision, recall, and ROC-AUC if predictive modeling is implemented.

## Skills Demonstrated

Python, Pandas, data aggregation, exploratory data analysis, data visualization, business interpretation, and analytical reporting.

## Author

**Azeem**

This project was developed as part of my practical learning in data analysis and my broader studies in Artificial Intelligence.
