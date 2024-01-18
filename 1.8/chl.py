class Data:
    def __init__(self, data, ip) -> None:
        self.data = data
        self.ip = ip


class Server:
    ip_count = 1

    def __init__(self) -> None:
        self.ip = Server.ip_count
        Server.ip_count += 1
        self.buffer = []
        self.router = None

    def send_data(self, data: Data):
        self.router.buffer.append(data)

    def get_data(self):
        data = self.buffer
        self.buffer = []
        return data

    def get_ip(self):
        return self.ip


class Router:
    servers: list[Server] = []
    buffer: list[Data] = []

    def link(self, server: Server):
        self.servers.append(server)
        server.router = self

    def unlink(self, server: Server):
        self.servers.remove(server)
        server.router = None

    def send_data(self):
        for server_data in self.buffer:
            server_to = [
                server
                for server in self.servers
                if server.ip == server_data.ip
            ]
            if server_to:
                server_to = server_to[0]
                server_to.buffer.append(server_data)
        self.buffer.clear()


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
