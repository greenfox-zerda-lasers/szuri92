var fft;
var effectCounter = 0;
var num = 128;
var slider;
var duration;
var randomcolor = 10
function preload(){
  sound = loadSound('music/CoDa.mp3');
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
  var cnv = createCanvas(365,300);
  colorMode(HSB);
  angleMode(DEGREES);
  cnv.mouseClicked(togglePlay);
  slider = createSlider(0, 100, 100);
  myduration = createSlider(0, sound.duration(), 0);
  //myduration.style('width', '345px')
  fft = new p5.FFT(0.9, num);
  sound.amp(0.5);
  w = width / num;
  console.log(myduration);
  var greenfox = document.querySelector('canvas');
  var mycanvas = document.querySelector('#mycanvas');
  mycanvas.appendChild(greenfox);
  var sliders = document.querySelectorAll('input');
  sliders.forEach(function(item){
    mycanvas.appendChild(item);
  });
  myduration.mouseClicked(setMusicDuration);
  //sound.changed(setTimeLel);
  button = createButton('Effects');
  myButton = document.querySelector('button')
  mycanvas.appendChild(myButton);
  button.mouseClicked(function(){
    if( effectCounter >= 2) {
      effectCounter = 0;
    } else {
    effectCounter += 1;
  }
  });
}

function draw() {
  background(0, 0, 90);
  var spectrum = fft.analyze();
  var volButton = slider.value();
  sound.setVolume(volButton/100);


  //var durationButton = myduration.value();
  //myduration.value(sound.currentTime());
  var spectrum = fft.analyze();
  var waveform = fft.waveform();

  if ( effectCounter === 0 ) {
    translate(width/2, height/2);
    for (var i =0; i < spectrum.length; i++) {
    noFill();
    strokeWeight(2);
    stroke(i, 255,255);
    var amp = spectrum[i];
    var y = map(amp, 0, 255, 0, height - 20);
    ellipse(0, 0, y, y);
    }
  }
  else if ( effectCounter === 1 ) {
    translate(width/2, height/2);
    for (var i = 0; i < spectrum.length; i++) {
      var angle = map(i, 0, waveform.length, 0, 360);
      var amp = waveform[i];
      var r = map(amp, -1, 1, 10, height/2);
      var x = r*cos(angle);
      var y = r*sin(angle);
      stroke(i+randomcolor, 96, 96);
      line(0, 0,x, y);
    }
  }
  else if ( effectCounter === 2 ) {
    noStroke();
    for ( var i = 0; i < spectrum.length; i++ ) {
    var amp = spectrum[i];
    var y = map( amp, 0, 255, height, 0 );
    fill( i+20, 240, 240 );
    rect(i*w, y, w, height);
    }
  }
  strokeWeight(2);
}

function setMusicDuration() {
  var myclick = myduration.value();
  console.log(myclick);
  sound.jump(myclick);
}

function setTimeLel() {
  myduration.value(sound.currentTime());
}
