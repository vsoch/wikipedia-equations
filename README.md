# Equation Mapping

This is a dataset that uses word2vec to extract embeddings to describe equations
from statistics and math articles from wikipedia. We will do this for groups of links
that generally fall into these categories:

 - [statistics](statistics)
 - [mathematics](math)

For the first, we use a list of statistics articles. For the second, we do a 
best effort to parse pages of math topics. You are free to use the vectors
for your analysis and efforts! Here are some interesting questions:

 1. Can you build a model to predict an equation from one or more terms?
 2. Can you predict terms from equations?

Please reference the README.md in each folder for further details.

## 1. Install Requirements

If you intend to try to recreate the data, for both, you need to first 
install requirements, including a few libraries I created as a graduate
student, [wordfish](https://vsoch.github.io/2016/2016-wordfish/) and 
[repofish](https://pypi.org/project/repofish/)
wordfish is a small library that uses gensim to run word2vec, and repofish uses it
to parse various internet resources for words, etc.

```bash
pip install -r requirements.txt
```

Then continue with instructions in the subfolder of choice. The steps are generally the same,
but the second (math) was developed after statistics.
