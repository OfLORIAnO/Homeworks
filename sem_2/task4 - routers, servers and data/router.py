from class_server import Server
from data import Data


class Router:

    connected__servers: set[Server] = set()
    buffer: list[Data] = []  # [[server1, data1], [server2, data2]]

    def link(self, server: Server):
        self.connected__servers.add(server)
        server.set_router(self)

    def unlink(self, server: Server) -> None:
        if server in self.connected__servers:
            self.connected__servers.remove(server)
            server.clear_router()

    def set_buffer(self, data: Data):
        self.buffer.append(data)

    def clean_buffer(self):
        self.buffer.clear()

    def send_data(self):
        for buff in self.buffer:
            for server in self.connected__servers:
                if buff.ip == server.get_ip():
                    server.set_data(buff)
