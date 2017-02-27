// alpha version, trying with {name: 'x', dep: 'y'} objects;
'use strict';

var vacationModule = (function () {

var testArr = [{name: 'u', dep: ''},
              {name: 'v', dep: 'w'},
              {name: 'w', dep: 'z'},
              {name: 'x', dep: 'u'},
              {name: 'y', dep: 'v'},
              {name: 'z', dep: ''}];

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
    console.log(destination);
    if (listOfObj[i].dep === '' && destination.indexOf(listOfObj[i].name) === -1) {
      destination.push(listOfObj[i].name);
    } else if (listOfObj[i].dep === '' && destination.indexOf(listOfObj[i].name) > -1) {
      continue;
    }
    else if (destination.indexOf(listOfObj[i].name) === -1 && destination.indexOf(listOfObj[i].dep) === -1) {
      var depArray = createArray(listOfObj[i]);
      destination.push(depArray[0], depArray[1]);
    } else if (destination.indexOf(listOfObj[i].name) > -1 && destination.indexOf(listOfObj[i].dep) === -1) {
        insertItem(destination, listOfObj[i].dep, destination.indexOf(listOfObj[i].name));
    } else if (destination.indexOf(listOfObj[i].name) === -1 && destination.indexOf(listOfObj[i].dep) > -1) {
        insertItem(destination, listOfObj[i].name, destination.indexOf(listOfObj[i].dep) + 1);
    }
  }
  return destination;
}

return {
  testArr: testArr,
  createArray: createArray,
  insertItem: insertItem,
  createDestination: createDestination
};

})();

console.log(vacationModule.createDestination(vacationModule.testArr));
module.exports = vacationModule;
