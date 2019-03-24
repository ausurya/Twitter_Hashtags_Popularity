#!/usr/bin/env python
# coding: utf-8

# In[13]:


from tweepy import OAuthHandler,Stream
from tweepy.streaming import StreamListener
import socket
import json


# In[14]:


#Insert your own developer keys
consumer_key = 'XXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'
access_token = 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'
access_secret = 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'


# In[15]:


class TweetListener(StreamListener):
    def __init__(self,csocket):
        self.client_socket=csocket
    def on_data(self,data):
        
        try:
            msg = json.loads(data)
            print(msg['text'].encode('utf-8'))
            self.client_socket.send(msg['text'].encode('utf-8'))
            return True
        except BaseException as e:
            print("Error",e)
    
    def on_error(self,status):
        print(status)
        return True
    


# In[17]:


def sendData(c_socket):
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    
    twitter_stream = Stream(auth,TweetListener(c_socket))
    #Filtering the tweets with having word guitar in them
    twitter_stream.filter(track=['guitar'])


# In[19]:


if __name__ == '__main__':
    s = socket.socket()
    host = '127.0.0.1'
    port = 5555
    s.bind((host,port))
    
    print('listening on port 5555')
    
    s.listen(5)
    c,addr = s.accept()
    
    sendData(c)


# In[ ]:




