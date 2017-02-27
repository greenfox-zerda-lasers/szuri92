// alpha version, trying with {name: 'x', dep: 'y'} objects;

var vacationModule = (function () {

var createArray = function (obj) {
   var result = [];
   result.push(obj.dep, obj.name);
   return result
}

var insertItem = function (array, item, index) {
  var result = [];
  result = array.splice(index, 0, item);
  return array;
}

var createDestination = function(listOfObj) {
  var destination = [];
  for (var i = 0; i < listOfObj.length; i++) {
    if (destination.indexOf(listOfObj[i].name) === -1 && destination.indexOf[i].depende)
    var depArray = createArray(listOfObj[i]);
    destination.push(depArray[1], depArray[0]);
  }
}

return {
  createArray: createArray,
  insertItem: insertItem
};

})();

module.exports = vacationModule;
