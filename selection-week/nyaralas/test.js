var test = require('tape');
var solution = require('./solution.js');

test('createArray', function (t) {
    var actual = solution.createArray({name: 'a', dep: 'b'});
    var expected = ['b', 'a'];
    t.deepEqual(actual, expected);
    t.end();
});

test('insertToArray', function (t) {
    var actual = solution.insertItem(['a', 'b', 'c'], 'x', 0);
    var expected = ['x','a', 'b', 'c'];
    t.deepEqual(actual, expected);
    t.end();
});

test('insertToArray', function (t) {
    var actual = solution.insertItem(['a', 'b', 'c'], 'x', 1);
    var expected = ['a', 'x', 'b', 'c'];
    t.deepEqual(actual, expected);
    t.end();
});
