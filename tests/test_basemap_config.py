import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('inject', 'scripts/inject_basemap_key.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class BasemapConfigTests(unittest.TestCase):
    def test_injection_is_json_safe_and_artifact_only(self):
        with tempfile.TemporaryDirectory() as directory:
            previous = Path.cwd()
            try:
                os.chdir(directory)
                target = Path('docs/static/gis-from-scratch/basemap-config.json')
                target.parent.mkdir(parents=True)
                target.write_text('{"key":""}')
                with patch.dict(os.environ, {'CARTO_BASEMAP_KEY': 'test-"key'}):
                    module.inject()
                self.assertEqual(json.loads(target.read_text()), {'key': 'test-"key'})
                with patch.dict(os.environ, {'CARTO_BASEMAP_KEY': ''}):
                    with self.assertRaises(SystemExit):
                        module.inject()
            finally:
                os.chdir(previous)

    def test_committed_config_is_empty(self):
        for root in ['static', 'docs/static']:
            self.assertEqual(json.loads(Path(root, 'gis-from-scratch/basemap-config.json').read_text()), {'key': ''})
