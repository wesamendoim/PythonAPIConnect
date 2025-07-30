import ConnAPIBancoCentral

def test_retorno_Json():
    resultado = ConnAPIBancoCentral.retorno_Json()
    assert isinstance(resultado, dict) 
    assert 'resultados' in resultado or len(resultado) > 0
