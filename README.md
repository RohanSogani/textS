# textS

A place to get the summary of a research paper.
Intend to use the text summarization domain of Natural Language Processing.

## Backend Folders
1. Scripts<br>
Contains scripts used for various cleaning and parsing activities
    1. extractArchive.py <br>
    Extracts research papers from the arXiv dataset based on the cs.DC taxonomy 
(Distributed, Parallel, and Cluster Computing).
    2. convertPDF.py <br>
Converts an input pdf to text and then converts the texts into sentences that 
our model requires.

2. arxiv <br>
Used to create a fraction of arxiv data set, the dataset sizes are as follows
~1000 articles train-set, ~50 articles for val-set and ~30 articles for test-set<br>

3. src <br>
Contains the main source for Django BackEnd and React FrontEnd

## Backend: Dev Guide

1. We plan to use virtual environment to keep track of this project
```bash
$ pip3 install virtualenv
```

2. Create a virtual environment
```bash
$ virtualenv venv
```

3. To activate virtual environment
```bash
$ source venv/bin/activate
```

4. Install libraries from requirement.txt
```bash
$ pip3 install -r requirements.txt
```

5. To run Django Backend
```bash
$ cd src/backend/src
$ python3 manage.py createsuperuser "Run this once"
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```

6. If you wish to deactivate virtual enviroment
```bash
$ deactivate
```
### Frontend: Dev Guide

1. Install npm and then
```bash
$ npm run build
```

2. Change Dir to frontend
```bash
$ npm start
```