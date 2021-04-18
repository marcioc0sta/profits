import numpy_financial as npf
from helpers.round import roundHelper


def Get_Goals(goal):
    raw_value = npf.rate(goal.time, -goal.montly_contribution, -
                         goal.initial_contribution, goal.goal_value)

    monthly = roundHelper(raw_value)
    yearly = round(pow(12 - 1, monthly), 2)

    return {
        "monthly": monthly,
        "yearly": yearly
    }
