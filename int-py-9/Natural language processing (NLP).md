# **Natural language processing (NLP)**

## Introduction to NLP

- Natural language processing (NLP) is a branch of artificial intelligence that helps computers understand, interpret and manipulate human language.

- NLP is automated way to understand and analyze natural human language and extract information from such data by applying machine learning algorithm.

We can understand through a diagram.

![Diagram](https://user-images.githubusercontent.com/47269967/93630169-26bf2e80-fa07-11ea-92fc-c1afc9c53ec4.png)

## Some example of NLP

- Google Assistant application , it takes questions from human that can be written and spoken and answer them accordingly

- Email filters: Email filters are one of the most basic and initial applications of NLP online. It started out with spam filters, uncovering certain words or phrases that signal a spam message. But filtering has upgraded, just like early adaptations of NLP.

- Predictive text: Things like autocorrect, autocomplete, and predictive text are so commonplace on our smartphones that we take them for granted. Autocomplete and predictive text are similar to search engines in that they predict things to say based on what you type, finishing the word or suggesting a relevant one. And autocorrect will sometimes even change words so that the overall message makes more sense.

## Why NLP

- NLP is important because it helps resolve ambiguity in language and adds useful numeric structure to the data for many downstream applications, such as speech recognition or text analytics.

## Use of NLP

- Answering Questions:-Question answering (QA) is a computer science discipline within the fields of information retrieval and natural language processing (NLP), which is concerned with building systems that automatically answer questions posed by humans in a natural language.

- Information Extraction:-Information extraction (IE) is the task of automatically extracting structured information from unstructured and/or semi-structured machine-readable documents and other electronically represented sources. In most of the cases this activity concerns processing human language texts by means of natural language processing (NLP). Recent activities in multimedia document processing like automatic annotation and content extraction out of images/audio/video/documents could be seen as information extraction.

![Diagram](https://user-images.githubusercontent.com/47269967/93641819-9559b780-fa1a-11ea-96f8-aaf8b497d25d.png)

- Machine Translation :- Machine Translation (MT) is the task of automatically converting one natural language into another, preserving the meaning of the input text, and producing fluent text in the output language.

- Text Summarization :- It is a technique that shortens a long piece of content with main points outlined that gives an idea of the whole content. It becomes critical when someone needs a quick and accurate summary of very long content. Summarizing text can be expensive and time-consuming if done manually.

- Sentiment Analysis :- Sentiment analysis is the interpretation and classification of emotions (positive, negative and neutral) within text data using text analysis techniques. Sentiment analysis tools allow businesses to identify customer sentiment toward products, brands or services in online feedback.

## Implementation of NLP

![Diagram](https://user-images.githubusercontent.com/47269967/93658365-a0333d00-fa58-11ea-8a93-a7b0518cfb01.png)

![Diagram](https://user-images.githubusercontent.com/47269967/93658369-a45f5a80-fa58-11ea-8fc8-7dfd740017f2.png)

![Diagram](https://user-images.githubusercontent.com/47269967/93658359-8db90380-fa58-11ea-912e-3e72bc933768.png)

## NLP Library

### **1.NLTK**

- NLTK is the leading and one of the best natural language processing libraries for Python.
- It have over 100 corpora and related and related lexical resources ,such as WordNet , web Text Corpus and so on.
- It has a lot of pre-defined models as well, which helps us to analyze things very quickly.
- Open-Source library that is available on windows,Macos and Linux.

Installation

    pip install nltk

Features

- Stemming
- Recommendation
- Sentiment analysis
- Translation

### **2.Gensim**

- Gensim is an open-source vector space and topic modelling toolkit.
- Gensim uses numpy and sciPy.
- Gensim is designed for data stemming ,habdle large text collections and efficient incremental algorithms.

Installation

    pip install gensim

Features

- FastText
- Word2Vec
- Latent Semantic Analysis
- Latent dirichlet Allocation
- tf-idf ( Term frequency-inverse document frequency)

### **3.TextBlob**

- TextBlob is a python library for processing textual data.
- It also offers smooth integration with other programming Language.

Installation

    pip install -U tectblob
    python _m textblob.download_corpora

Features

- Tokenization
- Parsing
- Spelling Corrrection
- Sentiment Analysis
- Part-Of_Speech tagging
- n-grams
- Translation
- Word & Phrase frequencies

### **4.coreNLP**

- coreNLP is a suite of tools for implementing a natural language processing .
- Originally written in Java,coreNLP words with other language such as python ,javascript and many more.

Installation

    pip install stanford-corenlp

Features

- Lemmatization
- Part-Of-Speech Tagging
- Morphological Tagging
- Named ENtity Recognition
- Tokenization
- Sentence Splitting

### **5.spaCy**

- spaCy is open source library for advance NLP.
- spaCy is designed specially for production use and helps us to bulid applications that process and understand large volume of text.
- It can be used to built information extration or natural language understanding systems or to pre-process text for deep learning.

Installation

    pip install -U spacy

Features

- Tokenization
- POS Tagging
- Dependency Parsing
- Lemmatization
- Sentence Boundary Detection
- Named Entity Recognition
- Entity Linking
- Text Classification
- Similarity
