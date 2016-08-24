from subprocess import call
import threading
import time

accounts = { "cmtzco" : { "posting_key" : "5JKLV1GkFsC7kVruxJNNb1TeH4AXvkyMtQyGJA9FRFVPvUorqyX" } }

def run_bot(puppet, posting_key):
    call(["python3", "steem.py", puppet, posting_key])


for ea_acct in accounts:
    pupp = ea_acct
    pupp_pk = accounts[ea_acct]['posting_key']
    t = threading.Thread(target=run_bot, args=(pupp, pupp_pk))
    t.start()
