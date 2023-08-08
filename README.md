# Statistics Test Generator Dashboard

This is a web-based application built using Dash and Plotly that allows you to generate sample data from different distributions and perform statistical tests. The dashboard provides an interactive interface where you can select the data distribution type, set the sample size, and perform various statistical tests based on the selected distribution.

## Features

- Generate sample data from three different distributions: Normal, Exponential, and Uniform.
- Perform statistical tests based on the selected distribution:
  - T-Test for Normal Distribution
  - Chi-Square Test for Exponential Distribution
  - Kolmogorov-Smirnov Test for Uniform Distribution
  - F-Test for Equal Variances (when applicable)  #still under progress
- Visualize the generated data distribution using a histogram.

## How to Use
Choose the desired Data Distribution Type from the dropdown menu (Normal, Exponential, or Uniform).

Enter the Sample Size (number of data points) that we want to generate for the selected distribution.

(Optional) If the Data Distribution Type is set to "Normal," you can enter a Population Mean for performing a T-Test.

The test results and a histogram of the generated data will be displayed on the dashboard.

## Assumptions
The generated sample data follows the selected distribution.
The statistical tests assume a level of significance (alpha) of 0.05.
For the T-Test, Chi-Square Test, and Kolmogorov-Smirnov Test, the null hypothesis is tested against a two-sided alternative hypothesis.

## Limitations
The generated sample data is based on random number generation and may vary with each run.
The dashboard assumes basic understanding of statistics and statistical tests.

## Contributing
Contributions are welcome! If you have suggestions or improvements for the dashboard, feel free to open an issue or submit a pull request.

## Future improvements

- Generate button
- Checking the "Equal Variances" checkbox if we want to perform an F-Test for equal variances (applicable only for Normal Distribution).
- Adding more assumptions in the dropdown for more tests
