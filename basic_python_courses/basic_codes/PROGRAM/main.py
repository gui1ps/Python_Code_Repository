import server
import client
server1=server.server()
client1=client.client(server1.host,server1.port)
server1.server_start()
client1.client_connect()