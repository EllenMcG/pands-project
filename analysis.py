# Importing the necessary python modules
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px
import statsmodels

# Importing the data and adding column names using a list
iris_data = pd.read_csv('iris.data')
column_names = ["sepal_length","sepal_width","petal_length","petal_width","species"]
iris_data = pd.read_csv('iris.data',header=None,names=column_names)

# slicing the species string so that the genus Iris is not kept and the species is kept
iris_data["species"]= iris_data["species"].str.split("-").str[1]

# Updating the values for loc[34] and loc[37]
# refer to 'analysis.ipynb for rationale 
iris_data.at[34,'petal_width']= 0.2
iris_data.at[37,'sepal_width']= 3.6
iris_data.at[37,'petal_length']= 1.4

# Summary statistics to summary.txt file and keeping to two decimal places using a lambda function 
summary = iris_data.describe().applymap(lambda x: f"{x:0.2f}")
summary.to_csv('summary.txt', header=True, index=True, sep=' ', mode='w')

# Histograms of each variable 
# sepal length 
plt.hist(iris_data['sepal_length'],bins=10)
plt.title("Histogram of Sepal Length", size=15)
plt.xlabel("Sepal Length (cm)", size=15)
plt.ylabel("Density", size=15)
plt.savefig('histogram_sepallength.png')
# Adding a plt.show() after the plt.savefig() command so that all of the histograms are not sequentially added so that the 
# last histogram contains all four combined histograms
plt.show()

# sepal width 
plt.hist(iris_data['sepal_width'],bins=10)
plt.title("Histogram of Sepal Width", size=15)
plt.xlabel("Sepal Width (cm)", size=15)
plt.ylabel("Density", size=15)
plt.savefig('histogram_sepalwidth.png')
# Adding a plt.show() after the plt.savefig() command so that all of the histograms are not sequentially added so that the 
# last histogram contains all four combined histograms
plt.show()

# petal length
plt.hist(iris_data['petal_length'],bins=10)
plt.title("Histogram of Petal Length", size=15)
plt.xlabel("Petal Length (cm)", size=15)
plt.ylabel("Density", size=15)
plt.savefig('histogram_petallength.png')
# Adding a plt.show() after the plt.savefig() command so that all of the histograms are not sequentially added so that the 
# last histogram contains all four combined histograms
plt.show()

# petal width
plt.hist(iris_data['petal_width'],bins=10)
plt.title("Histogram of Petal Width", size=15)
plt.xlabel("Petal Width (cm)", size=15)
plt.ylabel("Density", size=15)
plt.savefig('histogram_petalwidth.png')
# Adding a plt.show() after the plt.savefig() command so that all of the histograms are not sequentially added so that the 
# last histogram contains all four combined histograms
plt.show()

# Scatterplot using the Seaborn module function .pairplot() 
sns.pairplot(iris_data, hue='species',kind='scatter'); 

# Additional analysis (three items)
# 1 Correlation values using the .corr() funtion mapped to a Seaborn heatmap. First a list of numerical 
# values is created first 
iris_num_data = iris_data[['sepal_length','sepal_width','petal_length','petal_width']]
plt.figure(figsize = [6, 6])
sns.heatmap(iris_num_data.corr(), annot = True, fmt = '.2f', cmap = 'vlag_r', center = 0)
# Added plt.show() for analysis.py fil. Not needed for Jupyter Notebook as figures rendered within the notebook
plt.show()

# 2 Adding a aggregated calculation for sepal length grouped by species. The statistics are easier to see side-by-side
# that with the grouped function in the Summary section 
iris_grouped = iris_data.groupby("species").agg({"sepal_length":[np.mean, np.std, np.median]})
# adding a print statement to and naming aggregated calculation iris_grouped as otherwise it will not showup in this 
# python script. It will show up within the Jupyter Notebook and the print statement is not necessary
print(iris_grouped)

# 3 Viewing the grouped median values is made easy by using a boxplot created using the python module Seaborn 
sns.boxplot(x="species", y="sepal_length", data=iris_data)
# Adding plt.show() for analysis.py fil. Not needed for Jupyter Notebook as figures rendered within the notebook
plt.show()

# 4 Returning back to the correlation maxtix, sepal width had an r value of -0.12 with sepal length. This was a combined 
# correlation matix in that all three species were combined so there looks to be a very weak negative correlation between 
# these two variables. The plotly.express functationality can be imported to generate an interactive scatter plot with 
# one line for each of the three species. This could be done by filtering out by species with the pandas module, 
# but px.scatter can do this by setting the color argument to 'species'

fig = px.scatter(iris_data,x='sepal_length',y='sepal_width',trendline='ols',hover_data=iris_data,color='species')
# plot will open in browser
fig.show()

results = px.get_trendline_results(fig)

# Iris setosa trendline as setosa is in iloc[0]
print(results.px_fit_results.iloc[0].summary())

# Generating the correlation coefficient from the Rsquared of the Iris setosa model by generating the square root of the 
# Rsquared value 
setosa_rsquared = np.sqrt(results.px_fit_results.iloc[0].rsquared)
print(setosa_rsquared)

# Irisvirginia trendline as virginica is in iloc[1]
print(results.px_fit_results.iloc[1].summary())

# Generating the correlation coefficient from the Rsquared of the Iris virginica model by generating the square root of the 
# Rsquared value 
virginica_rsquared = np.sqrt(results.px_fit_results.iloc[1].rsquared)
print(virginica_rsquared)

# Iris versicolor trendline as versicolor is in iloc[2]
print(results.px_fit_results.iloc[2].summary())

# Generating the correlation coefficient from the Rsquared of the Iris versicolor model by generating the square root of the 
# Rsquared value 
versicolor_rsquared = np.sqrt(results.px_fit_results.iloc[2].rsquared)
print(versicolor_rsquared)

# Setting the argument 'trendline_scope' to 'overall' from 'trace' in px.scatter so that all data is combined into 
# one simple linear regression model 
fig_overall = px.scatter(iris_data,x='sepal_length',y='sepal_width',trendline='ols',
                         hover_data=iris_data,color='species',trendline_scope='overall')
# plot will open in browser
fig_overall.show()

results_overall = px.get_trendline_results(fig_overall)
print(results_overall.px_fit_results.iloc[0].summary())

iris_overall_rsquared = np.sqrt(results_overall.px_fit_results.iloc[0].rsquared)
print(iris_overall_rsquared)