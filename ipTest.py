import requests, socket
from flask import Flask
test = Flask(__name__)
test.secret_key = "random key generation here"

app2 = Flask(__name__)
app2.secret_key = "secret_key123"

@app2.route('/getIP')
def visits():
    # get the public ip address
    vendor_public_ip_addrs = requests.get('https://ipapi.co/ip/').text
    print(vendor_public_ip_addrs) #test
    print("Vendor IP Address: ", vendor_public_ip_addrs)

    ## getting the hostname by socket.gethostname() method
    hostname = socket.gethostname()
    ## getting the IP address using socket.gethostbyname() method
    client_public_ip_addrs = socket.gethostbyname(hostname)
    ## printing the hostname and ip_address
    print("Hostname: ", hostname)
    print("Client IP Address: ", client_public_ip_addrs)

    return "<h1>Client IP: "+client_public_ip_addrs+" Vendor IP: "+vendor_public_ip_addrs

if __name__ == '__main__':
    app2.run(debug=True)