// alpha version, trying with {name: 'x', dep: 'y'} objects;

var vacationModule = (function () {

var createArray = function (obj) {
   var result = [];
   result.push(obj.dep, obj.name);
   return result
}

return {
  createArray: createArray
};

})();

module.exports = vacationModule;
