// Create a constructor for creating Aircrafts,
// and one for creating Carriers.

function Aircrafts (name) {
  this.name = name;
  this.ammo = 0;
  if (this.name == 'F16') {
    this.maxAmmo = 8;
    this.baseDmg = 30;
  } else if (this.name == 'F35') {
    this.maxAmmo = 12;
    this.baseDmg = 50;
  }
}

Aircrafts.prototype.stats = function () {
  console.log('Type: ' + this.name+", " + "Ammo: " + this.ammo +", " + "Base Damage: " + this.baseDmg + ", " + "All Damage: " + this.ammo*this.baseDmg);
}

Aircrafts.prototype.refill = function(ammoAmount) {
  var remain = 0;
  if (this.ammo + ammoAmount > this.maxAmmo) {
    remain = ammoAmount - (this.maxAmmo - this.ammo);
    this.ammo = this.maxAmmo;
    return remain;
  }
  this.ammo  += ammoAmount;
  return ammoAmount;
}

Aircrafts.prototype.fight = function () {
  ammoUsed = this.ammo;
  this.ammo = 0;
  return ammoUsed*this.baseDmg;
}

function Carrier(ammo) {
  this.healthPoint = 3000;
  this.totalAmmo = ammo;
  this.aircrafts = [];
}

Carrier.prototype.addAircraft = function(aircraft) {
  this.aircrafts.push(aircraft);
}

Carrier.prototype.fill = function () {
  for(let i = 0; i < this.aircrafts.length && this.totalAmmo; i++) {
    var fillCount = this.aircrafts[i].refill(this.aircrafts[i].maxAmmo-this.aircrafts[i].ammo);
      console.log(this.aircrafts[i].ammo);
      //console.log(fillCount);
      this.totalAmmo -= fillCount;
  }
}

Carrier.prototype.cFight = function () {
  totalDmg = 0
  for(let i = 0; i < this.aircrafts.length; i++) {
    totalDmg += this.aircrafts[i].fight()
  }
  return totalDmg;
}

Carrier.prototype.statusReturn = function () {
  totaldmg = 0;
  for(let i = 0; i < this.aircrafts.length; i++) {
    totalDmg += this.aircrafts[i].ammo * this.aircrafts[i].baseDmg;
  }
  console.log("Aircraft count: " + this.aircrafts.length + " Ammo Storage: " + this.totalAmmo + " Total damage: " + totalDmg +  " Health Remaining: " + this.healthPoint);
  for(let i = 0; i < this.aircrafts.length; i++) {
    this.aircrafts[i].stats();
  }
}



var f161 = new Aircrafts('F16');
var f162 = new Aircrafts('F16');
var f351 = new Aircrafts("F35");
f161.stats();
console.log(f161.maxAmmo);
f161.refill(2);
console.log(f161.ammo);
console.log(f161.refill(10));
console.log(f161.fight());
console.log(f162.refill(8))
console.log(f161.ammo);
console.log(f161.refill(10));
f161.stats();
var carrier = new Carrier(500);
carrier.addAircraft(f161);
carrier.addAircraft(f351);
carrier.addAircraft(f162);
console.log(carrier.aircrafts);
console.log(carrier.totalAmmo);
carrier.fill();
console.log(carrier.aircrafts);
console.log(carrier.totalAmmo);
console.log(carrier.cFight());
console.log(carrier.aircrafts);
carrier.fill();
console.log(carrier.aircrafts);
console.log(carrier.totalAmmo);
f161.stats();
carrier.statusReturn();
