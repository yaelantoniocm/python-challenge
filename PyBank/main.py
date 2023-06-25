import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")


class Main:
    def budget_data_analyzer(budget_csv):
        # Variables
        months = 0
        total_calculate = 0
        changes = []
        greatest_increase_profits = ["", 0]
        greatest_decrease_profits = ["", 0]
        previous_month_profit = 0

        # Read in the CSV file
        with open(budget_csv, 'r') as csvfile:
            # Crea un lector CSV
            csv_reader = csv.reader(csvfile)

            # Skip the header row
            header = next(csv_reader)

            for row in csv_reader:
                # For each row traversed, the vairable of total months is increased by 1
                months += 1
                # We extract the "Profit/Losses" over the entire period
                profit = int(row[1])
                # We get the total
                total_calculate += profit

                ''' 
                The change in profit/loss can be calculate wit change = actual value - previous month value
                By checking if previous month profit is not equal to zero before calculating the change, 
                we avoid including the first row of data in the changes and ensure that the average is calculated correctly.
                For example, in the first iteration the first value is 1088983 is saying profit = 0 and previous_month_profit = 0,
                so 1088983 will be add to changes, this will change the average
                We calculate here previous month value
                '''
                if previous_month_profit != 0:
                    change = profit - previous_month_profit
                    # Here we add on our list changes
                    changes.append(change)

                    # We check if the current change is the greatest increase or decrease
                    if change > greatest_increase_profits[1]:
                        greatest_increase_profits = [row[0], change]
                    if change < greatest_decrease_profits[1]:
                        greatest_decrease_profits = [row[0], change]

                # Update the previous profit/loss value for the next iteration
                previous_month_profit = profit

        # Calculate the average change
        average_change = sum(changes) / len(changes)

        # for elemt in changes:
        # print(elemt)

        # for elemt in greatest_decrease_profits:
        # print(elemt)

        # Print the analysis results
        print("Financial Analysis")
        print("-------------------------")
        print(f"Total Months: {months}")
        print(f"Total: ${total_calculate}")
        print(f"Average Change: ${average_change:.2f}")
        print(
            f"Greatest Increase in Profits: {greatest_increase_profits[0]} (${greatest_increase_profits[1]})")
        print(
            f"Greatest Decrease in Profits: {greatest_decrease_profits[0]} (${greatest_decrease_profits[1]})")


if __name__ == "__main__":
    analyzer = Main
    analyzer.budget_data_analyzer(budget_csv)
