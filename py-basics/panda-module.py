import pandas  as pd
# df = pd.read_csv('./data-sets/gender_submission.csv')

# mydataset = {
#     "CARS" : ["BMW", "volvo", "FORD", ],
#     "YEARS" : [1992, 1996, 2001],
#     "variant" : ["black", "red", "green"]
#     }

# myvar = pd.DataFrame(mydataset)
# myvar.to_csv('data1.csv')
# # print(pd.__version__)

df = pd.read_csv('./data-sets/california_housing_test.csv')
# print(df.loc[0:3])

# cf = df[['total_rooms', 'total_bedrooms', 'population']]
# print(cf)

# print(df.describe())
# print(df.columns)
# print(df.isnull().any())

#series
a = [1, 7, 2]
# myvar = pd.Series(a)
# print(myvar[0])
# myvar = pd.Series(a, index=['x','y', 'z'])

# print(myvar['y'])

fine = {'day1' : [420, 200, 220, 120], 'day2' : [121, 220,330, 440], 'day3' : [200, 220, 130, 150]}
df = pd.Series(fine)
print(df)