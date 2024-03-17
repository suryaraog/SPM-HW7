class SprintVelocity:
    """
    A class to calculate and display the sprint velocity of a team based on entered sprint points.

    Attributes:
        sprint_points (list): A list to store the points completed in each sprint.
    """

    def __init__(self):
        """
        Initializes the SprintVelocity class with an empty list for sprint points.
        """
        self.sprint_points = []

    def collect_sprint_points(self):
        """
        Collects sprint points from the user via command-line input.

        Continuously prompts the user to enter the points completed in each sprint,
        accepting only integer values. The user can type 'done' to finish entering points.
        """
        print("Enter sprint points (type 'done' to finish): ")
        while True:
            entry = input("> ")
            if entry.lower() == 'done':
                break
            try:
                point = int(entry)
                self.sprint_points.append(point)
            except ValueError:
                print("Please enter a valid integer or 'done' to finish.")

    def calculate_velocity(self):
        """
        Calculates the average sprint velocity based on the entered sprint points.

        Returns:
            float: The average sprint velocity. Returns 0 if no sprint points were entered.
        """
        if not self.sprint_points:
            print("No sprint points entered.")
            return 0
        return sum(self.sprint_points) / len(self.sprint_points)
    
    def display_velocity(self):
        """
        Calculates and displays the sprint velocity.

        Prints the calculated sprint velocity to the console in a user-friendly format.
        """
        velocity = self.calculate_velocity()
        print(f"\nCalculated Sprint Velocity: {velocity} points per sprint")


class TeamMember:
    """
    Represents a single team member, storing their availability and commitments.

    Attributes:
        days_off (int): The number of days off the team member has during the sprint.
        ceremony_hours (int): The number of hours the team member will spend in sprint ceremonies.
        hours_per_day (tuple): A tuple representing the minimum and maximum hours per day the team member is available.
        sprint_days (int): The total number of days in the sprint.
    """

    def __init__(self, days_off, ceremony_hours, hours_per_day, sprint_days):
        """
        Initializes a TeamMember instance with the provided details about their availability and commitments.

        Parameters:
            days_off (int): Number of days off during the sprint.
            ceremony_hours (int): Hours dedicated to sprint ceremonies.
            hours_per_day (tuple): Minimum and maximum available hours per day.
            sprint_days (int): Total sprint days.
        """
        self.days_off = days_off
        self.ceremony_hours = ceremony_hours
        self.hours_per_day = hours_per_day
        self.sprint_days = sprint_days

class TeamCapacity:
    """
    Calculates and displays the total team capacity in effort-hours for a sprint.

    Attributes:
        team_members (list): A list of TeamMember instances representing the sprint team.
    """

    def __init__(self):
        """
        Initializes the TeamCapacity class with an empty list for team members.
        """
        self.team_members = []

    def collect_team_members(self):
        """
        Collects details for each team member via command-line input until 'done' is entered.
        """
        print("\nEnter team member details (type 'done' when finished):")
        while True:
            days_off_input = input("Days off (or type 'done' to finish): ")
            if days_off_input.lower() == 'done':
                break
            ceremony_hours = int(input("Ceremony hours: "))
            hours_per_day_min = int(input("Minimum hours per day: "))
            hours_per_day_max = int(input("Maximum hours per day: "))
            sprint_days = int(input("Sprint days: "))
            
            member = TeamMember(
                days_off=int(days_off_input),
                ceremony_hours=ceremony_hours,
                hours_per_day=(hours_per_day_min, hours_per_day_max),
                sprint_days=sprint_days
            )
            self.team_members.append(member)

    def calculate_individual_capacity(self, member):
        """
        Calculates the available effort-hours for an individual team member.

        Parameters:
            member (TeamMember): The team member for whom to calculate capacity.

        Returns:
            float: The total available effort-hours for the team member.
        """
        avg_hours_per_day = sum(member.hours_per_day) / 2
        available_hours = (member.sprint_days - member.days_off) * avg_hours_per_day - member.ceremony_hours
        return available_hours

    def calculate_team_capacity(self):
        """
        Calculates the total available effort-hours for the entire team.

        Returns:
            float: The sum of available effort-hours for all team members.
        """
        return sum(self.calculate_individual_capacity(member) for member in self.team_members)
    
    def display_team_capacity(self):
        """
        Displays the calculated total team capacity in effort-hours.
        """
        capacity = self.calculate_team_capacity()
        print(f"\nTotal Team Capacity: {capacity} effort-hours")

# Main program execution
if __name__ == "__main__":  
    """
    Main execution point of the script.

    Prompts the user to select between testing the Sprint Velocity feature (Feature A) and the
    Team Capacity feature (Feature B). Based on the user's choice, it either calculates and displays
    the sprint velocity or the team's total capacity in effort-hours.
    """  
    print("Select feature to test:\n1. Sprint Velocity\n2. Team Capacity")
    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        # Create an instance of the SprintVelocity class
        sprint_velocity = SprintVelocity()
        # Collect sprint points from the user
        sprint_velocity.collect_sprint_points()
        # Display the calculated sprint velocity
        sprint_velocity.display_velocity()
    elif choice == '2':
        # Process for testing Team Capacity
        team_capacity = TeamCapacity()
        team_capacity.collect_team_members()
        team_capacity.display_team_capacity()
    else:
        print("Invalid choice.")