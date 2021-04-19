import numpy_financial as npf
from app.helpers.round import round_helper


def get_goals(goal):
    raw_value = npf.rate(goal.time, -goal.montly_contribution, -
                         goal.initial_contribution, goal.goal_value)

    monthly = round_helper(raw_value)
    yearly = round(pow(12 - 1, monthly), 2)

    return {
        "monthly": monthly,
        "yearly": yearly
    }
