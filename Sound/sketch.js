var fft;
var num = 64;

function preload(){
  sound = loadSound('Dubz.mp3');
}

// fade sound if mouse is over canvas
function togglePlay() {
  if (sound.isPlaying()) {
    sound.pause();
  } else {
    sound.loop();
  }
}

function setup(){
  var cnv = createCanvas(1366,660);
  colorMode(HSB);
  angleMode(DEGREES);
  cnv.mouseClicked(togglePlay);
  fft = new p5.FFT(0.9, num);
  sound.amp(0.5);
  w = width / num;
}

function draw() {
  background(0);
  var spectrum = fft.analyze();
  //stroke(255);
  noStroke();
  for ( var i = 0; i < spectrum.length; i++ ) {
    var amp = spectrum[i];
    var y = map( amp, 0, 255, height/2, 10 );
    var c = map( w, 0, width/128, 0, (width/128)/3 )
    fill(i+240, 240, 240);
    rect(i*c, y, c, height/2 - y);
  }

  var waveform = fft.waveform();
  noFill();
  beginShape  ();
  strokeWeight(2);
  for ( var i = 0; i< waveform.length; i++ ){
    stroke(i ,255,255);
    var x = map( i, 0, waveform.length, width/3, width*2/3 );
    var y = map( waveform[i], -1, 1, 0, height/2 );
    var r = map(amp, -1, 1, 10, height/6);
    var angle = map(i, 0, waveform.length, 0, 360);
    vertex(x,y)
    quadraticVertex(x, y, x + 50, y + 50);
  }
  endShape();

  translate(width*5/6, 0);
  for (var i =0; i < spectrum.length; i++) {
    strokeWeight(1);
    stroke(i+100, 255,255);
    var amp = spectrum[i];
    var y = map(amp, 0, 255, 0, height/2 - 20);
    ellipse(0, height/2/2, y, y);
  }
  noStroke();

  translate(-width/3, height*3/4);
  strokeWeight(2);
  for (var i = 0; i < spectrum.length; i++) {
    var angle = map(i, 0, waveform.length, 0, 360);
    var amp = waveform[i];
    var r = map(amp, -1, 1, 10, height/6);
    var x = r*cos(angle);
    var y = r*sin(angle);
    stroke(i+126, 255, 255);
    line(0, 0,x, y);
  }
}
