from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def describe_profitability_goals():
    def should_return_monthly_and_yearly_goals_from_api():
        # given
        expected_result = {"monthly": 1.4, "yearly": 28.7}
        # when
        response = client.post(
            "/profitability-goals",
            json={
                "time": 100,
                "montly_contribution": 2500,
                "initial_contribution": 300000,
                "goal_value": 1750000,
            },
        )
        # then
        assert response.status_code == 200
        assert response.json() == expected_result
