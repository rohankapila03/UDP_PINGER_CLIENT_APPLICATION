import socket
import time
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1)
rrt = []

try:
    for i in range(1, 11):
        start_time = time.time()
        try:
            client_socket.sendto(
                ('Ping' + ' ' + str(i) + ' ' + str(time.time()) + ' Seconds').encode(), ('', 12000))
            message, messageAddress = client_socket.recvfrom(4096)
            recieve_message = message.decode()
            print(recieve_message)
            end_time = time.time()
            elapsed = end_time - start_time
            rrt.append(elapsed)
            print("RTT: " + str(elapsed) + " seconds \n")
        except socket.timeout:
            print('Requested Time out for: \n' + 'Ping' + ' ' + str(i) + '\n')
finally:
    min_rrt = min(rrt)
    max_rrt = max(rrt)
    average_rrt = sum(rrt)/len(rrt)
    packet_loss_rate = ((10 - len(rrt))/10)*100
    print('The Minimum RRT of all the Pings is: ' + str(min_rrt)+'seconds')
    print('The Maximum RRT of all the Pings is: ' + str(max_rrt)+'seconds')
    print('The Average RRT of all the Pings is: ' + str(average_rrt) + 'seconds')
    print('The packet loss percentage is: ' + str(packet_loss_rate) + '%')

    client_socket.close()
