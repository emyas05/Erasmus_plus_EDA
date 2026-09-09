# Bank Marketing Data Analysis

## Project Overview
This project focuses on analyzing a bank marketing dataset to identify patterns and insights related to customer subscriptions for term deposits. The dataset includes various customer attributes and campaign-related information, which are explored through data preprocessing, visualization, and clustering techniques.

## Repository Structure
- **overview.py**: Contains a function to load variable descriptions for the bank dataset.
- **Exploratory Data Analysis.ipynb**: A Jupyter Notebook that performs exploratory data analysis (EDA), including data loading, visualization, and clustering to identify customer segments based on their likelihood to subscribe to a term deposit.
- **bank.csv**: The dataset file containing customer and campaign data (not included in this repository but referenced in the notebook).

## Dataset Description
The dataset (`bank.csv`) contains information about customers and marketing campaign interactions. Key variables include:
- **age**: Customer's age.
- **job**: Type of job (e.g., admin, blue-collar, retired).
- **marital**: Marital status (e.g., married, single, divorced).
- **education**: Education level (e.g., secondary, tertiary, primary).
- **default**: Whether the customer has credit in default.
- **balance**: Average yearly balance in euros.
- **housing**: Whether the customer has a housing loan.
- **loan**: Whether the customer has a personal loan.
- **contact**: Contact communication type (e.g., cellular, telephone).
- **day**: Last contact day of the month.
- **month**: Last contact month of the year.
- **duration**: Last contact duration in seconds (for benchmarking, not prediction).
- **campaign**: Number of contacts during the current campaign.
- **pdays**: Days since last contact from a previous campaign (-1 if not contacted).
- **previous**: Number of contacts before the current campaign.
- **poutcome**: Outcome of the previous campaign (e.g., success, failure, nonexistent).
- **subscribed**: Whether the customer subscribed to a term deposit (target variable).

For a complete list and descriptions, refer to `overview.py` or the `Exploratory Data Analysis.ipynb` notebook.

## Analysis Overview
The Jupyter Notebook (`Exploratory Data Analysis.ipynb`) includes:
1. **Data Loading**: Loads the dataset and variable descriptions.
2. **Data Exploration**: Displays initial data samples and variable details.
3. **Data Visualization**: Visualizes the distribution of key numerical features (`age`, `balance`, `campaign`, `pdays`, `previous`) across clusters using histograms with kernel density estimation.
4. **Clustering Insights**:
   - **Cluster 0 (Less Engaged Group)**: Customers with lower balances, fewer previous contacts, and higher `pdays` (less recent contact). These customers are less likely to subscribe to a term deposit due to low engagement.
   - **Cluster 1 (More Engaged Group)**: Customers with higher balances, more frequent past contacts, and lower `pdays` (recent contact). These customers are more likely to subscribe due to higher engagement.

## Key Findings
- Customers with higher account balances are more likely to subscribe, indicating financial stability.
- Previous successful contacts with the bank increase subscription likelihood, suggesting trust and engagement.
- Fewer campaign contacts correlate with higher conversion rates, implying early interest among subscribers.
- Middle-aged customers (30-50 years) are more likely to subscribe compared to younger or older groups.

## Requirements
To run the notebook, ensure you have the following Python packages installed:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
