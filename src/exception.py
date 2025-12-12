# Exception handling module
import logging
import sys
# from src.logger import logging

def error_message_detail(error, error_detail: sys):
    """Generate detailed error message."""
    _, _, exc_tb = error_detail.exc_info()
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        error_message = f"Error occurred in script: {file_name} at line number: {line_number} with message: {str(error)}"
    else:
        error_message = f"Error occurred: {str(error)} (traceback not available)"
    return error_message

class CustomException(Exception):
    """Custom Exception class to handle exceptions with detailed messages."""
    def __init__(self, error, error_detail: sys):
        super().__init__(error)
        self.error = error
        self.error_detail = error_detail

    def __str__(self):
        return error_message_detail(self.error, self.error_detail)
    
# if __name__ == "__main__":
    
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Raising Custom Exception now. Its Divide by zero error    ")
#         raise CustomException(e, sys)