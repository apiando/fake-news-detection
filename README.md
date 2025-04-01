# Fake News Detection – Midterm Report  
**CS506 Final Project**  

---

## Presentation Video  
*Insert YouTube video link here once available*

---

## Project Overview  
Our project focuses on building a machine learning model to detect fake news by analyzing the text of news articles. While our initial dataset contains a wide range of current events, we plan to extend the model to specialize in healthcare misinformation in the later stages. Ultimately, our goal is to create a tool that can help users distinguish reliable reporting from fabricated or misleading content.

---

## Data Sources  

### Training Dataset  
We obtained our main training data from the **Fake News Detection Datasets**, published by Emine Bozkus. It includes two CSV files:
- `False.csv`: articles with fabricated or misleading claims  
- `True.csv`: articles containing fact-checked, credible content  

Each row contains the following fields:
- `title`: the main headline or claim  
- `text`: the full article body  
- `date`: publication date  

### Testing Dataset (Future Stage)  
For testing on health-related misinformation, we plan to use the **CoAID: COVID-19 Healthcare Misinformation Dataset**, published by Limeng Cui and Dongwon Lee in 2020. It includes over 4,200 articles and URLs to fact-checked claims. Once scraping is complete, we will test our model's generalization on this domain-specific dataset.

---

## Preprocessing Steps  

- **Labeling**: We created a new `label` column, assigning `0` to fake articles and `1` to real ones.  
- **Column Selection**: We retained `title`, `text`, and `label`, but used only the `text` field for training.  
- **Merging**: Both datasets were combined into one DataFrame and shuffled to randomize the order.  
- **Train-Test Split**: The dataset was split into 80% training and 20% validation using `train_test_split`.  
- **Tokenization**: We used Hugging Face’s `bert-base-uncased` tokenizer, which automatically performs:
  - Lowercasing  
  - WordPiece tokenization  
  - Padding/truncation to 512 tokens (BERT’s max input length)  

No additional text cleaning was necessary, as the BERT tokenizer handles raw input effectively.

---

## Data Modeling Methods  

To classify each article as real or fake, we fine-tuned a pretrained BERT model from Hugging Face (`bert-base-uncased`) for binary classification.

### Modeling Pipeline
- **Model**: `BertForSequenceClassification` with `num_labels=2`  
- **Training Framework**: Hugging Face’s `Trainer` API  

### Hyperparameters  
- Learning rate: `2e-5`  
- Batch size: `8`  
- Epochs: `3`  
- Weight decay: `0.01`

### Evaluation Metrics  
- Accuracy  
- Precision  
- Recall  
- F1 Score (computed using `sklearn.metrics`)  

This architecture allows the model to learn how language differs between fake and real news while generalizing to new content.

---

## Preliminary Results  

Our BERT-based model has shown promising early results, with strong accuracy and balanced evaluation metrics. Tracking precision, recall, and F1-score helped us evaluate whether the model was biased toward one class and which labels it struggled to classify correctly.

---

## Preliminary Visualizations  

We created visualizations to better understand our dataset and how the model may be learning:

- **Histogram**: Showed a slightly imbalanced distribution with more fake articles than real ones  
- **Word Clouds**:
  - Fake news included dramatic or attention-grabbing words such as "shocking", "breaking", and "alien"  
  - Real news used more formal language such as "reform", "healthcare", and "bill"  
  - Both word clouds included recurring names like "Trump", "Russia", and "Clinton", indicating consistent topical overlap  

These patterns suggest that the model is capturing not just factual content, but stylistic and emotional cues as well.

---

## Next Steps  

- Scrape article content from CoAID’s `news_url` column to build a test set focused on healthcare misinformation  
- Evaluate the model’s performance on unseen claims  
- Develop a simple user-facing input function to allow real-time predictions  
- Conduct further tuning and analysis to improve accuracy and reduce misclassifications  