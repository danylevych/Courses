import math
import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    allPages = list(corpus.keys())
    
    probability = dict()
    
    for nextPage in allPages:
        if nextPage in corpus[page]:
            probability[nextPage] = damping_factor / len(corpus[page])
        else:
            probability[nextPage] = 0
    
    for randomPage in allPages:
        probability[randomPage] += (1 - damping_factor) / len(allPages)
    
    return probability


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    probabilities = dict()
    for page in corpus.keys():
        probabilities[page] = 0
    
    tempProb = dict()
    
    for i in range(n):
        if i == 0: # The first iteration.
            randomPage = random.choice(list(corpus.keys()))
            probabilities[randomPage] = 1 / n
            tempProb = transition_model(corpus, randomPage, damping_factor)
        else:
            page = random.choices(list(tempProb.keys()), list(tempProb.values()), k = 1)
            probabilities[page[0]] += 1 / n
            tempProb = transition_model(corpus, page[0], damping_factor)
    
    return probabilities


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    n = len(corpus.keys())
    allPages = list(corpus.keys())
    probabilities = {page: 1 / n for page in allPages}
    
    prevProbabilities = None
    
    while prevProbabilities is None or not is_accuracy_saved(prevProbabilities, probabilities, 0.001):
        prevProbabilities = probabilities.copy()
        for page in probabilities:
            probabilities[page] = page_rank(corpus, page, damping_factor, probabilities, n)
    
    return probabilities


def is_accuracy_saved(new, prev, accuracy):
    if new is None or prev is None:
        return False
    
    for page in new.keys():
        if abs(new[page] - prev[page]) > accuracy:
            return False
    
    return True

def page_rank(corpus, page, d, probabilities, n):    
    if len(corpus[page]) == 0:
        return (1 - d) / n
    
    daughtersCoef = 0
    
    for parentPage in corpus:
        if page in corpus[parentPage]: # If current page is one of those that parent page is linked on.
            daughtersCoef += probabilities[parentPage] / len(corpus[parentPage])
    
    return (1 - d) / n + d * daughtersCoef

if __name__ == "__main__":
    main()
