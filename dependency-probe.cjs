const privateDependency = require("@naturellfil/private-dependency-cad27c7427e6");
const publicDependency = require("is-number");
exports.dependencyControl_cad27c7427e6 = value => publicDependency(value);
exports.privateDependencyProbe_cad27c7427e6 = () => privateDependency.privateDependencyCanary_cad27c7427e6();
