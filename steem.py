from piston.steem import Steem
from subprocess import call
from steemvars import *
import os
import sys
import json
import random
import threading
	
upvote_history = []



def vote(puppet, wif_key):
    steem = Steem(wif=wif_key)
    print("{} : Waiting for new posts by {}".format(puppet, my_subscriptions))
    for c in steem.stream_comments():
        if c.author in my_subscriptions:
            print(c.author)
            if c.identifier in upvote_history:
                continue
            print("New post by @{} {}".format(c.author, url_builder(c)))
            try:
                #print("Voting from {} account".format(puppet))
                #c.vote(100, puppet)
                #print("====> Upvoted")
                #upvote_history.append(c.identifier)
                print("Voting from {} account".format(puppet))
                curation_time = random.randint(840,1020)
                print(c.identifier)
                t = threading.Thread(target=curation_delay_vote, args=(wif_key, puppet, c.identifier, curation_time))
                t.start()
                upvote_history.append(c.identifier)
            except Exception as e:
                print("Upvoting failed...")
                print("We have probably reached the upvote rate limit.")
                print(str(e))
            
            

def curation_delay_vote(wif_key, account_to_vote_with, identifier, time_to_wait):
    print(time_to_wait)
    time.sleep(time_to_wait)
    steem = Steem(wif=wif_key)
    steem.vote(identifier, 100, account_to_vote_with)
    print("====> Upvoted")

def url_builder(comment):
    return "https://steemit.com/%s/%s" % (comment.category, comment.identifier)

if __name__ == "__main__":
    while True:
        try:
           puppet = sys.argv[1]
           posting_key = sys.argv[2]
           vote(puppet, posting_key)
        except (KeyboardInterrupt, SystemExit):
            print("Quitting...")
            break
        except Exception as e:
            print(e)
            print("### Exception Occurred: Restarting...")


