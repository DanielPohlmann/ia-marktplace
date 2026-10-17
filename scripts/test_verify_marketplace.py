import tempfile
import unittest
from pathlib import Path

import verify_marketplace as vm

VALID = """---
name: product-market-researcher
description: Researches competitors for an idea brief.
tools: WebSearch, WebFetch, Read
model: sonnet
---

Body.
"""


class CheckAgentTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, stem, text):
        path = self.dir / f"{stem}.md"
        path.write_text(text, encoding="utf-8")
        return path

    def test_valid_agent_has_no_errors(self):
        errors, _ = vm.check_agent(self.write("product-market-researcher", VALID), "product")
        self.assertEqual(errors, [])

    def test_name_must_match_file_name(self):
        errors, _ = vm.check_agent(self.write("product-other", VALID), "product")
        self.assertTrue(any("!= file name" in e for e in errors))

    def test_name_must_carry_plugin_prefix(self):
        text = VALID.replace("product-market-researcher", "market-researcher")
        errors, _ = vm.check_agent(self.write("market-researcher", text), "product")
        self.assertTrue(any("prefix" in e for e in errors))

    def test_unknown_model_is_rejected(self):
        text = VALID.replace("model: sonnet", "model: gpt")
        errors, _ = vm.check_agent(self.write("product-market-researcher", text), "product")
        self.assertTrue(any("model" in e for e in errors))

    def test_unexpected_key_is_rejected(self):
        text = VALID.replace("model: sonnet", "model: sonnet\nlicense: MIT")
        errors, _ = vm.check_agent(self.write("product-market-researcher", text), "product")
        self.assertTrue(any("'license'" in e for e in errors))

    def test_block_description_is_rejected(self):
        text = VALID.replace(
            "description: Researches competitors for an idea brief.",
            "description: |\n  Researches competitors.",
        )
        errors, _ = vm.check_agent(self.write("product-market-researcher", text), "product")
        self.assertTrue(any("description" in e for e in errors))

    def test_missing_frontmatter_is_rejected(self):
        errors, _ = vm.check_agent(self.write("product-market-researcher", "No frontmatter"), "product")
        self.assertTrue(any("frontmatter" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
