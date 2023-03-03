import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import warnings
import pickle
warnings.filterwarnings("ignore")

data = pd.read_csv("final_dataset.csv")
X = data.iloc[:,1:10]
Y = data.iloc[:,11]

X = np.array(X)
Y = np.array(Y)

X = X.astype('float')
Y = Y.astype('str')

x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.2, random_state=1 )
model_dt = DecisionTreeClassifier(criterion = 'entropy', max_depth = 12, max_features = 'auto', min_samples_split = 7, random_state = 0)
model_dt.fit(x_train, y_train)


# sample test cases
# s1= [float(x) for x in "5.584087 188.313324 28748.687739 7.544869 326.678363 280.467916 8.399735 54.917862 2.559708".split(' ')]  # row5 UV
# s2= [float(x) for x in "7.080795 118.988579 14285.583854 7.804174 268.646941 389.375566 12.706049 53.928846 3.595017".split(' ')]  # row8 RO
# s3= [float(x) for x in "9.177870 163.274828 20868.331219 7.726040 320.421432 426.994393 10.214275 62.430926 3.108770".split(' ')]  # row99 No need
# s4= [float(x) for x in "5.058109 238.569380 34873.934523 8.983276 374.433505 669.725086 13.353181 76.521800 5.106656".split(' ')]  # row66 UF
# for i in list([s1,s2,s3,s4]) :
#     final=[np.array(i)]
#     print(model_dt.predict(final))


pickle.dump(model_dt,open('model1.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))