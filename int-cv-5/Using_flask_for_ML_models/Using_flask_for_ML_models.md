![images/cover.png](images/cover.png)

# Using flask for ML models ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=plastic&logo=flask&logoColor=white) ![heroku](https://img.shields.io/badge/%E2%86%91_Deployed_to-Heroku-7056bf.svg?style=plastic)

- ### This application is a flask-based iris flower prediction machine learning project. It predicts the species of flower by taking some information as input. This application requires four inputs.
    1. length of sepal (cm)
    2. width of sepal (cm)
    3. length of petal (cm)
    4. width of petal (cm)

- ### Structure —
    1. **[templates](https://github.com/suvrashaw/Intern-Work/blob/main/int-cv-5/Using_flask_for_ML_models/src/templates)**: The HTML files are kept in this folder. 
    2. **[static](https://github.com/suvrashaw/Intern-Work/blob/main/int-cv-5/Using_flask_for_ML_models/src/static)**: Static files, such as images, are stored in this folder.
    3. [Dataset.csv](https://github.com/suvrashaw/Intern-Work/blob/main/int-cv-5/Using_flask_for_ML_models/src/Dataset.csv): This is the sample dataset, converted to csv. Download the Dataset from [Here](https://www.kaggle.com/uciml/iris/download).
    4. **[app.py](https://github.com/suvrashaw/Intern-Work/blob/main/int-cv-5/Using_flask_for_ML_models/src/app.py)**: This is a python file that contains the code for our application. The Flask Server is started here.
    5. **[iri.pkl](https://github.com/suvrashaw/Intern-Work/blob/main/int-cv-5/Using_flask_for_ML_models/src/iri.pkl)**: This is the pickel file, which has been saved as a model.
    6. **[iris.py](https://github.com/suvrashaw/Intern-Work/blob/main/int-cv-5/Using_flask_for_ML_models/src/iris.py)**: The model is created in this python file.

> Other files like Procfile, requirements.txt, basics.py, etc are for the Heroku deployment.

- ### Requirements —
    - **pandas**==1.0.3
    - **Flask**==1.1.1
    - **numpy**==1.18.1
    - **scikit_learn**==0.22.1
    - **gunicorn**==20.0.4
> The model is saved using the Pickle library after it has been built. Then, Flask is used for the web server. The ML prediction model is given as follows —

    python
    import pandas as pd
    import numpy as np
    import pickle

    df = pd.read_csv('Dataset.csv')
    df = df.drop(columns = ['Id'])

    X = np.array(df.iloc[:, 0:4])
    y = np.array(df.iloc[:, 4:])

    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    y = le.fit_transform(y.reshape(-1))

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    from sklearn.linear_model import LogisticRegression
    sv = LogisticRegression().fit(X_train,y_train)

    # print metric to get performance
    print("Accuracy: ",sv.score(X_test, y_test) * 100)

    pickle.dump(sv, open('iri.pkl', 'wb'))

- ### What does deploying A Machine Learning model entail?

> Model deployment is the process of integrating a machine learning model into an existing production environment where it can take in an input and return an output. The goal of model deployment is to make predictions from a trained ML model available to others, whether they are users, management, or other systems.

- ### Points to consider before deploying the model —
    - **Portability**: This refers to your software's ability to be moved from one machine or system to another. A portable model is one that has a short response time and can be rewritten with little effort.
    - **Scalability**: This refers to the maximum size that your model can scale to. A scalable model does not need to be redesigned in order to maintain its performance.
- ### Factors to consider when choosing a deployment method —
    - How often will predictions be made, and how urgently will the results be required.
    - If predictions should be made one at a time or in batches.
    - The model's latency requirements, one's computing power capabilities, and the desired SLA are all factors to consider.
    - The model's operational implications and costs to deploy and maintain
- ### What is Flask?

> Flask is a Python-based web application framework. Flask provides us with a number of options for developing web applications, as well as the tools and libraries we'll need to get started.

- ### Why Flask?
    - A micro framework with a lot of features
    - A quick template
    - WSGI features that are strong
    - A lot of documentation
> Now that you've built a variety of predictive models, it's time to learn how to use them in real-time to make predictions. When you deploy your model in production, you can always check its ability to generalize.

        python
        from flask import Flask, render_template, request
        import pickle
        import numpy as np

        model = pickle.load(open('iri.pkl', 'rb'))
        app = Flask(__name__)

        @app.route('/')
        def man():
            return render_template('home.html')

        @app.route('/predict', methods=['POST'])
        def home():
            data1 = request.form['a']
            data2 = request.form['b']
            data3 = request.form['c']
            data4 = request.form['d']
            arr = np.array([[data1, data2, data3, data4]])
            pred = model.predict(arr)
            return render_template('after.html', data=pred)

        if __name__ == "__main__":
            app.run(debug=True)

- ### What is Heroku?

> Heroku is a cloud-based platform as a service (PaaS) that allows developers to create, run, and maintain applications entirely in the cloud. Heroku is also known as a polyglot platform because it has features that allow developers to build, run, and scale applications in most languages in a similar way. It enables software developers to create and run complex web applications without worrying about the underlying hardware or networking.

- ### Why Heroku?
    - An easy-to-use tool
    - There is no requirement for infrastructure.
    - A fantastic Command Line Interface
    - Extensive Add-On Toolkit
    - Deploy from a variety of sources
- ### Output
    ![1](images/1.jpeg)
    ![2](images/2.jpeg)
    ![3](images/3.jpeg)
