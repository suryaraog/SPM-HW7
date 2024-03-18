import unittest
from features import TeamMember, TeamCapacity  # Adjust the import as needed

class TestTeamCapacity(unittest.TestCase):

    def setUp(self):
        """Setup reusable instances of TeamCapacity for each test."""
        self.team_capacity = TeamCapacity()
        self.team_member_1 = TeamMember(days_off=2, ceremony_hours=4, hours_per_day=(8, 10), sprint_days=10)
        self.team_member_2 = TeamMember(days_off=0, ceremony_hours=2, hours_per_day=(6, 8), sprint_days=10)

    def test_calculate_individual_capacity(self):
        """Test individual capacity calculation (happy path)."""
        expected_capacity = 68  # For team_member_1, assuming average hours per day
        result = self.team_capacity.calculate_individual_capacity(self.team_member_1)
        self.assertEqual(expected_capacity, result, f"Expected individual capacity of {expected_capacity}, got {result}")

    def test_calculate_team_capacity(self):
        """Test total team capacity calculation with multiple members (happy path)."""
        self.team_capacity.team_members = [self.team_member_1, self.team_member_2]
        expected_capacity = 68 + 68  # Sum of both members' capacities
        result = self.team_capacity.calculate_team_capacity()
        self.assertEqual(expected_capacity, result, f"Expected team capacity of {expected_capacity}, got {result}")

    def test_calculate_team_capacity_with_no_members(self):
        """Test total team capacity calculation with no team members (unhappy path)."""
        self.team_capacity.team_members = []  # No team members added
        expected_capacity = 0
        result = self.team_capacity.calculate_team_capacity()
        self.assertEqual(expected_capacity, result, f"Expected team capacity of {expected_capacity}, got {result}")

    def test_calculate_individual_capacity_with_extreme_hours(self):
        """Test individual capacity calculation with extreme working hours (unhappy path)."""
        extreme_member = TeamMember(days_off=0, ceremony_hours=0, hours_per_day=(12, 14), sprint_days=10)
        expected_capacity = 130  # Assuming average hours per day
        result = self.team_capacity.calculate_individual_capacity(extreme_member)
        self.assertEqual(expected_capacity, result, f"Expected individual capacity of {expected_capacity}, got {result}")

if __name__ == '__main__':
    unittest.main(verbosity=2)
