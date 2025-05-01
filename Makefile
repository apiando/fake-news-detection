# Makefile for Fake News Inspector

# create virtual environment and install dependencies
setup:
	python -m venv venv
	venv\Scripts\activate && pip install --upgrade pip && pip install -r requirements.txt

# run the Flask app (Windows)
run:
	venv\Scripts\activate && python app.py

# run word cloud generation notebook
wordcloud:
	jupyter notebook word_cloud.ipynb

# run training notebook
train:
	jupyter notebook training.ipynb

# clean the environment
clean:
	rd /s /q venv
