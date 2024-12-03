import unittest
from main import fetch_dependencies, build_dot_graph


class TestDependencyVisualizer(unittest.TestCase):
    def test_fetch_dependencies(self):
        dependencies = fetch_dependencies("express", version="latest", max_depth=1)
        self.assertIsInstance(dependencies, dict)
        self.assertIn("body-parser", dependencies)

    def test_build_dot_graph(self):
        dependencies = {
            "express": {
                "body-parser": {},
                "cookie-parser": {},
            }
        }
        dot_graph = build_dot_graph("express", dependencies)
        self.assertIn('"express" -> "body-parser";', dot_graph)
        self.assertIn('"express" -> "cookie-parser";', dot_graph)


if __name__ == "__main__":
    unittest.main()
