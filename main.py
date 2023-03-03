from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)
model=pickle.load(open('model1.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template("forest.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    print(request.form.values())
    float_features=[float(x) for x in request.form.values()]

    # float_features = [float(x) for x in "5.584087 188.313324 28748.687739 7.544869 326.678363 280.467916 8.399735 54.917862 2.559708".split(' ')]
    # float_features = [float(x) for x in "7.080795 118.988579 14285.583854 7.804174 268.646941 389.375566 12.706049 53.928846 3.595017".split(' ')]  # row8 RO
    # float_features = [float(x) for x in "9.177870 163.274828 20868.331219 7.726040 320.421432 426.994393 10.214275 62.430926 3.108770".split(' ')]  # row99 No need
    float_features = [float(x) for x in "5.058109 238.569380 34873.934523 8.983276 374.433505 669.725086 13.353181 76.521800 5.106656".split(' ')]  # row66 UF

    final=[np.array(float_features)]
    print(float_features)
    print(final)
    prediction=model.predict(final)
    output=prediction

    if output == 'No need':
        return render_template('forest.html',pred='No need to use any Purifier')
    else:
        return render_template('forest.html',pred='Recommended water Purifier is '+str(prediction))


if __name__ == '__main__':
    app.run(debug=True)
