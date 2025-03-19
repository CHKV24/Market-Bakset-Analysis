# Market Basket Analysis using Apriori Algorithm

This project demonstrates **Market Basket Analysis (MBA)** using the **Apriori Algorithm** in Python. The goal is to uncover associations between products frequently bought together in a supermarket setting. The analysis helps retailers optimize product placement, create targeted promotions, and enhance customer satisfaction.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Results](#results)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

Market Basket Analysis (MBA) is a data mining technique used to identify relationships between products based on customer transaction data. The **Apriori algorithm** is a popular method for discovering frequent itemsets and generating association rules. This project provides a Python implementation of the Apriori algorithm to analyze a supermarket dataset and uncover patterns in customer purchasing behavior.

## Features

- **Data Preprocessing**: The dataset is preprocessed to convert it into a binary transaction format suitable for the Apriori algorithm.
- **Frequent Itemset Mining**: The Apriori algorithm is used to find frequent itemsets based on a specified minimum support threshold.
- **Association Rule Generation**: Association rules are generated to identify relationships between products.
- **Visualization**: The top 10 frequent itemsets with two items are visualized using a bar plot.
- **Support Percentage Calculation**: The support percentage between two specific items can be calculated to understand their co-occurrence in transactions.

## Results

- **Related Items**: The script identifies items frequently bought together with a specified input item.
- **Support Percentage**: The support percentage between two items is calculated to understand their co-occurrence in transactions.
- **Visualization**: A bar plot of the top 10 frequent itemsets with two items is generated.

**Example Output**:
Antecedents: butter Consequents: whole milk (5.22%)
The support percentage between 'other vegetables' and 'whole milk' is: 7.48%

## Conclusion

This project demonstrates how to use the Apriori algorithm for Market Basket Analysis in Python. By analyzing customer transaction data, retailers can uncover valuable insights into product associations and optimize their marketing strategies. The script is flexible and can be adapted to different datasets and retail scenarios.

## References

- B. Ganguly Raich and M. Tota, "Machine Learning for Market Basket Analysis through", IOSR Journal of Engineering (IOSRJEN), pp. 22-23, 2019.
- M. Kaur and S. Kang, "Market Basket Analysis: Identify the changing trends of market data", International Conference on Computational Modeling and Security (CMS 2016), 2016.
- S. Mainali, "MARKET BASKET ANALYSIS" in GitHub, Kirtipur, 2016.
