import pandas as pd

# Tạo một DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [6, 7, 8, 9, 10],
                   'C': [11, 12, 13, 14, 15]})

print(df)
# Truy cập hàng thứ 0
row_0 = df.iloc[0]

# Truy cập cột thứ 1
col_1 = df.iloc[:, 1]

# Truy cập một ô cụ thể (hàng 0, cột 1)
cell = df.iloc[0, 1]

# print("Hàng thứ nhất:")
# print(row_0)

# print("\nCột thứ hai:")
# print(col_1)
print()

# print("\nÔ tại hàng 0, cột 1:")
# print(cell)
