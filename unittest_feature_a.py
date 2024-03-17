import unittest
from features import SprintVelocity  # Adjust the import as needed

class TestSprintVelocity(unittest.TestCase):

    def test_velocity_with_typical_points(self):
        # Happy path: typical list of sprint points
        """Test calculate_velocity with a standard list of sprint points (happy path)."""
        sprint_velocity = SprintVelocity()
        sprint_velocity.sprint_points = [10, 20, 30]
        expected = 20
        result = sprint_velocity.calculate_velocity()
        self.assertEqual(expected, result, f"Expected average velocity of {expected}, got {result}")

    def test_velocity_with_single_point(self):
        # Happy path: only one sprint point
        """Test calculate_velocity with only one sprint point (happy path)."""
        sprint_velocity = SprintVelocity()
        sprint_velocity.sprint_points = [50]
        expected = 50
        result = sprint_velocity.calculate_velocity()
        self.assertEqual(expected, result, f"Expected average velocity of {expected}, got {result}")

    def test_velocity_with_no_points(self):
        # Unhappy path: no sprint points
        """Test calculate_velocity with no sprint points entered (unhappy path)."""
        sprint_velocity = SprintVelocity()
        sprint_velocity.sprint_points = []
        expected = 0
        result = sprint_velocity.calculate_velocity()
        self.assertEqual(expected, result, f"Expected average velocity of {expected}, got {result}")

    def test_velocity_with_zero_points(self):
        # Unhappy path: sprint points include zero, which is valid but edge case
        """Test calculate_velocity with sprint points include zero (unhappy path)."""
        sprint_velocity = SprintVelocity()
        sprint_velocity.sprint_points = [0, 20, 40]
        expected = 20
        result = sprint_velocity.calculate_velocity()
        self.assertEqual(expected, result, f"Expected average velocity of {expected}, got {result}")

    def test_velocity_with_negative_points(self):
        # Unhappy path: sprint points include a negative value, assuming this to be handled gracefully
        sprint_velocity = SprintVelocity()
        sprint_velocity.sprint_points = [10, -20, 30]  # Assuming your logic handles negative values appropriately
        expected = "Some expected result"  # This should be your expected outcome based on how you handle negative values
        result = sprint_velocity.calculate_velocity()
        #  expected outcome and possibly the test based on how your application should handle negatives
        # self.assertEqual(expected, result, f"Expected average velocity of {expected}, got {result}")

if __name__ == '__main__':
    unittest.main(verbosity=2)
