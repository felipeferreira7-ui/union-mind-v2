// Compatibility entry point: use the maintained Python generator.
const { spawnSync } = require('node:child_process');
const path = require('node:path');
const result = spawnSync(process.env.UNION_PYTHON || 'python3', [path.join(__dirname, 'scripts_build/generate_seo.py')], { stdio: 'inherit' });
if (result.error) console.error(result.error.message);
process.exit(result.status ?? 1);
