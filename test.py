# Import Libraries
import pandas as pd
# Create Test Data
points = {'code': ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr',
                   'stu', 'vwx', 'yz'], 'lat': [1, 3, 6, 9, 12, 15, 18, 21, 23]}
bounds = {'bd_code': ['s1', 's2', 's3', 's4',
                      's5', 's6', 's7', 's8', 's9'], 'out': [2, 4, 6, 8, 10, 12, 14, 16, 19]}
df_points = pd.DataFrame(data=points)
df_bounds = pd.DataFrame(data=bounds)

# Loop through data frames
for r in range(len(df_points)):
    find = 0
    for q in range(len(df_bounds)):
        if df_points['lat'].iloc[r] == df_bounds['out'].iloc[q]:
            find = find + 1
            print(df_points['lat'].iloc[r], df_bounds['bd_code'].iloc[q])
        else:
            continue
    if find == 0:
        print(df_points['lat'].iloc[r], df_points['code'].iloc[r])
    else:
        continue
