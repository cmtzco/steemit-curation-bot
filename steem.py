from piston.steem import Steem
from subprocess import call
import os
import sys
import json

upvote_history = []
my_subscriptions = ["cmtzco", "cryptohustlin", "alchemage", "reported",
                    "Cryptohustlin", "Random-potato", "kennyskitchen",
                    "cryptocameo", "carlidos", "knozaki2015",
                    "e-steem", "princewahaj", "naifaz", "craig-grant", "dantheman",
                    "shortcut", "endaksi1", "sauravrungta", "neoxian", "jasen.g1311",
                    "btctoken", "zeartul", "timelapse", "cnmtz", "gochomoe"]

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
                print("Voting from {} account".format(puppet))
                c.vote(100, puppet)
                print("====> Upvoted")
                upvote_history.append(c.identifier)
            except BroadcastingError as e:
                print("Upvoting failed...")
                print("We have probably reached the upvote rate limit.")
                print(str(e))
            
            
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


