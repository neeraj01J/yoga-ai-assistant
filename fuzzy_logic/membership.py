
"""
AI-Based Yoga Routine Selection Assistant
Fuzzy Logic - Time Membership Functions

This module calculates fuzzy membership degrees
for available yoga session time.

Author: Neeraj Jaiswar
"""

# ============================================================
# 1. TRIANGULAR MEMBERSHIP FUNCTION
# ============================================================

def triangular_membership(x, a, b, c):
    """
    Calculate membership degree using a triangular
    membership function.

    Parameters:
        x : float
            Input value.
        a : float
            Left endpoint.
        b : float
            Peak of the triangle.
        c : float
            Right endpoint.

    Returns:
        float:
            Membership degree between 0.0 and 1.0.

    Raises:
        ValueError:
            If triangle parameters are invalid.
    """

    # Validate triangle parameters
    if not (a < b < c):
        raise ValueError(
            "Invalid triangle: "
            "a must be less than b "
            "and b must be less than c."
        )

    # Check if input is outside the triangle
    if x <= a or x >= c:
        return 0.0

    # Peak of the triangle
    elif x == b:
        return 1.0

    # Rising side of the triangle
    elif x < b:
        return (x - a) / (b - a)

    # Falling side of the triangle
    else:
        return (c - x) / (c - b)


# ============================================================
# 2. FUZZY SET DEFINITIONS
# ============================================================

# Available yoga session time (minutes)

SHORT_TIME = (5, 15, 30)

MEDIUM_TIME = (15, 30, 45)

LONG_TIME = (30, 60, 90)


# ============================================================
# 3. INPUT VALIDATION
# ============================================================

def validate_time(minutes):
    """
    Validate available yoga session time.

    Parameters:
        minutes : float
            Available time in minutes.

    Raises:
        ValueError:
            If the time is invalid.
    """

    if not isinstance(minutes, (int, float)):
        raise ValueError(
            "Time must be a number."
        )

    if minutes < 0:
        raise ValueError(
            "Time cannot be negative."
        )


# ============================================================
# 4. CALCULATE TIME MEMBERSHIPS
# ============================================================

def calculate_time_memberships(minutes):
    """
    Calculate membership degrees for
    Short, Medium, and Long time.

    Parameters:
        minutes : float
            Available yoga session time.

    Returns:
        dict:
            Membership degrees for each fuzzy set.
    """

    # Validate input
    validate_time(minutes)

    # Calculate Short membership
    short_degree = triangular_membership(
        minutes,
        *SHORT_TIME
    )

    # Calculate Medium membership
    medium_degree = triangular_membership(
        minutes,
        *MEDIUM_TIME
    )

    # Calculate Long membership
    long_degree = triangular_membership(
        minutes,
        *LONG_TIME
    )

    # Return all membership degrees
    return {
        "Short": short_degree,
        "Medium": medium_degree,
        "Long": long_degree
    }


# ============================================================
# 5. DISPLAY MEMBERSHIP RESULTS
# ============================================================

def display_memberships(minutes):
    """
    Display fuzzy membership results
    in a readable format.
    """

    memberships = calculate_time_memberships(minutes)

    print(
        f"\nAvailable Yoga Time: {minutes} minutes"
    )

    print("-" * 40)

    for category, degree in memberships.items():
        print(
            f"{category} Time: {degree:.3f}"
        )

    print("-" * 40)


# ============================================================
# 6. TESTING
# ============================================================

def run_tests():
    """
    Test the fuzzy membership function
    using different time values.
    """

    print("\n========== FUZZY LOGIC TESTS ==========")

    test_values = [5, 15, 20, 25, 30, 45, 60, 90]

    for minutes in test_values:
        display_memberships(minutes)

    # Test invalid input
    print("\n========== INVALID INPUT TEST ==========")

    try:
        calculate_time_memberships(-10)

    except ValueError as error:
        print("Error:", error)


# ============================================================
# 7. MAIN PROGRAM
# ============================================================

def main():
    """
    Main entry point of the program.
    """

    print("=" * 50)

    print(
        "AI-BASED YOGA ROUTINE SELECTION ASSISTANT"
    )

    print(
        "FUZZY LOGIC - TIME MEMBERSHIP SYSTEM"
    )

    print("=" * 50)

    # Run fuzzy logic tests
    run_tests()


# Execute the program
if __name__ == "__main__":
    main()