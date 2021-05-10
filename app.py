#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask
import requests
app = Flask(__name__)
@app.route("/say/<name>")
def greeting(name):
    
    x = requests.get('http://greeting-service.test:500/greeting/'+name)
    if x:
        return x.text
    else :
        return "Error"

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port=90)


# In[ ]:




