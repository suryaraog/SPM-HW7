# acceptance_test_feature_a.py
import io
import sys
from features import SprintVelocity

def acceptance_test_sprint_velocity(happy_path=True):
    """
    Acceptance test for the SprintVelocity feature.

    Args:
    - happy_path (bool): If True, test the happy path scenario; otherwise, test an unhappy path.
    """
    sprint_velocity = SprintVelocity()

    # Redirect standard output to capture the print statements
    captured_output = io.StringIO()
    sys.stdout = captured_output

    if happy_path:
        # Happy path scenario: valid sprint points are provided.
        test_points = [10, 20, 30]
        expected_velocity = sum(test_points) / len(test_points)
        sprint_velocity.sprint_points = test_points
    else:
        # Unhappy path scenario: no sprint points are provided.
        test_points = []
        expected_velocity = 0

    # Calculate and display the velocity.
    actual_velocity = sprint_velocity.calculate_velocity()
    sprint_velocity.display_velocity()

    # Reset redirection
    sys.stdout = sys.__stdout__

    # Check if the calculated velocity matches the expected velocity.
    assert actual_velocity == expected_velocity, (
        f"Test failed: Expected velocity was {expected_velocity}, but got {actual_velocity}."
    )

    # Check if the printed output matches the expected output
    output = captured_output.getvalue()
    expected_output = f"\nCalculated Sprint Velocity: {expected_velocity} points per sprint\n"
    assert expected_output in output, (
        f"Test failed: Expected output was {expected_output}, but got {output}."
    )
    print("Test passed: The calculated velocity and the output match the expected values.")

# Running the acceptance test
if __name__ == "__main__":
    # You can toggle between the happy path and unhappy path by changing this parameter.
    acceptance_test_sprint_velocity(happy_path=False)
