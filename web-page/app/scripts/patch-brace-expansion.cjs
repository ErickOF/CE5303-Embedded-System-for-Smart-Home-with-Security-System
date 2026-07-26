const fs = require('node:fs');
const path = require('node:path');

const packageJsonPath = require.resolve('brace-expansion/package.json');
const packageJson = JSON.parse(fs.readFileSync(packageJsonPath, 'utf8'));

if (packageJson.version !== '5.0.8') {
  throw new Error(`Expected brace-expansion 5.0.8, found ${packageJson.version}`);
}

const commonJsPath = path.join(path.dirname(packageJsonPath), 'dist', 'commonjs', 'index.js');
const source = fs.readFileSync(commonJsPath, 'utf8');
const marker = '// Legacy CommonJS compatibility for minimatch 3';

if (!source.includes(marker)) {
  fs.appendFileSync(
    commonJsPath,
    `\n${marker}\nif (typeof exports.expand === 'function') {\n  module.exports = exports.expand;\n  module.exports.expand = exports.expand;\n}\n`,
  );
}
