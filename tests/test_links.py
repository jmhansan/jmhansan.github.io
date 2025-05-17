import re
from pathlib import Path
import unittest

class TestLinks(unittest.TestCase):
    def test_html_links_exist(self):
        repo_root = Path(__file__).resolve().parents[1]
        html_files = list(repo_root.rglob('*.html'))
        references = []
        pattern = re.compile(r'href=["\']([^"\']+\.html)["\']')
        for html_file in html_files:
            text = html_file.read_text(encoding='utf-8', errors='ignore')
            for target in pattern.findall(text):
                references.append((html_file, target))

        missing = []
        for html_file, target in references:
            target_path = (html_file.parent / target).resolve()
            if not target_path.exists():
                missing.append((html_file.relative_to(repo_root), target))

        self.assertFalse(missing, f'Missing html files: {missing}')

if __name__ == '__main__':
    unittest.main()
