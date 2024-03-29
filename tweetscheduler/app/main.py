import gspread
from flask import Flask,render_template,request,redirect
from datetime import datetime, timedelta
from os import environ
from dotenv import load_dotenv
load_dotenv()

from werkzeug.utils import redirect
app = Flask(__name__)


gc = gspread.service_account(filename='../credentials.json')

gs_key = environ['GS_KEY']
sh = gc.open_by_key(gs_key)
worksheet = sh.sheet1

class Tweet:
    def __init__(self,message,time,done,row_idx):
        self.message = message
        self.time = time
        self.done = done
        self.row_idx = row_idx


def get_date_time(date_time_str):
    date_time_obj = None
    error_code = None
    try:
        date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        error_code = f'Error! {e}'
    
    if date_time_obj is not None:
        now_time_ind = datetime.utcnow() + timedelta(hours=5,minutes=30)
        if not date_time_obj > now_time_ind:
            error_code = "error! time must be in the future"
    return date_time_obj,error_code




@app.route('/')
def tweet_list():
    tweet_record = worksheet.get_all_records()
    tweets = []
    for idx,tweet in enumerate(tweet_record,start=2):
        tweet = Tweet(**tweet,row_idx=idx)
        tweets.append(tweet)
    
    tweets.reverse()

    n_open_tweets = sum(1 for tweet in tweets if not tweet.done)

    return render_template('base.html',tweets=tweets,n_open_tweets = n_open_tweets) 

@app.route('/tweet',methods=['POST'])
def add_tweet():
    message = request.form['message']
    if not message:
        return "error! no message"
    time = request.form['time']
    if not time:
        return "error! bo time"
    pw = request.form['pwd']
    if not pw or pw!="123456":
        return "error! wrong password"

    if len(message) > 280:
        return "error! message too long!"

    date_time_obj , error_code = get_date_time(time)
    if error_code is not None:
        return error_code
    
    tweet = [str(date_time_obj) , message , 0]
    worksheet.append_row(tweet)
    return redirect('/')

@app.route('/delete/<int:row_idx>')
def delete_tweet(row_idx):
    worksheet.delete_rows(row_idx)
    return redirect('/')

    


if __name__=="__main__":
    app.run(debug=True)


