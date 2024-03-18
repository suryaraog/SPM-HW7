# acceptance_test_feature_b.py
import io
import sys
from features import TeamMember, TeamCapacity

def acceptance_test_team_capacity(happy_path=True):
    """
    Acceptance test for the TeamCapacity feature.

    Args:
    - happy_path (bool): If True, test the happy path scenario; otherwise, test an unhappy path.
    """
    team_capacity = TeamCapacity()

    # Redirect standard output to capture the print statements
    captured_output = io.StringIO()
    sys.stdout = captured_output

    if happy_path:
        # Happy path scenario: valid team member details are provided.
        team_capacity.team_members.append(TeamMember(days_off=2, ceremony_hours=4, hours_per_day=(8, 10), sprint_days=10))
        team_capacity.team_members.append(TeamMember(days_off=0, ceremony_hours=2, hours_per_day=(6, 8), sprint_days=10))
        expected_capacity = 68 + 68  # Expected capacity based on the provided details
    else:
        # Unhappy path scenario: no team members are added.
        expected_capacity = 0

    # Calculate and display the team capacity.
    actual_capacity = team_capacity.calculate_team_capacity()
    team_capacity.display_team_capacity()

    # Reset redirection
    sys.stdout = sys.__stdout__

    # Check if the calculated capacity matches the expected capacity.
    assert actual_capacity == expected_capacity, (
        f"Test failed: Expected team capacity was {expected_capacity}, but got {actual_capacity}."
    )

    # Check if the printed output matches the expected output
    output = captured_output.getvalue()
    expected_output = f"\nTotal Team Capacity: {expected_capacity} effort-hours\n"
    assert expected_output in output, (
        f"Test failed: Expected output was {expected_output.strip()}, but got {output.strip()}."
    )
    print("Test passed: The calculated capacity and the output match the expected values.")

# Running the acceptance test
if __name__ == "__main__":
    # You can toggle between the happy path and unhappy path by changing this parameter.
    acceptance_test_team_capacity(happy_path=True)
