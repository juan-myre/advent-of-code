"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
exports.__esModule = true;
exports.Shau = exports.CompanyCreateBody = exports.CompanyBody = exports.EntityBody = void 0;
var EntityBody = /** @class */ (function () {
    function EntityBody() {
    }
    return EntityBody;
}());
exports.EntityBody = EntityBody;
var CompanyBody = /** @class */ (function (_super) {
    __extends(CompanyBody, _super);
    function CompanyBody() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    return CompanyBody;
}(EntityBody));
exports.CompanyBody = CompanyBody;
var CompanyCreateBody = /** @class */ (function (_super) {
    __extends(CompanyCreateBody, _super);
    function CompanyCreateBody() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    return CompanyCreateBody;
}(CompanyBody));
exports.CompanyCreateBody = CompanyCreateBody;
var Shau = /** @class */ (function () {
    function Shau() {
    }
    return Shau;
}());
exports.Shau = Shau;
