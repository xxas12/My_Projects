# Product_matching_using_hybrid_search_for_price_comparison

### Table of Contents
You're sections headers will be used to reference location of destination.

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)
- [License](#license)
- [Author Info](#author-info)

---

## Description

Finding the right product online at the cheapest price is always a challenge. While having a choice of multiple platforms to buy the same product is good, it takes a considerable amount for a user to search different e-commerce platforms and find the product at the right price.In the past decade it has become impossible to propose a search project without text retriever and because of its success there has been an increasing interest in image retrieval. To have the best solution, we combine two.
Hybrid search is a searching technique that allow users to search for same product using a description, a picture, or the title of the object you're looking for. The flexibility of keyword-based retrieval search is combined with the capacity to query and reason on metadata that is characteristic of semantic search systems in Hybrid Search.These functions take input as a text or an image of the product and return the matched products to the user.For simplicity, the dataset is used from Kaggle [1]. This dataset imitates the web scraping in real life where this data will be scraped from multiple e-commerce platforms. The front- end part of the project is developed in streamlit. Streamlit is an open-source framework for building machine learning and data science apps.

#### Technologies

- Streamlit
- Google collab
- Kaggle_note_book
-Jupyter_Lab

[Back To The Top](#read-me-template)

---

## How To Use

- Open kaggle_note book upload the data set [1]
- copy the  code from "text processing.ipynb",before running the code make sure to enter path of your working directory and directory of the images, then run the code
- Download the "submission.csv" on your desktop
- Download the train images
- upload the "submission.csv" and train images file to your google drive
- copy the  code from "kaggle_image.ipynb" for image processing,before running the code make sure to enter path of your working directory and directory of the images, then run the code
- Download "submit_eculidean.csv" from image processing
- open submit_eculidean.csv add new column "price" since the orignal file does not comke with price column we'll have to manually add our self or you can download mine 
- open jupyter lab ,copy the code from st.py just make sure to change working according to the path train images folder and submit_eculidean.csv
- To run streamlit on  the jupyter lab go to administrator > run this " streamlit run python_script_file.py", just make sure that train images and submit_eculidean.csv   


#### Installation

1. pip install ( annoy,pandas,numpy,os,PIL,vectorhub-nightly) [Image_Processing]
2. pip install ( pandas,os,numpy,TfidfVectorizer,tqdm,gc,torch,PIL,IPython.display) [Text_Processing]
3. pip install (Streamlit,itertools,numpy,pandas,os) [front end]
[Back To The Top](#read-me-template)

---

## References
[1] https://www.kaggle.com/c/shopee-product-matching/data

---

## License

Sarhad University of Science & Information Technology License

Copyright (c) [2022] [Abdullah Aziz]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#read-me-template)

---

## Author Info

- Linkedin - [@Abdullah Aziz](https://www.linkedin.com/in/abdullah-aziz-a22755205/)

[Back To The Top](#read-me-template)
