import matplotlib.pyplot as plt
import csv

# Initializing lists
months = []
profits = []
face_wash = []
bathing_soap = []

# Reading the csv file
file_path = "data_files/company_sales_data.csv"
with open(file=file_path, mode='r') as file:
    reader = csv.DictReader(file)

    # Appending data to "months" and "totals"
    for row in reader:
        months.append(int(row["month_number"]))
        profits.append(float(row["total_profit"]))
        face_wash.append(float(row["facewash"]))
        bathing_soap.append(float(row["bathingsoap"]))

# Line plot
plt.title("Company sales by month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.xticks(months)
plt.plot(months, profits, linewidth=2, marker=".", markersize=10)

# Subplots
figure, axes = plt.subplots(2, 1)

axes[0].plot(months, face_wash)
axes[0].set_title("Face Wash Sales")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Sales")
axes[0].set_xticks(months)
axes[1].plot(months, bathing_soap)
axes[1].set_title("Bathing soap Sales")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Sales")
axes[1].set_xticks(months)

# Showing plots
plt.tight_layout()
plt.show()