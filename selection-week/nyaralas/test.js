var test = require('tape');
var solution = require('./solution.js');

test('createArray', function (t) {
    var actual = solution.createArray({name: 'a', dep: 'b'});
    var expected = ['b', 'a'];
    t.deepEqual(actual, expected);
    t.end();
});
