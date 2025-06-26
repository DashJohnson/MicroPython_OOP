import socket
from html import HTML_PAGE

class WebServer:
    def __init__(self, robot, ip, port=80):
        self.robot = robot
        self.ip = ip
        self.port = port

    def start(self): 
        addr = socket.getaddrinfo(self.ip, self.port)[0][-1]
        server = socket.socket()
        server.bind(addr) 
        server.listen(1) 
        print(f"Server running on http://{self.ip}")

        while True:
            client, addr = server.accept()
            request = client.recv(1024).decode()

            if 'task=aisle1' in request:
                self.robot.go_to_aisle_1()
            elif 'task=aisle2' in request:
                self.robot.go_to_aisle_2()
            elif 'task=stop' in request:
                self.robot.stop()
            elif 'task=aisle3' in request:
                self.robot.go_to_aisle_3()
            elif 'task=aisle4' in request:
                self.robot.go_to_aisle_4()
            elif 'task=aisle5' in request:
                self.robot.go_to_aisle_5()
            elif 'task=aisle6' in request:
                self.robot.go_to_aisle_6()

            

            client.send("HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n")
            client.send(HTML_PAGE)
            client.close()
