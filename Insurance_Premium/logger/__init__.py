import logging
from datetime import datetime
import os

LOG_DIR = "logs"

current_time_stamp =   f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

log_file_name = f"log_{current_time_stamp}.log"

os.makedirs(LOG_DIR, exist_ok = True)

log_file_path = os.path.join(LOG_DIR, log_file_name)

logging.basicConfig(filename= log_file_path, 
                    filemode='w',
                    format = '%(asctime)s %(name)-15s %(levelname)-8s %(message)s',
                    level = logging.DEBUG
                    # level = logging.INFO
                    )
