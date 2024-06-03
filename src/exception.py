import sys
from logger import logging

def custom_error(error_message, error_details:sys) -> str:
    """
    This function take original error details from sys and return a edited custome error message.
    """
    _, _, exc_tb = error_details.exc_info()
    line_number = exc_tb.tb_lineno
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"{error_message} in file {file_name} at line {line_number}"
    return error_message



class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super.__init__(error_message)
        self.error_message = custom_error(error_message, error_details)
    
    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e,sys)







# 1
#### amra bangla ak niom a kaj ta korte partam j tumi jokhon error khaba tokhon amar kache asba and then i print that what i got return from custom_error. and the custom error function return us that way, at first take error details from sys. then make it edite, then return it more solide way.

# 2
#### but in production we need a standard way what is esay and take able for every programmer cineore or junior  don't mater so, that's why when we calling exeption that time exeption place we are calling direct our function but direct function never work parfectly as a exeption some time make problem and lack. that why we are connecting exeption in child function. there for python understaned that -> that also a exeption. that why we calling exeption in our function other wise all work done by sys.

# 3
#### And the error_message name var giving us "programmer wroted error message in program exeption message". like // raise getExeption("we got an error", sys) // here "we got an error" my func geting from error_message var. // then you able to ask me, then what job done by sys.exc.info() -> he giving us [page_name, line number, and others]