import yaml
import os
from pathlib import Path
from common import logger

logger=logger.Log().getlog()
logger.info("get login_data.")

login_data = os.path.join(Path(__file__).parent.parent, 'data', 'login_data.yaml')
# print(login_data)


def getData(file=login_data):
    with open(file, 'r') as f:
        data = yaml.safe_load(f)
    return data


# print(getData())
