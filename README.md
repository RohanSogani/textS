# textS

A place to get the summary of a research paper.
Intend to use the text summarization domain of Natural Language Processing.

## Backend Activities
1. extractArchive.py<br>
Extracts research papers from the arXiv dataset based on the cs.DC taxonomy 
(Distributed, Parallel, and Cluster Computing). 

2. convertPDF.py <br>
Converts an input pdf to text and then converts the texts into sentences that 
our model requires.

3. arxiv folder <br>
Used to create a fraction of arxiv data set, the dataset sizes are as follows
~1000 articles train-set, ~50 articles for val-set and ~30 articles for test-set<br>
Usage
``bash
$ cd arxiv
$ tfds build
```

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

5. To deactivate virtual enviroment
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