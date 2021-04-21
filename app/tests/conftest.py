import pytest


@pytest.fixture
def num_to_round():
    return 0.1123


@pytest.fixture
def goal():
    class Goal(object):
        time = 120
        montly_contribution = 2500
        initial_contribution = 300000
        goal_value = 1750000

    return Goal
