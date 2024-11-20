import os
import sys
import logging




logging_str = '[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] [%(message)s]'
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
log_path = os.path.join('logs', 'app.log')


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler(sys.stdout)
    ]
)


logger = logging.getLogger('FakeNewsDetection')