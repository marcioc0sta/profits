from fastapi import APIRouter

from models.Goal import Goal
from apis.goals import get_goals

router = APIRouter()


@router.post('/profitability-goals', tags=['/profitability-goals'])
async def profitability_goals(goal: Goal):
    return {
        "Monthly goal": get_goals(goal)['monthly'],
        "Anual goal": get_goals(goal)['yearly']
    }
