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

const nebularPackageJsonPath = require.resolve('@nebular/theme/package.json');
const nebularPackageJson = JSON.parse(fs.readFileSync(nebularPackageJsonPath, 'utf8'));

if (nebularPackageJson.version !== '17.0.0') {
  throw new Error(`Expected @nebular/theme 17.0.0, found ${nebularPackageJson.version}`);
}

const nebularThemePath = path.join(path.dirname(nebularPackageJsonPath), 'fesm2022', 'nebular-theme.mjs');
const nebularSource = fs.readFileSync(nebularThemePath, 'utf8');
const nebularMarker = '// Angular 22 compatibility for Nebular 17';

if (!nebularSource.includes(nebularMarker)) {
  const nebularImport = "import { _VIEW_REPEATER_STRATEGY, _DisposeViewRepeaterStrategy } from '@angular/cdk/collections';";
  const nebularReplacement = `${nebularMarker}\nimport { _DisposeViewRepeaterStrategy } from '@angular/cdk/collections';\nconst _VIEW_REPEATER_STRATEGY = new InjectionToken('_VIEW_REPEATER_STRATEGY');`;

  if (!nebularSource.includes(nebularImport)) {
    throw new Error('The expected Nebular 17 Angular CDK import was not found');
  }

  fs.writeFileSync(nebularThemePath, nebularSource.replace(nebularImport, nebularReplacement));
}
