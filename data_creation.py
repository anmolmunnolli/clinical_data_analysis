import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set the number of data points
num_data_points = 10000

# Generate dummy patient IDs
patient_ids = [f"P{i:05d}" for i in range(1, num_data_points + 1)]

# Generate demographic data
np.random.seed(42)  # For reproducibility
ages = np.random.normal(loc=60, scale=15, size=num_data_points).astype(int)
ages = np.clip(ages, 18, 85)  # Ensure ages are within 18 to 85
genders = np.random.choice(['Male', 'Female'], p=[0.48, 0.52], size=num_data_points)
races = np.random.choice(['White', 'Black', 'Asian', 'Hispanic', 'Other'], p=[0.6, 0.15, 0.1, 0.1, 0.05], size=num_data_points)
locations = np.random.choice(['USA', 'Canada', 'UK', 'Germany', 'India'], p=[0.4, 0.15, 0.2, 0.15, 0.1], size=num_data_points)

# Generate treatment data
treatment_arms = np.random.choice(['Drug A', 'Drug B', 'Placebo'], p=[0.4, 0.4, 0.2], size=num_data_points)
dosages = np.random.choice([50, 100, 150, 200], p=[0.25, 0.35, 0.3, 0.1], size=num_data_points)
start_dates = [datetime(2023, 1, 1) + timedelta(days=int(np.random.normal(loc=30, scale=15))) for _ in range(num_data_points)]
end_dates = [start_date + timedelta(days=int(np.random.normal(loc=90, scale=30))) for start_date in start_dates]

# Generate adverse event data
adverse_event_types = np.random.choice(['None', 'Mild', 'Moderate', 'Severe', 'Life-threatening'], p=[0.6, 0.2, 0.1, 0.08, 0.02], size=num_data_points)
adverse_event_counts = np.random.poisson(1, size=num_data_points)

# Generate efficacy outcome data
response_rates = np.random.normal(loc=70, scale=15, size=num_data_points)
response_rates = np.clip(response_rates, 0, 100)  # Ensure response rates are between 0 and 100
primary_endpoints = np.random.choice(['Met', 'Not Met'], p=[0.6, 0.4], size=num_data_points)
secondary_endpoints = np.random.choice(['Improved', 'No Change', 'Worsened'], p=[0.5, 0.3, 0.2], size=num_data_points)

# Generate visit compliance data
visits_scheduled = np.random.randint(5, 15, size=num_data_points)
visits_completed = np.random.binomial(visits_scheduled, p=0.8)  # 80% average completion rate

# Generate patient-reported outcomes (PROs)
quality_of_life_scores = np.random.normal(loc=70, scale=20, size=num_data_points)
quality_of_life_scores = np.clip(quality_of_life_scores, 0, 100)  # Score from 0 to 100

# Create a DataFrame with the generated data
df = pd.DataFrame({
    'PatientID': patient_ids,
    'Age': ages,
    'Gender': genders,
    'Race': races,
    'Location': locations,
    'TreatmentArm': treatment_arms,
    'Dosage_mg': dosages,
    'TreatmentStartDate': start_dates,
    'TreatmentEndDate': end_dates,
    'AdverseEventType': adverse_event_types,
    'AdverseEventCount': adverse_event_counts,
    'ResponseRate_Percent': response_rates,
    'PrimaryEndpoint': primary_endpoints,
    'SecondaryEndpoint': secondary_endpoints,
    'VisitsScheduled': visits_scheduled,
    'VisitsCompleted': visits_completed,
    'QualityOfLifeScore': quality_of_life_scores
})

# Save the DataFrame to a CSV file
df.to_csv('clinical_trial_realistic_data.csv', index=False)
