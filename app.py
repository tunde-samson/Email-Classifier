from flask import Flask, render_template, redirect, url_for, request
from form import MyEmailClassifier
import joblib

app = Flask(__name__)
app.secret_key = 'SuperSecret'

model = joblib.load("email_spam_perceptron_model")
vectorizer = joblib.load("vectorizer_perceptron_model")

@app.route("/", methods=['POST', 'GET'])
def index():
    form = MyEmailClassifier()

    prediction = 0

    if form.validate_on_submit():
        email_text = form.email.data
        # Transform and predict
        X = vectorizer.transform([email_text])
        result = model.predict(X)[0]
        prediction = 'Spam' if result == 1 else 'Not Spam'

    return render_template("index.html", form=form, prediction=prediction)




if __name__ == '__main__':
    app.run(debug=True)


