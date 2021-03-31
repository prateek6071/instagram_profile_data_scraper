from bs4 import BeautifulSoup
from instagramy import  InstagramUser
import pandas as pd
import requests

session_id="17889d0ff99-2360a0"

user =InstagramUser('prateekpamecha1511',sessionid=session_id)
userdata=[]
userdata.append(
    {
     'followers': user.number_of_followers,
     'follows': user.number_of_followings,
     'full_name': user.fullname,
     'profile_pic_url': user.profile_picture_url,
     'username': user.username}
)
#joblist=[]

#c=extract(0..)


df=pd.DataFrame(userdata)
print(df.head())
df.to_csv('userdata.csv')