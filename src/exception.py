import sys
import logging

import sys  # Step 1: Import the sys module

def error_message_detail(error, error_detail):  # Step 2: Correct the function signature
    _, _, exc_tb = error_detail.exc_info()  # Note: Changed exe_info() to exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)  # Step 3: Correct formatting and missing brackets
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super.__init__(error_message)
        self.error_message = error_message_detail(error,error_detail=error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a=10;
    except:
        logginginfo("Divide by zero error")
        raise CustomException