const source = require("abstraction-audit-fixture-e0c2da42cfe6");
const generated = require("abstraction-audit-fixture-e0c2da42cfe6/generated.cjs");

exports.ingestionSourceControl = function ingestionSourceControl() { return source.sourceMarker(); };
exports.ingestionExecutionControl = function ingestionExecutionControl() { return generated.generatedMarker(); };
