from app.helpers.round import round_helper


def describe_round_helper():
    def should_return_a_rounded_number_with_default_decimal_count(num_to_round):
        # given
        expected_result = 11.23
        # when
        rounded_num = round_helper(num_to_round)
        # then
        assert rounded_num == expected_result

    def should_return_a_rounded_number_accordig_with_given_decimal_count(num_to_round):
        # given
        expected_result = 11.2
        # when
        rounded_num = round_helper(num_to_round, 1)
        # then
        assert rounded_num == expected_result
