# Importing the libraries
import numpy as np
import pandas as pd
from csv import reader
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt

# Function to read the dataset and prepare transactions
def read_and_prepare_data(file_path):
    groceries = []
    with open(file_path, 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            groceries.append(row)

    encoder = TransactionEncoder()
    transactions = encoder.fit_transform(groceries)
    df = pd.DataFrame(transactions, columns=encoder.columns_)
    return df

# Function to find related items for a given item
def find_related_items(input_item, frequent_itemsets):
    rules = association_rules(frequent_itemsets, metric='support', min_threshold=0.001)
    filtered_rules = rules[rules['antecedents'].apply(lambda x: input_item in x)].copy()
    
    filtered_rules.drop_duplicates(subset={'antecedents', 'consequents'}, inplace=True)
    
    related_items = []
    for _, row in filtered_rules.iterrows():
        antecedents = row['antecedents']
        consequents = row['consequents']
        support_percentage = row['support'] * 100
        related_items.append({
            'Antecedents': ', '.join(antecedents),
            'Consequents': ', '.join(consequents),
            'Support Percentage': support_percentage
        })

    return related_items

# Function to plot the top frequent itemsets with two items
def plot_top_frequent_itemsets(frequent_itemsets):
    two_itemsets = frequent_itemsets[frequent_itemsets['itemsets'].apply(lambda x: len(x) == 2)]
    top_10_two_itemsets = two_itemsets.sort_values(by='support', ascending=False).head(10)
    top_10_two_itemsets['itemsets_str'] = top_10_two_itemsets['itemsets'].apply(lambda x: ', '.join(x))
    
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(top_10_two_itemsets)), top_10_two_itemsets['support'], tick_label=top_10_two_itemsets['itemsets_str'])
    plt.xlabel('Frequent Itemsets (Two Items)')
    plt.ylabel('Support')
    plt.title('Top 10 Frequent Itemsets with Two Items')
    plt.xticks(rotation=90)
    plt.show()

# Function to find support percentage between two items
def find_support_percentage_between_two_items(item1, item2, frequent_itemsets):
    rules = association_rules(frequent_itemsets, metric='support', min_threshold=0.001)
    filtered_rules = rules[
        (rules['antecedents'].apply(lambda x: item1 in x) & rules['consequents'].apply(lambda x: item2 in x)) |
        (rules['antecedents'].apply(lambda x: item2 in x) & rules['consequents'].apply(lambda x: item1 in x))
    ].copy()

    filtered_rules.drop_duplicates(subset={'antecedents', 'consequents'}, inplace=True)

    if not filtered_rules.empty:
        return filtered_rules.iloc[0]['support'] * 100
    else:
        return 0

# Example usage
file_path = '/Users/chkv/Downloads/groceries.csv'  # Change 'your_username' to your actual username
data = read_and_prepare_data(file_path)
frequent_itemsets = apriori(data, min_support=0.01, use_colnames=True)

input_item = 'butter'
related_items = find_related_items(input_item, frequent_itemsets)
for item in related_items:
    print(f"Antecedents: {item['Antecedents']}")
    print(f"Consequents: {item['Consequents']} ({item['Support Percentage']:.2f}%)")
    print('-' * 40)

item1 = 'other vegetables'
item2 = 'whole milk'
support_percentage = find_support_percentage_between_two_items(item1, item2, frequent_itemsets)
print(f"The support percentage between '{item1}' and '{item2}' is: {support_percentage:.2f}%")

plot_top_frequent_itemsets(frequent_itemsets)
