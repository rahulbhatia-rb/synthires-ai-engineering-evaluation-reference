import sys
import unittest
sys.path.append("src")
from rubric import Evaluation, summarize

class RubricTests(unittest.TestCase):
    def test_accepts_high_quality_answer(self): self.assertEqual(summarize(Evaluation(5,4,4))["decision"], "accept")
    def test_flags_weak_correctness(self): self.assertEqual(summarize(Evaluation(2,5,5))["decision"], "review")
    def test_rejects_invalid_score(self):
        with self.assertRaises(ValueError): summarize(Evaluation(6,4,4))
if __name__ == "__main__": unittest.main()
