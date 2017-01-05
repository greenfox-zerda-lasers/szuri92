'use strict';
var bodyParser = require('body-parser')
var express = require('express');
var mysql = require('mysql');
var app = express();
app.use(bodyParser.json());

var con = mysql.createConnection({
  host: "localhost",
  user: "'root'",
  password: "cerna2",
  database: "music"
});
app.use(express.static('../client'));

app.get('/playlists', function (req, res) {
  con.query('SELECT playlist FROM playlists;',function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
    res.send(rows);
  });
});

app.get('/playlist_track', function (req, res) {
  con.query('SELECT path, Artist, Title, Duration FROM tracks;',function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
    res.send(rows);
  });
});

app.get('/playlist_track/:playlist_id', function (req, res) {
  con.query('SELECT path, Artist, Title, Duration FROM tracks WHERE playlist_id =' + req.params.playlist_id + ';',function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
    res.send(rows);
  });
});


app.post('/playlists', function (req, res) {
  con.query('INSERT INTO playlists (playlist) VALUES (' + req.body.playlist + ');');
  res.send();
});


app.listen(3000);
