function DjsFun(){
    var height = window.innerHeight;
    var width = window.innerWidth;
    var depth = screen.colorDepth;
    var browserDetails = height.toString()+":"+width.toString()+":"+depth.toString();

    const request = new XMLHttpRequest();
    request.open('POST', '/', true);
    request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    request.send('browserDetails=' + browserDetails);
}