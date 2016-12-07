'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

var Student = {

    grades : [4, 5],
    addGrade : function (grade) {
      if ( grade <=5 && grade >=1)
      Student.grades.push(grade)
    },
    getAverage : function (){
      var sum = 0;
      for(var i = 0; i < Student.grades.length; i++) {
          sum += Student.grades[i];
      }
      sum /= Student.grades.length;
      return sum;
    }
};

Student.addGrade(2)
Student.addGrade(2)
Student.addGrade(4)
Student.addGrade(5)
Student.addGrade(1)
Student.addGrade(6)
console.log(Student.getAverage())
console.log(Student.grades)
