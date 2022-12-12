from reverse_string.main import reverse


def test_reverse_string():
    assert reverse('abcd') == 'dcba'


def test_reverse_string_with_blank():
    assert reverse('  abcd') == 'dcba  '


if __name__ == '__main__':
    test_reverse_string()
    test_reverse_string_with_blank()
