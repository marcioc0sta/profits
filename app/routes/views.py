from fastapi import APIRouter

from models.Goal import Goal
from apis.goals import Get_Goals

router = APIRouter()


@router.post('/profitability-goals', tags=['/profitability-goals'])
async def profitability_goals(goal: Goal):
    return {
        "Monthly goal": Get_Goals(goal)['monthly'],
        "Anual goal": Get_Goals(goal)['yearly']
    }
