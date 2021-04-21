from app.helpers.round import round_helper


def describe_should_round_a_number():
    def with_default_decimal_count():
        # given
        num = 0.1123
        expected_result = 11.23
        # when
        rounded_num = round_helper(num)
        # then
        assert rounded_num == expected_result

    def accordig_with_given_decimal_count():
        # given
        num = 0.1123
        expected_result = 11.2
        # when
        rounded_num = round_helper(num, 1)
        # then
        assert rounded_num == expected_result
