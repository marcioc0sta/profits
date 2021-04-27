from app.helpers.round import round_helper


def real_profitability(walletValues):
    # TODO: get the inflation rate via bcb forecast
    # https://www.bcb.gov.br/api/servico/sitebcb/indicadorinflacao
    # https://servicodados.ibge.gov.br/api/v3/agregados/6691/periodos/-6/variaveis/63?localidades=N1[all]
    inflation_rate = 0.93 / 100
    profitability = walletValues.value / walletValues.initial_value - 1
    real_profitability_formula = (1 + profitability) / (1 + inflation_rate) - 1
    return {
        "profitability": round_helper(profitability),
        "real_profitability": round_helper(real_profitability_formula),
        "inflation_rate": inflation_rate * 100,
    }
