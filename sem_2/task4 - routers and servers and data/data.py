from typing import Union
from myTypes import ipType, dataStringType


class Data:

    string: Union[dataStringType, None] = None
    ip: Union[ipType, None] = None

    def __init__(self, dataString: dataStringType, ip: ipType):
        self.string = dataString
        self.ip = ip
