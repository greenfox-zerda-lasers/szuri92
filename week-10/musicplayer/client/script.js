 'use strict';
var playlistList = 0;





var musicSrcList = ['music/Calibra.mp3', 'music/Calyxa.mp3', 'music/CoDa.mp3', 'music/grafixa.mp3', 'music/Logista.mp3', 'music/wfla.mp3', 'music/Calibra.mp3', 'music/Calibra.mp3', 'music/Calibra.mp3', 'music/Calibra.mp3'];

var musicList = [{'Artist': 'Glude', 'title': 'Identity'},
                 {'Artist': 'Different Heaven', 'title': 'Safe And Sound'},
                 {'Artist': 'Floatinurboat', 'title': 'Spirit of Things'},
                 {'Artist': 'Ahrix', 'title': 'Nova'},
                 {'Artist': 'Warriyo', 'title': 'Mortals (feat. Laura Brehm)'},
                 {'Artist': 'Cartoon', 'title': 'C U Again'},
                 {'Artist': 'Glude', 'title': 'Identity'},
                 {'Artist': 'Glude', 'title': 'Identity'},
                 {'Artist': 'Glude', 'title': 'Identity'},
                 {'Artist': 'Glude', 'title': 'Identity'}];

var musicPic = ['url("music/calibrepic.jpg")', 'url("music/ctb.jpg")', 'url("music/dheavy.jpg")', 'url("music/fredv.jpg")', 'url("music/logistics.jpg")', 'url("music/dheavy.jpg")', 'url("music/calibrepic.jpg")', 'url("music/calibrepic.jpg")', 'url("music/calibrepic.jpg")', 'url("music/calibrepic.jpg")'];
var myAudio = document.querySelector('audio');

function createTrackList () {
  getPlaylist();
  let myimg = document.querySelector('.img_pic');
  let myh2 = document.querySelector('h2');
  let myp = document.querySelector('.tracks p');
  let myTracks = document.querySelector('.tracklist');
  for (let i = 0; i < musicSrcList.length; i++) {
    var track = document.createElement('div');
    track.setAttribute('class', 'single_track');
    track.innerText = i + 1 + ' : '  + musicList[i]['title'] + ' (' + musicList[i]['Artist'] + ')';
    myTracks.appendChild(track);
  }
  let alltracks = document.querySelectorAll('.single_track');
  alltracks.forEach(function(e, i){
    e.addEventListener('click', function(e){
      randomcolor = random(200);
      console.log(randomcolor);
      removeId(alltracks);
      changeWave(musicSrcList[i]);
      alltracks[i].setAttribute('id', 'playing');
      myh2.innerText = musicList[i]['title'];
      myp.innerText = musicList[i]['Artist'];
      myimg.style.backgroundImage = musicPic[i];
    });
  });
}


function getPlaylist() {
  let xhr = new XMLHttpRequest();
  xhr.open("GET", "http://localhost:3000/playlists");
  xhr.send();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      playlistList = JSON.parse(xhr.response);
      let myPlaylist = document.querySelector('.playlist_list');
      console.log(myPlaylist);
      playlistList.forEach(function(item){
        var newP = document.createElement('p');
        newP.innerText = item.playlist;
        myPlaylist.appendChild(newP);
      });
    }
  }
}

function removeId(elements) {
  elements.forEach(function(e, i){
    elements[i].removeAttribute('id');
  });
}

function changeWave(item) {
  sound.stop();
  sound = preload();
  sound = loadSound(item);
}


createTrackList();
