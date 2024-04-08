# Pands Project (of the _Iris_ dataset)

This Github repo contains the project repo completed as part of the Programming and Scripting module done as part of the Higher Diploma in Computing (Data Analysis) at ATU Galway. This project uses python to explore the [Iris dataset](https://archive.ics.uci.edu/dataset/53/iris) through visualisation. 

## Project Background 
The Iris dataset is a small dataset that is commonly used by beginners within machine learning to learn about classification algorithms. This dataset is one of the widley used in machine learning and was published by R.A. Fisher (statistican) in 1936 with Edgar Anderson collecting the raw data ([Unwin and Kleinman, 2021](https://rss.onlinelibrary.wiley.com/doi/abs/10.1111/1740-9713.01589)). The data was origionally published in 1936 by R. A. Fisher for the purposes of applying to a newly created technique by Fisher called linear discriminant function (also known as linear discriminant analysis ([Unwin and Kleinman, 2021](https://rss.onlinelibrary.wiley.com/doi/abs/10.1111/1740-9713.01589); [Fisher, 1936](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x)).

There are 150 observations comprising of four numerical variables and one class label. The numerical variables (all in cm) are petal length, petal width, sepal length, and sepal width while the class column consists of three flowers of the _Iris_ genus with 50 observations each; _Iris setosa_, _Iris versicolor_, and _Iris virginica_. As each class of Iris flower has 50 observations each, this is a balanced dataset and makes it quite suitable for learning about machine learning techniques such as the decision tree, K-means clustering or SVM (support vector machines) classification algorithm ([Ye et al., 2023](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10456161)).

The dataset housed within UCI contains three well known errors. This error arises within python as the python module Skikit-Learn contains these errors from UCI. However, the R module MASS does not contain these errors. The data from [Fisher, 1936](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x) is presented below with the correct data and a code snippit showing the current data within these locations (refer to analysis.ipynb). Also refer to the Scikit-Learn issue [#10550](https://github.com/scikit-learn/scikit-learn/issues/10550) for further discussion. 

## Contents of the repository
Several files within this repository are from the [UCI Iris dataset website](https://archive.ics.uci.edu/dataset/53/iris) and include;
- _iris.data_ - data file used in this project
-  _index_
-   _iris.names_ - Information about the _Iris_ dataset
-   _bezdekiris.data_ - data file with the errors mentioned above updated to aling with the origional dataset published by [Fisher, 1936](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x).

Several files within this repositroy were generated from _anaysis.py_ and _analysis.ipynb_ and include;
- _histogram_petallength.png_ - .png file of histogram of petal length
- _histogram_petalwidth.png_ - .png file of histogram of petal width
- _histogram_sepallength.png_ - .png file of histogram of sepal length
- _histogram_sepalwidth.png_ - .png file of histogram of sepal width
- _summary.txt_ - a text file containing numerical descriptions of the four numerical variables (features) contained within the _Iris_ dataset

The main scripting file is _analysis.py_ and has some light commenting. Further explaination is found within the Jupyter Notebook _analysis.ipynb_*. The analysis remains the same within the two, aside from minor stylistic differences that does not affect the code. For example, the _analysis.py_ file contains _plt.show()_ command, but this is not necessary to include within the Jupyter Notebook as plots are rendered within the Jupyter Notebook. 

- _.gitignore_ file - a file containing a list of files that git should ignore

Two additional _.html_ files were generated as part of the additional analysis so that easy interactive viewing of plots could be presented. These include;
- _separate_slr.html_ - Separated simple linear regression of the three _Iris_ flowers
- _overall_slr.html_ - Combined simple linear regression of the three _Iris_ flowers

## How to run the code
The _analysis.py_ file contains the code for the project. Further discussion and commenting was completed through the Jupyter Notebook, _analysis.ipynb_. This _analysis.ipynb_ Jupyter Notebook can be run though a [Google CoLab](https://colab.google/) envionment from the below link. The badge was created using [Open in Colab](https://openincolab.com/). 

<a target="_blank" href="https://colab.research.google.com/github/EllenMcG/pands-project/blob/main/analysis.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

* The _analysis.ipynb_ Jupyter Notebook was also converted to _.html_ format as _analysis.html_ by running the below code in the directory.

  ```
jupyter nbconvert --to html analysis.ipynb
```
