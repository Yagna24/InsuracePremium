from Insurance_Premium.logger import logging
from Insurance_Premium.exception import InsuranceException
import os,sys

def test_logger_and_exception():
    
    try : 
        logging.info("Starting the test_logger_and_exception")
        result = 3/0
        print(result)
        logging.info("Ending point of test_logger_and_exception")
    except Exception as ex : 
        logging.debug(str(ex))
        raise InsuranceException(ex, sys)


if __name__ == '__main__':
    try :
        test_logger_and_exception()
    
    except Exception as ex :
        print(ex)