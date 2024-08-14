
class jpegView {
    constructor(container) {
        this.container = container;
        
        this.canvas = document.createElement('canvas', {id: 'ExJPG'});
        this.container.appendChild(this.canvas);
        this.container.onload = this.SetFormDefaults();
        //this.context = this.canvas.getContext('2d');
        // this.image = new Image();
        // this.image.onload = () => {
        //     this.context.drawImage(this.image, 0, 0, this.canvas.width, this.canvas.height);
        // };	
    }

	SetFormDefaults()
	{
		ExJPG.lastcheck = false;
		ExJPG.Interval = 100; // reducing this value does not seem to reduce the interval.
		ExJPG.Img = new Image();
		ExJPG.XMLHttpReq = new XMLHttpRequest();
		ExJPG.urlCreator = window.URL || window.webkitURL;
		ExJPG.funcGetjpegimage();
	}
    drawPlayer(container)
	{
        container_Element = document.getElementById(container);
        container_Element.innerHTML = `
        <div onload="SetFormDefaults();">
        	<div style="margin:5px">"
        		<canvas id="ExJPG" width="960" height="540"></canvas>
        </div>`;
    }
}
window.ExJPG = {
    lastcheck : false,
    dx : 0,
    dy : 0,
    blob : 0 ,
    urlCreator : 0,
    canvas : 0,
    context : 0,
    Img : 0,
    XMLHttpReq : 0,
    Interval : 1000,

    funcDraw:function(blob) {	
        ExJPG.canvas = document.getElementById("ExJPG");
        if (ExJPG.canvas == null) {
            ExJPG.lastcheck = true;
            return 0;
        }
        ExJPG.context = ExJPG.canvas.getContext("2d");
        ExJPG.Img.onload = function(evt) {
            ExJPG.context.drawImage(ExJPG.Img, ExJPG.dx, ExJPG.dy, 960, 540);
            ExJPG.urlCreator.revokeObjectURL(ExJPG.Img.src);
            return 0;
        };
        ExJPG.Img.src = ExJPG.urlCreator.createObjectURL(blob);
    },

    funcGetjpegimage:function() {
        ExJPG.XMLHttpReq.open("GET", "/jpg/", true, "", "");
        ExJPG.XMLHttpReq.responseType = "blob";	
        if (ExJPG.lastcheck) {
            return 0;
        }

        ExJPG.XMLHttpReq.onload = function(oEvent) {
            ExJPG.funcDraw(ExJPG.XMLHttpReq.response);
            setTimeout(function() {
                requestAnimationFrame(ExJPG.funcGetjpegimage);
            }, ExJPG.Interval);
            return 0;
        };
        ExJPG.XMLHttpReq.send(null);
    }
};