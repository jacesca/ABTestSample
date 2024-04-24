# AB Test
Sample code to make a simple A/B Test.

Features:
- A/B Test to determine significance of the results when normal distributions and variance are equals.
- A/B Test to determine significance of the results when normal distributions and variance are not equals.
- A/B Test to determine significance of the results when non normal distributions.
- A/A Test to determine no difference in the control samples.
- Shapiro-Wilk test to confirm if the distribution is nornal.
- Mann-Whitney U test to confirm if 2 series have the same distribution.
- Levene test to confirm if 2 sets have the same variance.
- T-test to confirm if 2 independent samples have identical average (expected) values.
- Colored terminal text.
- Tick label font size in plots.
- Subplots.

## Installing using GitHub
- Fork the project into your GitHub
- Clone it into your dektop
```
git clone https://github.com/jacesca/ABTestSample.git
```
- Setup environment (it requires python3)
```
python -m venv venv
source venv/bin/activate  # for Unix-based system
venv\Scripts\activate  # for Windows
```
- Install requirements
```
pip install -r requirements.txt
```

## Run ML model
For A/A Test
```
python AATest.py
```

Observing all statistics at once (not including A/B Test):
```
python GetStatistics.py
python ImprovedMetrics.py
```

For A/B Test related to the gathering metrics
```
python ABTestImpressions.py
python ABTestEarning.py
python ABTestClicks.py
python ABTestPurchase.py
python ABTestNoNormal.py
```

## Others
- Proyect in GitHub: https://github.com/jacesca/ABTestSample
- Commands to save the environment requirements:
```
conda list -e > requirements.txt
# or
pip freeze > requirements.txt

conda env export > env.yml
```
- For coding style
```
black model.py
flake8 model.py
```

## Extra documentation
- [shapiro to test if the distribution is nornal (p>0.05)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html)
- [mannwhitneyu to test if 2 series have the same distribution (p>0.05)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html)
- [levene to test if 2 sets have the same variance (p>0.05)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levene.html)
- [ttest_ind to test that 2 independent samples have identical average (expected) values](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)
- [Colored terminal text](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal)
- [How to change tick label font size](https://stackoverflow.com/questions/6390393/how-to-change-tick-label-font-size)
- [How to plot in multiple subplots](https://stackoverflow.com/questions/31726643/how-to-plot-in-multiple-subplots)
- [Increase tick label font size in seaborn](https://stackoverflow.com/questions/42404154/increase-tick-label-font-size-in-seaborn)
