import pandas as pd

data = {
    "Duration": [60, 60, 60, 45, 45, 60, 60, 450, 30, 60, 60, 60, 60, 60, 60, 60, 60, 60, 45, 60, 45, 60, 45, 60, 45, 60, 60, 60, 60, 60, 60, 60],
    "Date": ['2020/12/01', '2020/12/02', '2020/12/03', '2020/12/04', '2020/12/05', '2020/12/06', '2020/12/07', '2020/12/08', '2020/12/09', '2020/12/10',
             '2020/12/11', '2020/12/12', '2020/12/12', '2020/12/13', '2020/12/14', '2020/12/15', '2020/12/16', '2020/12/17', '2020/12/18', '2020/12/19',
             '2020/12/20', '2020/12/21', None, '2020/12/23', '2020/12/24', '2020/12/25', '20201226', '2020/12/27', '2020/12/28', '2020/12/29', '2020/12/30', '2020/12/31'],
    "Pulse": [110, 117, 103, 109, 117, 102, 110, 104, 109, 98, 103, 100, 100, 106, 104, 98, 98, 100, 90, 103, 97, 108, 100, 130, 105, 102, 100, 92, 103, 100, 102, 92],
    "Maxpulse": [130, 145, 135, 175, 148, 127, 136, 134, 133, 124, 147, 120, 120, 128, 132, 123, 120, 120, 112, 123, 125, 131, 119, 101, 132, 126, 120, 118, 132, 132, 129, 115],
    "Calories": [409.1, 479.0, 340.0, 282.4, 406.0, 300.0, 374.0, 253.3, 195.1, 269.0, 329.3, 250.7, 250.7, 345.3, 379.3, 275.0, 215.2, 300.0, None, 323.0, 243.0, 364.2, 282.0, 300.0, 246.0, 334.5, 250.0, 241.0, None, 280.0, 380.3, 243.0]
}

df = pd.DataFrame(data)

# print(df.loc[[0,2,3],["Pulse","Date"]])


# One way to fix wrong values is to replace them with something else.

# In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7:

df.loc[7,'Duration'] = 45

print(df["Duration"])


# or you can loop around the values and set them according to some rules
# Example
df = pd.DataFrame(data)
for index in df.index:
    if df.loc[index,"Duration"] > 100:
        df.loc[index,"Duration"] = 100
print(df["Duration"])

# Another way of handling wrong data is to remove the rows that contains wrong data.

# This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.
df = pd.DataFrame(data)
for index in df.index:
    if df.loc[index,"Duration"] > 100:
        df.drop(index,inplace=True)
print(df["Duration"])