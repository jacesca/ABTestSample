"""
Let's formulate hypotheses:
H₀: There is no statistically significant difference between the means of the
    two samples.
Hₐ: There is a statistically significant difference between the means of the
    two samples.
"""
import pandas as pd
from scipy.stats import mannwhitneyu


# Read .csv file
control_group_1 = pd.read_csv('data/updated_first.csv')
control_group_2 = pd.read_csv('data/updated_second.csv')


# Print dataframe info
print('Control Group 1:', control_group_1.info(), sep='\n', end='\n\n')
print('Control Group 2:', control_group_2.info(), sep='\n', end='\n\n')

# Define metric
control_group_1['Conversion'] = (control_group_1['Purchase']/control_group_1['Page view']).round(2)  # noqa
control_group_2['Conversion'] = (control_group_2['Purchase']/control_group_2['Page view']).round(2)  # noqa

# Print head of dataframe
print('Control Group 1:')
print(control_group_1.head(), sep='\n', end='\n\n')
print('Control Group 2:')
print(control_group_2.head(), sep='\n', end='\n\n')

# Do U-Test
stat, p = mannwhitneyu(control_group_1['Conversion'], control_group_2['Conversion'])  # noqa


# Identify the test result
print(f'stat = {stat:.3f}, p={p:.3f}')
CRED = '\033[92m'
CEND = '\033[0m'
if p > 0.05:
    msg = 'There is no statistically significant difference between the medians of the two samples'  # noqa
else:
    msg = 'There is a statistically significant difference between the medians of the two samples'  # noqa

print(CRED + msg + CEND, end='\n\n')
