import ConnAPIBancoCentral

def test_retorno_Json():
    resultado = ConnAPIBancoCentral.retorno_Json()
    assert isinstance(resultado, dict)  # Verifica se o retorno � um dicion�rio
    assert 'resultados' in resultado or len(resultado) > 0  # Verifica se h� dados
