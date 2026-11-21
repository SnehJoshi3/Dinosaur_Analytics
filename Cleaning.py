import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('dino.csv')

data = data.dropna()
data['decade'] = (data['year'] // 10) * 10
data['decade'] = data['decade'].astype('Int64')
data['era'] = data['when_it_lived'].str.split(',').str[0].str.strip().astype(str)

data['founded_in_country'] =data['found_it']

data = data.drop(columns=['when_it_lived','found_it'])

print(data.head())
print(data.info())

sns.countplot(data=data, x='decade')
plt.title('Count by Decade')
plt.show()

sns.countplot(data=data, x='year')
plt.title('Count by Year')
plt.show()

sns.countplot(data=data, x='type')
plt.title('Type')
plt.show()

data.to_csv('updated_dinos.csv',index=False)