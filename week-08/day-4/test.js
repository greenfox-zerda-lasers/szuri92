var test = require('tape');
var add = require('./ex_39.js');
//******************************39*******************************
test('double a number', function (t) {
    var actual = add(2);
    var expected = 4;
    t.equal(actual, expected);
    t.end();
});

test('double zero', function(t) {
  var actual = add(0);
  var expected = 0;
  t.equal(actual, expected);
  t.end();
});

test('double a string', function(t) {
  var actual = add(5675);
  var expected = 5675*2
  t.equal(actual, expected);
  t.end();
});
//***********************************************************
//**************************40*******************************
var append = require('./ex_40');

test("add 'a' to bel", function(t) {
  var actual = append('bel');
  var expected =  'bela'
  t.equal(actual, expected);
  t.end();
});

test("add 'a' to 5", function(t) {
  var actual = append(5);
  var expected =  '5a'
  t.equal(actual, expected);
  t.end();
});

test("add 'a' to empty", function(t) {
  var actual = append('');
  var expected =  'a'
  t.equal(actual, expected);
  t.end();
});
//******************************************************
//*********************ex_41*******************************
var sum = require('./ex_41.js');

test("sum a normal array", function(t) {
  var actual = sum([1, 2, 3, 4]);
  var expected =  10
  t.equal(actual, expected);
  t.end();
});

test("sum array with a string", function(t) {
  var actual = sum([1, 2, 3, 'a', 5, 6]);
  var expected =  '6a56'
  t.equal(actual, expected);
  t.end();
});
//******************************************************************
//****************************ex_42************************************
var factorial = require('./ex_42.js');

test("small number", function(t) {
  var actual = factorial(2);
  var expected =  2
  t.equal(actual, expected);
  t.end();
});

test("check factorial of 0", function(t) {
  var actual = factorial(0);
  var expected =  1
  t.equal(actual, expected);
  t.end();
});

//**********************************************************
//*********************ex_43********************************
var filter = require('./ex_43.js');

test("test filter with simple array", function(t) {
  var actual = filter([1, 2, 3, 4, 5, 6])
  var expected =  [2,4,6]
  t.deepEqual(actual, expected);
  t.end();
});

test("test with odd numbers", function(t) {
  var actual = filter([1, 3]);
  var expected =  []
  t.deepEqual(actual, expected);
  t.end();
});

//****************************************************************
//*************************ex_44********************************
var minimal = require('./ex_44.js');

test("test minimal with simple array ", function(t) {
  var actual = minimal([1, 2, 0, 3, 4, 5, 6, 2]);
  var expected =  0
  t.equal(actual, expected);
  t.end();
});

test("test minimal with array with string", function(t) {
  var actual = minimal([1, 2, 0, 3, 4, 5, 6, 2, 'a']);
  var expected =  0
  t.equal(actual, expected);
  t.end();
});
//*********************************************************************
//***************ex_45.js*********************************************

var short = require('./ex_45.js');

test("test minimal with array with strings", function(t) {
  var actual = minimal(['a', 'al', 'alm', 'alma']);
  var expected =  'a'
  t.equal(actual, expected);
  t.end();
});

test("test minimal with array with an empty string", function(t) {
  var actual = minimal(['a', 'al', 'alm', 'alma', '']);
  var expected =  ''
  t.equal(actual, expected);
  t.end();
});
