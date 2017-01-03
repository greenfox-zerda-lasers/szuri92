 'use strict';

 // var wavesurfer = WaveSurfer.create({
 //     container: '#waveform',
 //     waveColor: '#b4b4b4',
 //     progressColor: '#ABE7E5',
 //     width: '50%'
 // });
 //
 //
 // wavesurfer.load('music/Calyxa.mp3');


var musicSrcList = ['music/Calibra.mp3', 'music/Calyxa.mp3', 'music/CoDa.mp3', 'music/grafixa.mp3', 'music/Logista.mp3', 'music/wfla.mp3'];

var musicList = [{'Artist': 'Glude', 'title': 'Identity'},
                 {'Artist': 'Different Heaven', 'title': 'Safe And Sound'},
                 {'Artist': 'Floatinurboat', 'title': 'Spirit of Things'},
                 {'Artist': 'Ahrix', 'title': 'Nova'},
                 {'Artist': 'Warriyo', 'title': 'Mortals (feat. Laura Brehm)'},
                 {'Artist': 'Cartoon', 'title': 'C U Again'}];

var musicPic = ['url("music/calibrepic.jpg")', 'url("music/ctb.jpg")', 'url("music/dheavy.jpg")', 'url("music/fredv.jpg")', 'url("music/logistics.jpg")', 'url("music/dheavy.jpg")'];
var myAudio = document.querySelector('audio');

function createTrackList () {
  let myimg = document.querySelector('.img_pic');
  let myh2 = document.querySelector('h2');
  let myp = document.querySelector('.tracks p');
  let myOl = document.querySelector('ol');
  for (let i = 0; i < musicSrcList.length; i++) {
    var myLi = document.createElement('li');
    myLi.innerText = musicList[i]['title'] + ' (' + musicList[i]['Artist'] + ')';
    myOl.append(myLi);
  }
  let allLi = document.querySelectorAll('li');
  allLi.forEach(function(e, i){
    e.addEventListener('click', function(e){
      myAudio.setAttribute('src', musicSrcList[i]);
      removeId(allLi);
      allLi[i].setAttribute('id', 'playing');
      myh2.innerText = musicList[i]['title'];
      myp.innerText = musicList[i]['Artist'];
      myimg.style.backgroundImage = musicPic[i];
    });
  });
}

function removeId(elements) {
  elements.forEach(function(e, i){
    elements[i].removeAttribute('id');
  });
}


createTrackList();
