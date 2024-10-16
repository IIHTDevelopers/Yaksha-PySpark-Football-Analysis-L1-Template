import unittest
from test.TestUtils import TestUtils

# Assuming the functions are defined in another module, you can import them like this:
from footballmain import *

class FunctionalTest(unittest.TestCase):

    def setUp(self):
        # Initialize TestUtils object
        self.test_obj = TestUtils()

        # The expected results from your analysis
        self.expected_results = {
            "top_goal_scorer": "Erling Haaland",
            "top_assist_provider": "Kevin De Bruyne",
            "best_goal_per_match_ratio": "Erling Haaland",
            "total_goals": 283,
            "total_assists": 173,
            "team_with_most_goals": "Paris Saint-Germain",
                    }

    def test_top_goal_scorer(self):
        try:
            result = get_top_goal_scorer(df)
            if result == self.expected_results["top_goal_scorer"]:
                self.test_obj.yakshaAssert("TestTopGoalScorer", True, "functional")
                print("TestTopGoalScorer = Passed")
            else:
                self.test_obj.yakshaAssert("TestTopGoalScorer", False, "functional")
                print("TestTopGoalScorer = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestTopGoalScorer", False, "functional")
            print("TestTopGoalScorer = Failed")

    def test_top_assist_provider(self):
        try:
            result = get_top_assist_provider(df)
            if result == self.expected_results["top_assist_provider"]:
                self.test_obj.yakshaAssert("TestTopAssistProvider", True, "functional")
                print("TestTopAssistProvider = Passed")
            else:
                self.test_obj.yakshaAssert("TestTopAssistProvider", False, "functional")
                print("TestTopAssistProvider = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestTopAssistProvider", False, "functional")
            print("TestTopAssistProvider = Failed")

    def test_best_goal_per_match_ratio(self):
        try:
            result = get_best_goal_per_match_ratio(df)
            if result == self.expected_results["best_goal_per_match_ratio"]:
                self.test_obj.yakshaAssert("TestBestGoalPerMatchRatio", True, "functional")
                print("TestBestGoalPerMatchRatio = Passed")
            else:
                self.test_obj.yakshaAssert("TestBestGoalPerMatchRatio", False, "functional")
                print("TestBestGoalPerMatchRatio = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestBestGoalPerMatchRatio", False, "functional")
            print("TestBestGoalPerMatchRatio = Failed")

    def test_total_goals(self):
        try:
            result = get_total_goals(df)
            if result == self.expected_results["total_goals"]:
                self.test_obj.yakshaAssert("TestTotalGoals", True, "functional")
                print("TestTotalGoals = Passed")
            else:
                self.test_obj.yakshaAssert("TestTotalGoals", False, "functional")
                print("TestTotalGoals = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestTotalGoals", False, "functional")
            print("TestTotalGoals = Failed")

    def test_total_assists(self):
        try:
            result = get_total_assists(df)
            if result == self.expected_results["total_assists"]:
                self.test_obj.yakshaAssert("TestTotalAssists", True, "functional")
                print("TestTotalAssists = Passed")
            else:
                self.test_obj.yakshaAssert("TestTotalAssists", False, "functional")
                print("TestTotalAssists = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestTotalAssists", False, "functional")
            print("TestTotalAssists = Failed")

    def test_team_with_most_goals(self):
        try:
            result = get_team_with_most_goals(df)
            if result == self.expected_results["team_with_most_goals"]:
                self.test_obj.yakshaAssert("TestTeamWithMostGoals", True, "functional")
                print("TestTeamWithMostGoals = Passed")
            else:
                self.test_obj.yakshaAssert("TestTeamWithMostGoals", False, "functional")
                print("TestTeamWithMostGoals = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestTeamWithMostGoals", False, "functional")
            print("TestTeamWithMostGoals = Failed")




if __name__ == '__main__':
    unittest.main()
