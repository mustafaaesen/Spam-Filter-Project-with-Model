from flask import Flask, request, jsonify, render_template
#flask frameworkü ve json işlemleri için

import pickle


app = Flask(__name__)
#flask uygulaması başlatır

with open("model.pkl","rb") as model_file:
    model =pickle.load(model_file)

#model ve vectorizer dosyalarını yükleme

with open("vectorizer.pkl","rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)



#test iin GET endpoint


@app.route("/")
def home():

    return render_template("index.html")

#post isteğiyle gelen  metni sınıflandırmak için

@app.route("/tahmin",methods=["POST"])

def tahmin():

    if request.method=="POST":
        mesaj = request.form["mesaj"]
        vektor = vectorizer.transform([mesaj])
        tahmin = model.predict(vektor)

        sonuc = "SPAM" if tahmin[0]==1 else "SPAM DEĞİL"
        return render_template("index.html",tahmin_sonucu=sonuc, girilen_mesaj=mesaj)


if __name__ == "__main__":
      app.run(debug=True)

  