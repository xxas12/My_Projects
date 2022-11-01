import streamlit as st
import os
import numpy as np
from PIL import Image as im
import pandas as pd
from itertools import cycle
#ALL THE LIBERARY'S
st.title("Product Matching Using Hybrid Search For Price Comparison")
work_directory=os.chdir('C:/Users/xxas12/Downloads/Compressed/Shopee')
option=["text_embeding","Image_embeding"]
option_select=st.radio("Embeding_Type:",option)

if option_select == "Image_embeding":
        
    df=pd.read_csv('submit_euclidean1.csv')
    item_list=(list(df.title))
    item_s=st.selectbox("searchproduct...",item_list,key="0")
    search_by_txt_btn=st.button("Search Product..",key="0")
    spliting_matches_column=df["image_id_list"].str.split("")
    first_image_=df.at[df["title"].eq(item_s).idxmax(),'image']
    first_title= df.at[df["title"].eq(item_s).idxmax(),'title']
    first_price= df.at[df["title"].eq(item_s).idxmax(),'Price']
    related_title_matches=df.at[df["title"].eq(item_s).idxmax(),'image_id_list']
    spliting_list=list(related_title_matches.split(" "))
    related_img_posting_id=df.loc[df['posting_id'].isin(spliting_list)]["image"]
    price_posting_id=df.loc[df['posting_id'].isin(spliting_list)]["Price"]
    match_title=df.loc[df['posting_id'].isin(spliting_list)]["title"]
    path_image=("CAT_0/CAT_STR/CAT_00/CAT/"+related_img_posting_id)
    first_path_image=("CAT_0/CAT_STR/CAT_00/CAT/"+first_image_)
    images_list = list(path_image)
    first_images_list=first_path_image
    resizedImages=[]
    
    display_match_text=im.open(first_images_list)
    re_display_match_text=display_match_text.resize((325, 425), im.ANTIALIAS)
    for imagess in images_list:
        if imagess==first_images_list:
            continue
        else:
            img = im.open(imagess)
        resizedImg = img.resize((325, 425), im.ANTIALIAS)
        resizedImages.append(resizedImg)

    if search_by_txt_btn:
        f_price=price_posting_id[1:]
        f_title=match_title[1:]
        fir=st.image(re_display_match_text,width=350,caption=str("[ "+first_title+" ]"+" --PRICE:"+first_price))
        cols = cycle(st.columns(2))

        for idx, filteredImage in enumerate(resizedImages): 
            next(cols).image(filteredImage, width=350,caption=list("[ "+f_title+" ]"+" --PRICE:"+f_price)[idx])

if option_select=="text_embeding":
    
    df=pd.read_csv('submit_euclidean1.csv')
    item_list=(list(df.title))
    item_s=st.selectbox("search product...",item_list,key="1")
    search_by_txt_btn=st.button("Search Product..",key="1")
    spliting_matches_column=df["matches"].str.split(" ")
    first_image_=df.at[df["title"].eq(item_s).idxmax(),'image']
    first_title= df.at[df["title"].eq(item_s).idxmax(),'title']
    first_price= df.at[df["title"].eq(item_s).idxmax(),'Price']
    related_title_matches=df.at[df["title"].eq(item_s).idxmax(),'matches']
    spliting_list=list(related_title_matches.split(" "))
    related_img_posting_id=df.loc[df['posting_id'].isin(spliting_list)]["image"]
    price_posting_id=df.loc[df['posting_id'].isin(spliting_list)]["Price"]
    match_title=df.loc[df['posting_id'].isin(spliting_list)]["title"]
    path_image=("CAT_0/CAT_STR/CAT_00/CAT/"+related_img_posting_id)
    first_path_image=("CAT_0/CAT_STR/CAT_00/CAT/"+first_image_)
    images_list = list(path_image)
    first_images_list=first_path_image
    resizedImages=[]
    
    display_match_text=im.open(first_images_list)
    re_display_match_text=display_match_text.resize((325, 425), im.ANTIALIAS)
    for imagess in images_list:
        if imagess==first_images_list:
            continue
        else:
            img = im.open(imagess)
        resizedImg = img.resize((325, 425), im.ANTIALIAS)
        resizedImages.append(resizedImg)
     
    if search_by_txt_btn:
        f_title=match_title[1:]
        f_price=price_posting_id[1:]
        fir=st.image(re_display_match_text,width=350,caption=str("[ "+first_title+" ]"+" --PRICE:"+first_price))
        cols = cycle(st.columns(2))

        for idx, filteredImage in enumerate(resizedImages): 
            next(cols).image(filteredImage, width=350,caption=list("[ "+f_title+" ]"+" --PRICE:"+f_price)[idx])