from flask import Flask
import logging
import requests
import time

app = Flask(__name__)

#below 3 lines are used to remove a unwanted info which
#was also getting printed
app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(asctime)s - %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

@app.route("/say/<name>")
def greeting(name):
    
    g  = time.time()
    x = requests.get('http://greeting-int-service.test:500/greeting/'+name)
    t = (time.time() - g)
    logging.info('Greet-Client is Started , Response_Time=%ss',t)
    if x:
        return x.text
    else :
        return "Error"

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port=90)

