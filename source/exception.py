import sys
from source.logger import logging

def error_message_detail(error,error_detail:sys):
    # execution info
    _,_,exc_tb=error_detail.exc_info()
    # exc_tb: tells from which file, which line error is coming
    
    file_name=exc_tb.tb_frame.f_code.co_filename  # to get file name
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        # since we are inheriting from exception, hence super
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message