import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

train_years = list(range(2018, 2026))  
predict_years = list(range(2026, 2031))

X_train = np.array(train_years).reshape(-1, 1)

predicted_data = []

for i, row in df.iterrows():
    company = row["Company"]
 
    y_train = np.array([row[f"Emp({year})"] for year in train_years])
     
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    X_future = np.array(predict_years).reshape(-1, 1)
    y_pred = model.predict(X_future)
   
    prediction_dict = {"Company": company}
    for year, pred in zip(predict_years, y_pred):
        prediction_dict[f"Emp({year})"] = int(pred)
    predicted_data.append(prediction_dict)
   
    plt.plot(train_years + predict_years, list(y_train) + list(y_pred), marker='o', label=company)

plt.title("Employee Prediction (2018–2030)")
plt.xlabel("Year")
plt.ylabel("Employees")
plt.legend()
plt.grid(True)
plt.show()

pred_df = pd.DataFrame(predicted_data)

pred_df.to_csv("predicted_2026_to_2030.csv", index=False)

print(pred_df)

full_data = df.copy()

for pred_row in predicted_data:
    company_name = pred_row["Company"]
    for year in predict_years:
        full_data.loc[full_data["Company"] == company_name, f"Emp({year})"] = pred_row[f"Emp({year})"]

all_years = list(range(2018, 2031))
change_data = []

for idx, row in full_data.iterrows():
    company = row["Company"]
    changes = {"Company": company}
    
    for i in range(1, len(all_years)):
        year_prev = all_years[i-1]
        year_curr = all_years[i]
        prev_val = row.get(f"Emp({year_prev})", None)
        curr_val = row.get(f"Emp({year_curr})", None)

        if prev_val and curr_val and prev_val != 0:
            change = ((curr_val - prev_val) / prev_val) * 100
            changes[f"Emp({year_curr})_change"] = f"{change:.2f}%"
        else:
            changes[f"Emp({year_curr})_change"] = "N/A"

    change_data.append(changes)

change_df = pd.DataFrame(change_data)
change_df.to_csv("employee_growth_percent.csv", index=False)
print("\nYear-on-Year Employee % Change:")
print(change_df)

