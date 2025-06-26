import socket
from html import HTML_PAGE, LOGIN_PAGE

class WebServer:
    def __init__(self, robot, ip, port=80):
        self.robot = robot
        self.ip = ip
        self.port = port
        self.user_email = "admin@example.com"
        self.user_password = "robotpass"
        self.is_authenticated = False

    def parse_form_data(self, request):
        def url_decode(s):
            res = ''
            i = 0
            while i < len(s):
                if s[i] == '%':
                    hex_val = s[i+1:i+3]
                    res += chr(int(hex_val, 16))
                    i += 3
                elif s[i] == '+':
                    res += ' '
                    i += 1
                else:
                    res += s[i]
                    i += 1
            return res

        try:
            body_start = request.find("\r\n\r\n") + 4
            body = request[body_start:]
            form = {}
            for pair in body.split("&"):
                if "=" in pair:
                    k, v = pair.split("=", 1)
                    form[url_decode(k)] = url_decode(v)
            return form
        except:
            return {}

    def start(self):
        addr = socket.getaddrinfo(self.ip, self.port)[0][-1]
        server = socket.socket()
        server.bind(addr)
        server.listen(1)
        print(f"Server running on http://{self.ip}")

        while True:
            client, addr = server.accept()
            request = b""
            while True:
                chunk = client.recv(1024)
                if not chunk:
                    break
                request += chunk
                if b"\r\n\r\n" in request:
                    break

            request = request.decode()
            print("REQUEST RECEIVED:\n", request)

            # Handle login
            if not self.is_authenticated:
                if request.startswith("POST"):
                    form = self.parse_form_data(request)
                    print("Parsed login form:", form)
                    email = form.get("email", "")
                    password = form.get("password", "")

                    if email == self.user_email and password == self.user_password:
                        self.is_authenticated = True
                        print("✅ Login successful")
                        client.send(b"HTTP/1.1 302 Found\r\nLocation: /\r\n\r\n")
                        client.close()
                        continue
                    else:
                        print("❌ Invalid login attempt")
                        client.send(b"HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n")
                        client.send(LOGIN_PAGE.encode())
                        client.close()
                        continue
                else:
                    client.send(b"HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n")
                    client.send(LOGIN_PAGE.encode())
                    client.close()
                    continue

            # After login: Robot command interface
            if 'task=aisle1' in request:
                self.robot.go_to_aisle_1()
            elif 'task=aisle2' in request:
                self.robot.go_to_aisle_2()
            elif 'task=aisle3' in request:
                self.robot.go_to_aisle_3()
            elif 'task=aisle4' in request:
                self.robot.go_to_aisle_4()
            elif 'task=aisle5' in request:
                self.robot.go_to_aisle_5()
            elif 'task=aisle6' in request:
                self.robot.go_to_aisle_6()
            elif 'task=stop' in request:
                self.robot.stop()

            distance = self.robot.get_distance()
            speed = getattr(self.robot, "last_speed", 0.0)

            html_response = HTML_PAGE.replace("[distance]", f"{distance:.2f}").replace("[speed]", f"{speed:.2f}")
            client.send(b"HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n")
            client.send(html_response.encode())
            client.close()
