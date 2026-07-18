from acceleration import calculate_traction, estimate_zero_to_sixty
import pytest


def test_calculate_traction():
    result = calculate_traction("good", "performance", "dry", "awd")
    assert result == 1.15

    result = calculate_traction("low", "snow", "snowy", "fwd")
    assert result == 0.50   # Limited by minimum traction


def test_estimate_zero_to_sixty():
    result = estimate_zero_to_sixty(
        3000,
        300,
        1.0,
        "automatic",
        "experienced"
    )
    assert result == 6.03

    result = estimate_zero_to_sixty(
        3000,
        300,
        1.2,
        "manual",
        "beginner"
    )
    assert result == 5.63