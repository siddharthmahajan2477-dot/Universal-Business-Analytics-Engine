import csv
import os
from datetime import datetime
from collections import defaultdict

FILE_NAME = "business_data.csv"

def create_csv():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Date",
                "Product",
                "Category",
                "Region",
                "Units",
                "Revenue",
                "Cost"
            ])

            # Sample Universal Business Data
            writer.writerow(["01-01-2026", "Laptop", "Electronics", "North", 5, 50000, 35000])
            writer.writerow(["15-01-2026", "Phone", "Electronics", "South", 8, 32000, 20000])
            writer.writerow(["28-01-2026", "Shoes", "Fashion", "West", 15, 30000, 18000])

            writer.writerow(["05-02-2026", "Laptop", "Electronics", "North", 6, 60000, 42000])
            writer.writerow(["18-02-2026", "Watch", "Accessories", "East", 10, 25000, 15000])
            writer.writerow(["25-02-2026", "Shoes", "Fashion", "West", 12, 24000, 14000])

            writer.writerow(["03-03-2026", "Laptop", "Electronics", "North", 7, 70000, 49000])
            writer.writerow(["12-03-2026", "Phone", "Electronics", "South", 9, 36000, 22000])
            writer.writerow(["22-03-2026", "Watch", "Accessories", "East", 14, 35000, 20000])

        print("Sample business dataset created.\n")
        
def load_data():
    records = []

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["Units"] = int(row["Units"])
            row["Revenue"] = float(row["Revenue"])
            row["Cost"] = float(row["Cost"])
            row["Profit"] = row["Revenue"] - row["Cost"]

            # Extract month for trend analysis
            row["Month"] = datetime.strptime(
                row["Date"], "%d-%m-%Y"
            ).strftime("%Y-%m")

            records.append(row)

    return records

def financial_overview():
    data = load_data()

    total_revenue = sum(record["Revenue"] for record in data)
    total_cost = sum(record["Cost"] for record in data)
    total_profit = sum(record["Profit"] for record in data)

    profit_margin = 0
    if total_revenue != 0:
        profit_margin = (total_profit / total_revenue) * 100

    print("\n==============================")
    print("FINANCIAL OVERVIEW")
    print("==============================")
    print(f"Total Revenue : ₹{total_revenue:,.2f}")
    print(f"Total Cost    : ₹{total_cost:,.2f}")
    print(f"Total Profit  : ₹{total_profit:,.2f}")
    print(f"Profit Margin : {profit_margin:.2f}%")

    if total_profit > 0:
        print("Status        : Business is Profitable")
    elif total_profit < 0:
        print("Status        : Business is in Loss")
    else:
        print("Status        : Break-even")
        
def product_performance():
    data = load_data()

    product_revenue = defaultdict(float)
    product_profit = defaultdict(float)

    for record in data:
        product = record["Product"]
        product_revenue[product] += record["Revenue"]
        product_profit[product] += record["Profit"]

    # Rank by profit
    ranked_products = sorted(
        product_profit.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print("\n==============================")
    print("PRODUCT PERFORMANCE")
    print("==============================")

    for index, (product, profit) in enumerate(ranked_products, start=1):
        revenue = product_revenue[product]
        print(f"{index}. {product}")
        print(f"   Revenue : ₹{revenue:,.2f}")
        print(f"   Profit  : ₹{profit:,.2f}")
        print("----------------------------------")

    if ranked_products:
        top_product = ranked_products[0][0]
        weakest_product = ranked_products[-1][0]

        print(f"Top Performing Product    : {top_product}")
        print(f"Weakest Performing Product: {weakest_product}")
        
def category_analysis():
    data = load_data()

    category_units = defaultdict(int)
    category_revenue = defaultdict(float)
    category_profit = defaultdict(float)

    for record in data:
        category = record["Category"]
        category_units[category] += record["Units"]
        category_revenue[category] += record["Revenue"]
        category_profit[category] += record["Profit"]

    # Rank categories by demand (units sold)
    ranked_categories = sorted(
        category_units.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print("\n==============================")
    print("CATEGORY ANALYSIS")
    print("==============================")

    for index, (category, units) in enumerate(ranked_categories, start=1):
        revenue = category_revenue[category]
        profit = category_profit[category]

        print(f"{index}. {category}")
        print(f"   Units Sold : {units}")
        print(f"   Revenue    : ₹{revenue:,.2f}")
        print(f"   Profit     : ₹{profit:,.2f}")
        print("----------------------------------")

    if ranked_categories:
        top_category = ranked_categories[0][0]
        print(f"Highest Demand Category: {top_category}")
        
def region_analysis():
    data = load_data()

    region_units = defaultdict(int)
    region_revenue = defaultdict(float)
    region_profit = defaultdict(float)

    for record in data:
        region = record["Region"]
        region_units[region] += record["Units"]
        region_revenue[region] += record["Revenue"]
        region_profit[region] += record["Profit"]

    # Rank regions by profit
    ranked_regions = sorted(
        region_profit.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print("\n==============================")
    print("REGION PERFORMANCE")
    print("==============================")

    for index, (region, profit) in enumerate(ranked_regions, start=1):
        revenue = region_revenue[region]
        units = region_units[region]
        margin = (profit / revenue * 100) if revenue != 0 else 0

        print(f"{index}. {region}")
        print(f"   Units Sold : {units}")
        print(f"   Revenue    : ₹{revenue:,.2f}")
        print(f"   Profit     : ₹{profit:,.2f}")
        print(f"   Margin     : {margin:.2f}%")
        print("----------------------------------")

    if ranked_regions:
        strongest_region = ranked_regions[0][0]
        weakest_region = ranked_regions[-1][0]

        print(f"Strongest Region : {strongest_region}")
        print(f"Weakest Region   : {weakest_region}")
        
def trend_analysis():
    data = load_data()

    monthly_revenue = defaultdict(float)

    for record in data:
        month = record["Month"]
        monthly_revenue[month] += record["Revenue"]

    sorted_months = sorted(monthly_revenue.items())

    print("\n==============================")
    print("MONTHLY TREND ANALYSIS")
    print("==============================")

    previous_revenue = None

    for month, revenue in sorted_months:
        print(f"{month} : ₹{revenue:,.2f}")

        if previous_revenue is not None:
            growth = ((revenue - previous_revenue) / previous_revenue) * 100
            if growth > 0:
                print(f"   Growth  : {growth:.2f}% ↑")
            elif growth < 0:
                print(f"   Decline : {abs(growth):.2f}% ↓")
            else:
                print("   No Change")

        previous_revenue = revenue
        
def executive_summary():
    data = load_data()

    total_revenue = sum(r["Revenue"] for r in data)
    total_profit = sum(r["Profit"] for r in data)

    # Top Product
    product_profit = defaultdict(float)
    for r in data:
        product_profit[r["Product"]] += r["Profit"]

    ranked_products = sorted(product_profit.items(), key=lambda x: x[1], reverse=True)

    top_product = ranked_products[0][0]
    weakest_product = ranked_products[-1][0]

    # Top Category
    category_units = defaultdict(int)
    for r in data:
        category_units[r["Category"]] += r["Units"]

    top_category = max(category_units, key=category_units.get)

    # Top Region
    region_profit = defaultdict(float)
    for r in data:
        region_profit[r["Region"]] += r["Profit"]

    strongest_region = max(region_profit, key=region_profit.get)

    print("\n==============================")
    print("EXECUTIVE BUSINESS SUMMARY")
    print("==============================")
    print(f"Total Revenue        : ₹{total_revenue:,.2f}")
    print(f"Total Profit         : ₹{total_profit:,.2f}")
    print(f"Top Product          : {top_product}")
    print(f"Weakest Product      : {weakest_product}")
    print(f"Highest Demand Cat.  : {top_category}")
    print(f"Strongest Region     : {strongest_region}")
    print("==============================")
    
def menu():
    create_csv()

    while True:
        print("\n======= UNIVERSAL BUSINESS ANALYTICS ENGINE =======")
        print("1. Financial Overview")
        print("2. Product Performance")
        print("3. Category Analysis")
        print("4. Region Analysis")
        print("5. Monthly Trend Analysis")
        print("6. Executive Summary")
        print("7. Exit")

        choice = input("Select option: ")

        if choice == "1":
            financial_overview()
        elif choice == "2":
            product_performance()
        elif choice == "3":
            category_analysis()
        elif choice == "4":
            region_analysis()
        elif choice == "5":
            trend_analysis()
        elif choice == "6":
            executive_summary()
        elif choice == "7":
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Try again.")
            
menu()