from morse import decode
import pytest

@pytest.mark.parametrize(
    "source_string,result",
    [
        ('... --- ...', 'SOS'),
        ('..... ....- .-.-.- ---.. --... -.... -.... --... --..-- .---- ..... .-.-.- ....- .----', '54.87667, 15.41'),
        ('.... . .-.. .-.. --- .-- --- .-. .-.. -..', 'HELLOWORLD'),
    ],
)
def test_decoder(source_string, result):
    assert decode(source_string) == result
