import os
import sys
from networksecurity.logging.logger import logging

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details:sys):
        self.error_message=error_message
        _, _, exc_tb = error_details.exc_info()
        
        
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename
        
    def __str__(self):
        return f"Error occured in python script name {self.file_name}\n at line number {self.lineno}.\n And error message is {str(self.error_message)}"
    
if __name__=="__main__":
    try:
        logging.info("STarted")
        a=1/0
        print(a)
        logging.info("Completed")
    except Exception as e:
        logging.info("Error occured")
        raise NetworkSecurityException(e, sys)