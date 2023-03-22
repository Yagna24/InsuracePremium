from Insurance_Premium.logger import logging
from Insurance_Premium.exception import InsuranceException
import os,sys
from Insurance_Premium.utils import get_collection_as_dataframe

# def test_logger_and_exception():
    
#     try : 
#         logging.info("Starting the test_logger_and_exception")
#         result = 3/0
#         print(result)
#         logging.info("Ending point of test_logger_and_exception")
#     except Exception as ex : 
#         logging.debug(str(ex))
#         raise InsuranceException(ex, sys)


if __name__ == '__main__':
    try :
        # test_logger_and_exception()
        get_collection_as_dataframe(database_name="INSURANCE", collection_name= "INSURANCE_PROJECT")
    
    except Exception as ex :
        print(ex)