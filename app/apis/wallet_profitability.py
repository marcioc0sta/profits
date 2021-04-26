from app.helpers.round import round_helper


def real_profitability(walletValues):
    # TODO: get the inflation rate via bcb forecast
    inflation_rate = 6.1 / 100
    profitability = walletValues.value / walletValues.initial_value - 1
    real_profitability_formula = (1 + profitability) / (1 + inflation_rate) - 1
    return {
        "profitability": round_helper(profitability),
        "real_profitability": round_helper(real_profitability_formula),
    }
