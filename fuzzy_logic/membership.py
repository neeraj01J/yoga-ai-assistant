
def triangular_membership(x, a, b, c):
    """
    Calculate the membership degree
    using a triangular membership function.
    """

    # Step 1: Validate triangle parameters
    if not (a < b < c):
        raise ValueError(
            "Invalid triangle: a must be less than b "
            "and b must be less than c."
        )

    # Step 2: Outside the triangle
    if x <= a or x >= c:
        return 0.0

    # Step 3: Peak of the triangle
    elif x == b:
        return 1.0

    # Step 4: Rising side
    elif x < b:
        return (x - a) / (b - a)

    # Step 5: Falling side
    else:
        return (c - x) / (c - b)


# Test values
print(
    "Membership for 5 minutes:",
    triangular_membership(5, 5, 15, 30)
)

print(
    "Membership for 15 minutes:",
    triangular_membership(15, 5, 15, 30)
)

print(
    "Membership for 20 minutes:",
    triangular_membership(20, 5, 15, 30)
)

print(
    "Membership for 25 minutes:",
    triangular_membership(25, 5, 15, 30)
)

print(
    "Membership for 30 minutes:",
    triangular_membership(30, 5, 15, 30)
)


# Test invalid triangle
try:
    print(
        "Invalid triangle:",
        triangular_membership(20, 30, 15, 5)
    )

except ValueError as error:
    print("Error:", error)