from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from router import Router
    from data import Data

from typing import Union
from myTypes import ipType


class Server:
    __initIp: ipType = 0
    __buffer: list[Data.string] = []
    router: Union[None, Router] = None
    __ip: ipType = 0

    def __new__(cls, *args, **kwargs):
        cls.__initIp += 1
        return super().__new__(cls)

    def __init__(self) -> None:
        self.__ip = Server.__initIp

    def get_ip(self) -> ipType:
        return self.__ip

    def set_router(self, router: Router):

        self.__router = router

    def clear_router(self):
        self.__router = None

    def set_data(self, data: Data):
        self.__buffer.append(data.string)

    def send_data(self, data: Data):
        print(data.string)
        if self.__router:
            self.__router.set_buffer(data)

    def get_data(self):
        return self.__buffer


if __name__ == "__main__":
    server1 = Server()
    server2 = Server()
    server3 = Server()

    print(server1.__ip)
    print(server2.__ip)
    print(server3.__ip)
