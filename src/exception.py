import sys

def error_message_detail(error , error_details:sys) :
    _,_, exc_tb = error.detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in the python script [{0}] Line Number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno , str(error)
    

    )



class CustomException(Exception):
    def __init__(self, error_message , error_details:sys):
        super().__init__(error_message)
        self.error_messgae = error_message_detail(error_message , error_details= error_details)

    def __str__(self):
        return self.error_messgae