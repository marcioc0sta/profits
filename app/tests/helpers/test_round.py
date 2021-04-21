from app.helpers.round import round_helper


def describe_round_helper():
    def return_a_rounded_num_with_default_decimal_count(num_to_round):
        # given
        expected_result = 11.23
        # when
        rounded_num = round_helper(num_to_round)
        # then
        assert rounded_num == expected_result

    def return_a_rounded_num_accordig_with_given_decimal_count(num_to_round):
        # given
        expected_result = 11.2
        # when
        rounded_num = round_helper(num_to_round, 1)
        # then
        assert rounded_num == expected_result
