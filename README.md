# Mean-Reversion

Introduction

With this report, we intend to study the behavior of two main variables and understand how their relationship has evolved over time in order      to draw a line and find general rules holding in the long-run.

Business Question

With this purpose, we have selected the stock price of Apple (“AAPL”) and Microsoft (“MSFT”) and wrote a code to answer one main business question:
Does the spread between the price of the two Tech giants follow a mean reverting path?

Plan

1) Define dataset, we downloaded the relevant price data from yahoo Finance and made sure the data downloaded for each symbol is of the same length.

2) Plot the two stocks price series against each other to get a visual representation. In order to understand how strong is the correlation we can use an easy way to get a clearer visual representation of this by using a Seaborn “jointplot” as follows:

3) Run an Ordinary Least Squares regression on the closing prices to calculate a hedge ratio. Use the hedge ratio to generate the spread between the two prices,

4) Run an Augmented Dickey Fuller test on the spread to confirm statistically whether the series is mean reverting or not

5) Conclusions
