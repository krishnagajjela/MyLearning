function browserTesting(){
    var height = window.innerHeight;
    var width = window.innerWidth;
    var depth = screen.colorDepth;
    var browserDetails = height.toString()+":"+width.toString()+":"+depth.toString();

    console.log(browserDetails)

    return browserDetails;
}