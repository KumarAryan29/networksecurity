# Indise the logging folder there is already __init__.py file is present so this folder can also be created as package.

import logging  # Here  i am going to probably go ahead and give my logging configuration, this is really important because with respect to every execution of our modules, it is always necessary that we are try to log some information so that if there is an error that comes we will be able to debug it very easy way.

import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(),"logs", LOG_FILE)
os.makedirs(logs_path, exist_ok = True)     # This will create a log directory.

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",

    level = logging.INFO,
)


# Now what i can actually do is that i can import this logger.py file and i can call with respect to this logging itself, to log any details that i really want. If i just go ahead and write logging.info with the kind of message that i really want, it will be able to log each and eveything