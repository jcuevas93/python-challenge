import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")
output_folder = "analysis"
output_text_file = os.path.join(output_folder, "financial_analysis.txt")

# Create the analysis folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


total_months = 0
net_total = 0
previous_profit_loss = 0
profit_loss_changes = []
months = []

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")

    # Read through each row of data
    for row in csv_reader:
        # Calculate total number of months
        total_months += 1

        # Calculate net total amount of "Profit/Losses"
        net_total += int(row["Profit/Losses"])

        # Calculate changes in "Profit/Losses" over the entire period
        if total_months > 1:
            profit_loss_change = int(row["Profit/Losses"]) - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)
            months.append(row["Date"])

        previous_profit_loss = int(row["Profit/Losses"])

# Calculate the average of changes in "Profit/Losses" over the entire period
average_change = sum(profit_loss_changes) / (total_months - 1)

# Find the greatest increase and decrease in profits
max_increase = max(profit_loss_changes)
max_decrease = min(profit_loss_changes)

# Find the corresponding dates for greatest increase and decrease
max_increase_date = months[profit_loss_changes.index(max_increase)]
max_decrease_date = months[profit_loss_changes.index(max_decrease)]

# Print the analysis results
analysis_results = (
    "Financial Analysis\n"
    "-----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n"
    f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})"
)

print(analysis_results)

# Write the analysis results to a text file in the 'analysis' folder
with open(output_text_file, "w") as output_file:
    output_file.write(analysis_results)

print(f"Analysis results have been exported to {output_text_file}")
