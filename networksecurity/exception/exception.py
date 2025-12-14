import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):      # The below are some beasic information that we should definitely know related to exception. and these are the intenal details with respect to the exception that we really have. So. this class will besically raise our custom exception.

    def __init__(self, error_message, error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()


        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename


    def __str__(self) :
        return "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        self.file_name, self.lineno, str(self.error_message))


if __name__ == "__main__":
    try:        # This is for checking that whether the logging is working or not. We'are just testing to check both logging and exception should work.
        logger.logging.info("Enter the try block")

        a = 1/0
        print("This will not be printed", a)

    except Exception as e:
        raise NetworkSecurityException(e,sys)



# if exception.py is not running:- python -m networksecurity.exception.exception
