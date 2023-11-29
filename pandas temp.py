import pandas as pd

# Open database
df = pd.read_excel("nics-firearm-background-checks.xlsx")

# save (document, table name)
# df.to_excel("nics-firearm-background-checks.xlsx")
# alaskaTable.to_csv("alaska-firearm-background-checks.csv") # for bigger tables

''' Save to new sheets
writer = pd.ExcelWriter("nics-firearm-background-checks1.xlsx", engine = 'openpyxl')
df.to_excel(writer, sheet_name = "nics-firearm-background-checks")
writer.close() # saves sheets and excel document
'''

# table info
#print(df.info())

# table headers
'''
headers = df.columns.values
print(df.columns.values)
'''

# Veiw
'''
print(df)
print(df.head()) # print top 5
print(df.to_string()) # print entire database
'''

# filter
#             rows            columns
#     iloc[start : finish, start : finish]
#print(df.iloc[:20, :5]) # prints first 20 rows and 5 columns



# remove empty rows
'''
df.dropna()
'''

# fill empty cells
'''
      inplace = True # if you want to alter original table
df.fillna(0, inplace = True)
df[state].fillna(0, inplace = True) # for specific rows
'''

# Format datetime
'''
df['month'] = pd.to_datetime(df['Date'])
print(pd.to_datetime(df['month']))
'''





# Example
df = pd.read_excel("nics-firearm-background-checks.xlsx")
headers = df.columns.values

df.fillna(0, inplace=True)

alaskaRows = []

for x in df.index:
    if df.iloc[x, 1] == "Alaska":
        alaskaRows.append(list(df.iloc[x, :]))

alaskaTable = pd.DataFrame(alaskaRows, columns=headers)
print(alaskaTable.to_string())
