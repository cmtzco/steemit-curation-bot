from subprocess import call
from steemvars import *
import threading
import time


def run_bot(puppet, posting_key):
    call(["python3", "steem.py", puppet, posting_key])


for ea_acct in accounts:
    pupp = ea_acct
    pupp_pk = accounts[ea_acct]['posting_key']
    t = threading.Thread(target=run_bot, args=(pupp, pupp_pk))
    t.start()
