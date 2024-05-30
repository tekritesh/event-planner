import pandas as pd
import sys
import os
sys.path.append('../')
from  event_planner.wa_invite import wa_invite
import logging

def test_max_value():
    test_df = pd.read_csv("test_list.csv")
    inst = wa_invite(df=test_df,msg_txt_file="test.txt", log_level=logging.INFO)
    inst.send_invite()
  