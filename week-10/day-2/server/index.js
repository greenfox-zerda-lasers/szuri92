'use strict';

var bodyParser = require('body-parser')
var express = require('express');

var app = express();
app.use(bodyParser.json());

var tracks = ['John', 'Betty', 'Hal'];
var playlist = [
    { "id": 21, "title": "Halahula", "artist": "Untitled artist", "duration": 545, "path": "c:/music/halahula.mp3" },
    { "id": 412, "title": "No sleep till Brooklyn", "artist": "Beastie Boys", "duration": 312.12, "path": "c:/music/beastie boys/No sleep till Brooklyn.mp3" }
]

app.get('/playlists', function (req, res) {
  res.json(tracks);
});

app.get('/playlists/playlist', function (req, res) {
  res.json(playlist);
});

app.get('/playlists/:id', function (req, res) {
  res.send(tracks[req.params.id]);
});


app.delete('/playlists/:id', function (req, res) {
  var newList = [];
  for(let i = 0; i < tracks.length; i++){
    if ( i != req.params.id) {
      newList.push(tracks[i]);
    }
  }
  tracks = newList
  res.send(tracks);
});

app.post('/playlists', function (req, res) {
  console.log(req.body);
  tracks.push(req.body);
  res.send(tracks)
});

app.get('/playlis-tracks/', function (req, res) {
  res.send(playlist);
});


module.exports = app;
