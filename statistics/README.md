# Equation Mapping: Statistics

Here we will derive vectors based on equations from [statistics topics](https://en.wikipedia.org/wiki/List_of_statistics_articles). You should have already installed the required python
modules in [requirements.txt](../requirements.txt). 

I first started with these steps in separate files, but I find it easier to provide one cohesive 
analysis file, now represented at [statisticsAnalysis.py](statisticsAnalysis.py). The goal of this 
step is to build a word2vec model that has character vectors derived from a huge corpus
of equations.

## Overall Strategy

The general goal is to:

 1. Create word embeddings using (some set) of equations from wikipedia
 2. Create embeddings based on the article summaries 
 3. Link the two


## 1. Create List of Statistics Articles

We first need a crapton of wikipedia pages to parse equations from. This means
getting a list of links from the [statistics topics](https://en.wikipedia.org/wiki/List_of_statistics_articles) 
page, and then (manually) disambiguating the terms when appropriate. These manual
steps are now preserved in the code to be reproducible.

At the end of this step, we have a list of final articles (wikipedia pages) we will
use for the model in [wikipedia_statistics_articles.txt](wikipedia_statistics_articles.txt).

## 2. Obtain Articles and Metadata

From our list of articles above, we now want to populate a lookup dictionary
with metadata about each article. This step pulls the entire page from Wikipedia,
and saves fields such as links, images, url, etc. This is the starting data
structure we need to keep in the case of needing to go back and redo any
portions of the analysis.

At the end of this procedure we will have a [wikipedia_statistics_articles.json](wikipedia_statistics_articles.json) 
and matching [wikipedia_statistics_articles.pkl](wikipedia_statistics_articles.pkl) to each
store the same data structure. 

## 3. Equation Extraction

From our articles, the equations are represented as an attribute of an image.
Wikipedia does this because browsers that don't support MathJax (or similar)
can fall back to showing the image itself. We can take advantage of this
and find the images having a particular class, and then extracting the raw
latex from it. We thus:

 1. use BeautifulSoup to parse the raw html of each article (subpage)
 2. find equations in images based on their class
 3. save the equations, and image, to an equations data structure organized by the topic page

Here is an example of an entry in the list of equations

```python
  {'png': 'https://wikimedia.org/api/rest_v1/media/math/render/svg/b7c3ba47cc5436c389f86a3f617a191d0dbe4877',
   'tex': '2^{n\\mathrm {H} (k/n)}'},
```

At the end of this step, we have a data structure with indices as article name,
and indexing into a list of equations that were extracted. We save both as
[wikipedia_statistics_equations.json](wikipedia_statistics_equations.json) and
[wikipedia_statistics_equations.pkl](wikipedia_statistics_equations.pkl).
