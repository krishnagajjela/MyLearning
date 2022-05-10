from flask import Flask, request, session
import requests, uuid, datetime
import socket

app2 = Flask(__name__)
app2.secret_key = "secret_key123"

# --------------------------------------------------------------------------------------------------------------------------------------
# get the ip address in the form of uuid
uuid = uuid.uuid4()

# get the timestamp
# current date and time
tnow = datetime.datetime.now()
timestamp = tnow.strftime("%Y-%m-%dT%H:%M:%S") + tnow.strftime('.%f')[:4] + 'Z'
print(str(timestamp))
#get the public ip address
public_ip_addrs = requests.get('https://ipapi.co/ip/').text


## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
local_ip_address = socket.gethostbyname(hostname)
## printing the hostname and ip_address
print("Hostname: ", hostname)
print("IP Address: ", local_ip_address)

fraud_prevention_headers_list = {"Accept": "application/vnd.hmrc.1.0+json",
                                 "Gov-Client-Connection-Method": "WEB_APP_VIA_SERVER",
                                 "Gov-Client-Browser-Do-Not-Track": "false",
                                 "Gov-Client-Browser-Plugins": None, "Gov-Client-Device-ID": str(uuid),
                                 "Gov-Client-Local-IPs": str(local_ip_address),
                                 "Gov-Client-Local-IPs-Timestamp": str(timestamp), "Gov-Client-Multi-Factor": None,
                                 "Gov-Client-Public-IP": str(public_ip_addrs),
                                 "Gov-Client-Public-IP-Timestamp": str(timestamp), "Gov-Client-Public-Port": "5000",
                                 "Gov-Client-User-IDs": "myvatapp=apptest123",
                                 "Gov-Client-Screens": "width=1920&height=1080&scaling-factor=1&colour-depth=16,width=3000&height=2000&scaling-factor=1.25&colour-depth=16",
                                 "Gov-Client-Timezone": "UTC+05:30", "Gov-Vendor-License-IDs": None,
                                 "gov-vendor-product-name": "Minerals Technologies VAT",
                                 "Gov-Client-Window-Size": "width=1256&height=803",
                                 "Gov-Vendor-Version": "app=v1.0&servcode=v1.0", "Gov-Vendor-Public-IP": "49.204.189.172",
                                 "gov-vendor-forwarded": "by=49.204.189.172&for="+str(public_ip_addrs)}

s = requests.session()
s.headers.update(fraud_prevention_headers_list)

# --------------------------------------------------------------------------------------------------------------------------------------


@app2.route('/')
def index():
    user_agent = request.headers.get('User-Agent')

    # test = request.cookies.get('client_window', None)
    print(user_agent)
    # print(test)
    session['user_agent'] = user_agent
    return 'FlaskTest1 -- Hello IIS from Flask framework.'

@app2.route("/hello")
def test():
    x = session['user_agent']
    return "Hello calling"+str(x)


if __name__ == '__main__':
    app2.run(debug=True)