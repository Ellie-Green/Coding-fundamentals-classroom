import csv 

companies = []
sales = []

with open("labs/outputs.csv", "r") as file:
    reader = csv.reader(file)
    lines = list(reader)

for x in range(0, len(lines), 2):
    companies.append(lines[x][0].strip())
    data = lines[x+1][0].strip().split(",")
    sales.append([int(item) for item in data])  


monthly_totals = [sum(month) for month in zip(*sales)]
grand_total = sum(sum(month)for month in sales)

print("Sum of cars sold in each month: ")
for month, total in enumerate(monthly_totals, start=1):
    print(f"{month}/{2019}: {total}")

print("\n. Total yearly sales by each manufacturer: ")
for company, total_sales in zip(companies, [sum(month) for month in sales]):
    print(f"{company}: {total_sales} cars.")

print(f"\n Grand total: {grand_total}")