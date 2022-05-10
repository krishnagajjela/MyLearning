let private_ip
function getip(json) {
    private_ip = json.ip;
    console.log(private_ip);
}

let p
function getIP(json) {
    p = json.ip;
    console.log(p);
  }
function bTesting(){

    var address = RTCIceCandidate.address;
    var height = window.innerHeight;
    var width = window.innerWidth;
    var depth = screen.colorDepth;
    var browserDetails = height.toString()+":"+width.toString()+":"+depth.toString()+":"+p.toString()+":";

    var request = new XMLHttpRequest();
    request.open('POST', '/', true);
    request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    request.send('browserDetails=' + browserDetails);
}
