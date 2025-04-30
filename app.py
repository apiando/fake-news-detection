from flask import Flask, render_template, request, url_for
from transformers import BertTokenizer, BertForSequenceClassification
import torch
import pandas as pd
import os

# initialize the Flask application
app = Flask(__name__)

# load the trained model and tokenizer
model = BertForSequenceClassification.from_pretrained("model")
tokenizer = BertTokenizer.from_pretrained("model")

# landing page redirect
@app.route("/")
def index():
    return render_template("home.html")

# path to load home page
@app.route('/home')
def home():
    return render_template('home.html')

# path to load about page
@app.route('/about')
def about():
    return render_template('about.html')

# path to load about page
@app.route('/demo')
def demo():
    true_df = pd.read_csv("training/True.csv").head(3)
    fake_df = pd.read_csv("training/Fake.csv").head(3)
     # Check if wordclouds exist

     # Generate URLs for the wordcloud images
    true_cloud_url = 'static/true_wordcloud.png'
    fake_cloud_url = 'static/fake_wordcloud.png'
    
    # Copy images from results to static (one-time operation)
   
    
    return render_template('demo.html',
                        true_df=true_df,
                        fake_df=fake_df,
                        true_cloud=true_cloud_url,
                        fake_cloud=fake_cloud_url)



# path to load form page 
@app.route("/inspect", methods=["GET", "POST"])
def inspect():
    prediction = None

    if request.method == "POST":
        user_input = request.form["text"]

        # preprocess the input text
        inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True, max_length=512)

        # predict
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            predicted_class_id = logits.argmax().item()

        # map prediction to label
        if predicted_class_id == 1:
            prediction = "This article appears to be REAL."
        else:
            prediction = "This article appears to be FAKE."

    return render_template("inspect.html", prediction=prediction)

# path to load inspection form with model prediction
@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form['text']

    # tokenize the input
    inputs = tokenizer(
        input_text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=512
    )

    # put model into evaluation mode
    model.eval()

    # disable gradient calculation
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class_id = torch.argmax(logits, dim=1).item()

    # map class ID to labe;;
    label_map = {0: "Fake News", 1: "Real News"}
    prediction = label_map.get(predicted_class_id, "Unknown")

    return render_template('inspect.html', prediction=prediction, input_text=input_text)




# run app on local development server
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
