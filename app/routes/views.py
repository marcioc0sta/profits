from app.apis.goals import get_goals
from app.apis.wallet_profitability import real_profitability
from app.models.Goal import Goal
from app.models.Wallet_value import Wallet_values
from fastapi import APIRouter

router = APIRouter()


@router.post("/profitability-goals", tags=["/profitability-goals"])
async def profitability_goals(goal: Goal):
    return {
        "monthly": get_goals(goal)["monthly"],
        "yearly": get_goals(goal)["yearly"],
    }


@router.post("/wallet-profitability", tags=["/wallet-profitability"])
async def wallet_profitability(walletValues: Wallet_values):
    return real_profitability(walletValues)
