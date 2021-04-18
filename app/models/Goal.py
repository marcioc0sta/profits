from pydantic import BaseModel


class Goal(BaseModel):
    time: int
    montly_contribution: int
    initial_contribution: int
    goal_value: int
