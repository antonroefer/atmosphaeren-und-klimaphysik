import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# Part a: Read the data and process it
file_path = "./../data//interim//klima_hamburg_TMK_TXK_TNK.csv"
data = pd.read_csv(file_path, delimiter=";")

data["DD"] = data["DD"].astype(int)
data["MM"] = data["MM"].astype(int)
data["YYYY"] = data["YYYY"].astype(int)

data["DATE"] = pd.to_datetime(
    {"year": data["YYYY"], "month": data["MM"], "day": data["DD"]}
)
data.set_index("DATE", inplace=True)

# Choose a month (e.g., July) and calculate monthly mean values
chosen_month = 7
monthly_mean = data[data["MM"] == chosen_month].groupby(data["YYYY"])["TMK"].mean()

# Plot the time series of monthly mean values
plt.figure(figsize=(10, 6))
plt.plot(
    monthly_mean.index, monthly_mean.values, marker="o", label="July Mean Temperature"
)
plt.title("Time Series of Monthly Mean Temperature (July)")
plt.xlabel("Year")
plt.ylabel("Mean Temperature (°C)")
plt.ylim(10, 25)  # Set y-axis limits between 10 and 25°C
plt.grid()
plt.legend()
plt.show()

# Calculate the first three statistical moments
mean = monthly_mean.mean()
variance = monthly_mean.var()
skewness = monthly_mean.skew()

print("a)")
print(f"Mean: {mean:.2f} °C")
print(f"Variance: {variance:.2f} °C")
print(f"Skewness: {skewness:.2f} °C\n")

# Part b: Seasonal cycle over the first and last 20 years
first_20_years = data[data["YYYY"] <= data["YYYY"].min() + 19]
last_20_years = data[data["YYYY"] >= data["YYYY"].max() - 19]

# Group by month and calculate mean for each month
seasonal_cycle_first = first_20_years.groupby("MM")["TMK"].mean()
seasonal_cycle_last = last_20_years.groupby("MM")["TMK"].mean()

# Plot the seasonal cycles
plt.figure(figsize=(10, 6))
plt.plot(
    seasonal_cycle_first.index,
    seasonal_cycle_first.values,
    marker="o",
    label="First 20 Years",
)
plt.plot(
    seasonal_cycle_last.index,
    seasonal_cycle_last.values,
    marker="o",
    label="Last 20 Years",
)
plt.title("Seasonal Cycle Comparison")
plt.xlabel("Month")
plt.ylabel("Mean Temperature (°C)")
plt.xticks(
    ticks=range(1, 13),
    labels=[
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ],
)
plt.grid()
plt.legend()
plt.show()

# Part c: Compare seasonal cycle changes to standard deviation
std_dev = monthly_mean.std()
print(f"Standard Deviation of Monthly Mean Temperature (July): {std_dev:.2f} °C")

print(
    "Seasonal cycle changes can be observed by comparing the first and last 20 years' seasonal cycles. "
    "The magnitude of these changes relative to the standard deviation provides insight into the variability."
)
