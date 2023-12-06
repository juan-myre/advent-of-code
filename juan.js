"use strict";
exports.__esModule = true;
var classes_1 = require("./classes");
console.log('juan bustamante');
var companyCreateBody = new classes_1.CompanyCreateBody();
var shau = new classes_1.Shau();
function passEntityDto(param) {
    console.log(param.id);
}
passEntityDto(shau);
