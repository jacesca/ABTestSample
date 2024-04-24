"""
Sample of how the Descriptive Statistics can be obtained.
"""
from matplotlib import pyplot as plt
from scipy.stats import shapiro, levene
import pandas as pd
import seaborn as sns


# Global configuration
CRED = '\033[42m'
CEND = '\033[0m'

plt.rcParams.update({'axes.labelsize': 6, 'xtick.labelsize': 6,
                     'ytick.labelsize': 6, 'legend.fontsize': 6,
                     'font.size': 6})

# Read .csv file
control_group = pd.read_csv('data/ab_control.csv', delimiter=';')
test_group = pd.read_csv('data/ab_test.csv', sep=';')


# Print dataframe info
print(CRED + 'Data Frame Info' + CEND)
print('Control Group:')
print(control_group.info(), sep='\n', end='\n\n')
print('Test Group:')
print(test_group.info(), sep='\n', end='\n\n')

# Define improved metrics
new_metrics = {
    'Conversion Rate': ('Purchase', 'Click'),
    'Average Purchase Value': ('Earning', 'Purchase'),
    'Average Earning Per Click': ('Earning', 'Click'),
}
for metric in new_metrics.keys():
    control_group[metric] = control_group[new_metrics[metric][0]]/control_group[new_metrics[metric][1]]  # noqa
    test_group[metric] = test_group[new_metrics[metric][0]]/test_group[new_metrics[metric][1]]  # noqa

# Print head of dataframe
print(CRED + 'Data Frame Head' + CEND)
print('Control Group:', control_group.head(), sep='\n', end='\n\n')
print('Test Group:', test_group.head(), sep='\n', end='\n\n')

for col in new_metrics.keys():
    print(CRED + f'Statistics for {col}' + CEND)
    msg = col
    # Calculate descriptive statistics using .agg method
    control_descriptive = control_group[col].agg(['count', 'mean', 'std', 'median', 'min', 'max']).round(2)  # noqa
    test_descriptive = test_group[col].agg(['count', 'mean', 'std', 'median', 'min', 'max']).round(2)  # noqa
    # print('Control Group:', control_descriptive, sep='\n', end='\n\n')
    # print('Test Group:', test_descriptive, sep='\n', end='\n\n')

    # Concat the results of aggregations
    result = pd.concat([control_descriptive, test_descriptive], axis=1)
    result.columns = ['Control', 'Test']
    print('Aggregations Results', result, sep='\n', end='\n\n')

    # Plotting hists
    plt.figure()
    plt.subplot(2, 2, 1)
    sns.histplot(control_group[col], color='#1e2635', label='Control Group')
    plt.axvline(x=control_group[col].values.mean(), ls='--', color='black', label='Mean Control Group')  # noqa
    sns.histplot(test_group[col], color='#ff8a00', label='Test Group')
    plt.axvline(x=test_group[col].values.mean(), ls='--', color='red', label='Mean Test Group')  # noqa
    plt.legend(title='Groups')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.title(f'Distribution of {col}', fontsize=8)

    # Let's look at box plots
    control_group['group'] = 'Contol group'
    test_group['group'] = 'Test group'
    df_combined = pd.concat([control_group, test_group])
    plt.subplot(2, 2, 2)
    sns.boxplot(data=df_combined, hue='group', y=col,
                palette=['#1e2635', '#ff8a00'], medianprops={'color': 'red'})
    plt.xlabel('')
    plt.ylabel(col)
    plt.tight_layout()
    plt.title(f'Comparison of {col}', fontsize=8)

    # The Shapiro Test
    # The Shapiro Test is a statistical test that is used to test the
    # hypothesis of a normal distribution. It compares the distribution
    # of the data with a normal distribution.
    # The null hypothesis assumes that the data are normally distributed.
    # If the p-value is below the significance level (below 0.05), then the
    # null hypothesis is rejected.
    # In such a case, we can argue that the data is not normally distributed
    # (the alternative hypothesis is accepted).
    # Note:
    # If we have more than 5 000 observations, it is better to use the
    # Kolmogorov-Smirnov test.
    # Its use is similar to the Shapiro test.
    print('Shapiro Test - Control Group')
    stat_control, p_control = shapiro(control_group[col])
    print('Control group: ')
    print('Stat: %.4f, p-value: %.4f' % (stat_control, p_control))
    if p_control > 0.05:
        msg_temp = 'Control group is likely to normal distribution'
    else:
        msg_temp = 'Control group is NOT likely to normal distribution'
    msg += f'\nShapiro Test: {msg_temp}'
    print(msg, end='\n\n')

    print('Shapiro Test - Test Group')
    stat_test, p_test = shapiro(test_group[col])
    print('Test group: ')
    print('Stat: %.4f, p-value: %.4f' % (stat_test, p_test))
    if p_test > 0.05:
        msg_temp = 'Test group is likely to normal distribution'
    else:
        msg_temp = 'Test group is NOT likely to normal distribution'
    msg += f'\nShapiro Test: {msg_temp}'
    print(msg_temp, end='\n\n')

    # Swarm Plots
    colors_list = ['#ff8a00', '#33435c']
    control_group['group'] = 'Contol group'
    test_group['group'] = 'Test group'
    df_combined = pd.concat([control_group, test_group])
    plt.subplot(2, 2, 3)
    sns.swarmplot(data=df_combined, x='group', y=col, hue='group',
                  palette=colors_list)
    plt.xlabel('')
    plt.ylabel(col)
    plt.title(f'Comparison of {col}', fontsize=8)
    plt.tight_layout()

    # Violin Plots
    colors_list = ['#ff8a00', '#33435c']
    control_group['group'] = 'Contol group'
    test_group['group'] = 'Test group'
    df_combined = pd.concat([control_group, test_group])
    plt.subplot(2, 2, 4)
    sns.swarmplot(data=df_combined, x='group', y=col, hue='group',
                  palette=colors_list)
    sns.violinplot(data=df_combined, x='group', y=col, color="r",
                   alpha=0.8)
    plt.xlabel('')
    plt.ylabel(col)
    plt.title(f'Comparison of {col}', fontsize=8)
    plt.tight_layout()

    # Levene's Test
    # It is used to test the null hypothesis that the variances are equal.
    print('Levene Test - Test Group', col)
    statistic, p_value = levene(control_group[col], test_group[col])
    print('Statistic:', statistic)
    print('p-value:', p_value)
    if p_value > 0.05:
        msg_temp = 'The variances of the two groups are NOT statistically different'  # noqa
    else:
        msg_temp = 'The variances of the two groups are statistically different'  # noqa
    msg += f'\nLevene Test: {msg_temp}'
    print(msg_temp, end='\n\n')

    plt.suptitle(msg, x=0.05, horizontalalignment='left', fontsize=10)
    plt.subplots_adjust(top=0.8, hspace=.5)

# Show the graph
plt.show()
plt.style.use('default')
