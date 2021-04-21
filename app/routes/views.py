from app.apis.goals import get_goals
from app.models.Goal import Goal
from fastapi import APIRouter

router = APIRouter()


@router.post("/profitability-goals", tags=["/profitability-goals"])
async def profitability_goals(goal: Goal):
    return {
        "monthly": get_goals(goal)["monthly"],
        "yearly": get_goals(goal)["yearly"],
    }
