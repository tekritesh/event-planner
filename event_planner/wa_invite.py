import pandas as pd
import logging 
import sys
import argparse

import pywhatkit as pwk

# sys.path.append('../')
# import PyWhatKit.pywhatkit as pwk
# import PyWhatKit.whats as pwk


class wa_invite():

    def __init__(self, df=pd.DataFrame(),msg_txt_file = "",log_level=logging.INFO):
        """initialising class with dataframe
            args:
                df(dataframe): contact dataframe
                log_level(logging.level): log level for the class
        """
        self.log = logging.getLogger("event-logger")
        self.log.setLevel(log_level)
        self.df = df

        try:
            if not self.df.empty:
                self.log.info("Reading Contacts from dataframe with columns X Rows:[%s X %s]" % (
                    self.df.shape[0], self.df.shape[1]))
            else:
                self.log.error("Empty Data Frame Provided")

            self.msg_txt = self._read_msg_txt(msg_txt_file)
                
        except:
            self.log.error("Check the Dataframe")

    
    def _read_msg_txt(self,msg_txt_file=""):
        try:
            f = open(msg_txt_file, 'r')
            content = f.read()
            f.close()
            return content
        except:
            self.log.error("Cannot Read Txt File")




    def send_invite(self):
        """initialising class with dataframe
            args:
                
        """

        ### read data in
        df = self.df
        ### if mobile number is empty drop the row
        df.dropna(subset=['Mobile_No'], inplace=True)
        ## convert to dictionary of lists per column
        df_dict = df.to_dict('list')
        ## get the required lists and combine
        names = df_dict['Name']
        phs = df_dict['Mobile_No']
        length_phs = df_dict['LengthofMobileNumber']
        country_codes = df_dict['CountryCode']
        combo = zip(names,phs,length_phs,country_codes)

        # text = """ Hello Friend """
        
        

        for name, ph, length_ph, country_code in combo:
            try:
                # time.sleep(10)
                ph = str(ph).replace("+", "") ## drop + symbol if exists
                ph = ph.replace("-","")
                ph = ph.replace("(","")
                ph = ph.replace(")","")
                ph = ph.replace(".0", "")
                ph = ph.replace(" ", "") ## drop space
                if len(ph)==length_ph:
                    ph = str(country_code) + f'{ph}'

                self.log.info(f'Sending Message to {ph}')
                text = self.msg_txt.replace("<NAME>", name)
                pwk.sendwhatmsg_instantly(f'+{ph}', \
                                    f'{text}', \
                                    wait_time = 10,
                                    tab_close =True)    
                # self.log.debug(f'Sending {text} to {ph}') 
                self.log.debug(f'Sending {text} to {ph}') 
                self.log.info(f'Message Sent to {ph}') 
            except: 
                self.log.error("Error in sending the message due to whatsapp issue")



def cli(args=None):
    """Process command line arguments"""
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_contact_list", type=str, default="tests/test_list.csv")
    parser.add_argument("--input_msg_txt", type=str, default="tests/test.txt")
    args = parser.parse_args()
    
    if not args.input_contact_list and not args.input_msg_txt:
        print("Oops, you will need to provide input directory or input file")
        parser.print_help(sys.stderr)
        sys.exit(1)

    test_df = pd.read_csv(args.input_contact_list)
    inst = wa_invite(df=test_df,msg_txt_file=args.input_msg_txt, log_level=logging.INFO)
    inst.send_invite()

