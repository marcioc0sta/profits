from app.apis.goals import get_goals


def describe_get_goals():
    def should_return_monthly_and_yearly_goals(goal):
        # given
        expected_result = {"monthly": 1.11, "yearly": 14.32}
        # when
        goals = get_goals(goal)
        # then
        assert goals == expected_result
