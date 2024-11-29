# 66. Escreva uma função bin2dec(binario) que converte um número binário para decimal.
def bin2dec(binario):
    return int(binario, 2)

# Teste para a função bin2dec
def test_bin2dec():
    assert bin2dec("1010") == 10
    assert bin2dec("0") == 0
    assert bin2dec("11111111") == 255
    print("test_bin2dec passou!")