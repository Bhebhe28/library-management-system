import pandas as pd
import matplotlib.pyplot as plt

def perform_data_analysis():
    # Read the dataset
    insurance_data = pd.read_csv('motor_insure.csv')

    # Inspect column by displaying the first 10 records
    print("First 10 records of the dataset:")
    print(insurance_data.head(10))

    # Display records for make and usage for sets_num that are more than 40
    filtered_data = insurance_data[insurance_data['sets_num'] > 40]
    print("\nRecords for make and usage where sets_num > 40:")
    print(filtered_data[['make', 'usage']])

    # Plot a basic graph showing effective_yr on y-axis and carrying capacity on x-axis
    plt.scatter(insurance_data['carrying_capacity'], insurance_data['effective_yr'])
    plt.xlabel('Carrying Capacity')
    plt.ylabel('Effective Year')
    plt.title('Carrying Capacity vs Effective Year')
    plt.show()
