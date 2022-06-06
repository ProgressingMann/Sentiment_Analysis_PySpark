# Sentiment Analysis of Amazon Reviews using NLP

## Data - 300,000 Amazon Reviews
## Tools - PySpark, sklearn, TensorFlow

## The motivation of this project is to improve NLP, Machine Learning and Big Data skills.

### How are the tools used - 
  <ul>
    <li>We will use <strong>PySpark</strong> DataFrames for data cleaning, preprocessing and filtering because we have a large text dataset (corpus).<br>
        The motivation for using PySpark comes from the fact that it utilizes all the available CPU cores concurrently to perform operations on DataFrames
        and hence is much much faster than any other technique. <br>
        <strong>Note:</strong> I tried using the futures.concurent functionality for parallel processing but PySpark outperformed it big time.
  </ul>
