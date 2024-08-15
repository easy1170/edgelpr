
class JpegView {
    constructor() {
      this.img_name = '';
      this.hostname='';
    }
	SetFormDefaults(){
		ExJPG.lastcheck = false;
		ExJPG.Interval = 100; // reducing this value does not seem to reduce the interval.
		ExJPG.Img = new Image();
		ExJPG.XMLHttpReq = new XMLHttpRequest();
		ExJPG.urlCreator = window.URL || window.webkitURL;
		ExJPG.funcGetjpegimage();
	}
  drawPlayer(container, jpg_url){
    this.container = container;
    this.jpg_url = jpg_url;

    this.canvas = document.createElement('canvas');
  	this.canvas.setAttribute("id","ExJPG")
  	this.canvas.setAttribute("width","384")
  	this.canvas.setAttribute("height","216")
    this.container.appendChild(this.canvas);
    console.log("ready to draw")
	  this.container.onload = this.SetFormDefaults();
    
  }
}
window.jpegView = new JpegView();
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
			var cw=ExJPG.canvas.width;
			var ch=ExJPG.canvas.height;
			var vw=ExJPG.Img.width;
			var vh=ExJPG.Img.height;
			//var th=cw*vh/vw;
			ExJPG.context.drawImage(ExJPG.Img,  0, 0, vw, vh, 0, 0, cw, ch);
            ExJPG.urlCreator.revokeObjectURL(ExJPG.Img.src);
            return 0;
        };
        ExJPG.Img.src = ExJPG.urlCreator.createObjectURL(blob);
    },

    funcGetjpegimage:function() {
		  const hostname = window.location.hostname; //window.jpegView.hostname
      const jpg_url = `http://${hostname}/${window.jpegView.jpg_url}`;
      console.log(jpg_url)
      ExJPG.XMLHttpReq.open("GET", jpg_url, true);
      ExJPG.XMLHttpReq.responseType = "blob";	
      if (ExJPG.lastcheck) {
          return 0;
      }

      ExJPG.XMLHttpReq.onload = function(oEvent) {
          ExJPG.funcDraw(ExJPG.XMLHttpReq.response);
          setTimeout(function() {
              requestAnimationFrame(ExJPG.funcGetjpegimage);
			  //console.log("request next")
          }, ExJPG.Interval);
          return 0;
      };
      ExJPG.XMLHttpReq.send(null);
	  //console.log("make empyt");
    }

};
