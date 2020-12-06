

1​. Servidor HTTP que funcionará apenas para requisições GET.

*Observações:*
* Este requisito é um requisito válido?
* Caso seja um requisito válido, o mesmo não é cumprido. Pois, caso seja feita uma requisição do tipo HEAD ou OPTIONS para o server, a mesma é retornada com o status code 200 desrespeitando o requisito 1 e o requisito 7. Seguindo as especificações do protocolo HTTP o valor esperado deveria ser 405 e este é retornado para as requisições do tipo POST, PATCH, PUT e DELETE nos casos de HEAD ou OPTIONS não foi respeitado este padrão.
* O cenário descrito acima não pode ser automatizado, pois a ferramenta utilizada não possui suporte aos métodos HEAD e OPTIONS, porém pode ser facilmente reproduzido utilizando a biblioteca requests no python com o seguinte código:
```
​from requests import head, options
head("http://challengeqa.staging.devmuch.io/7777")
options("http://challengeqa.staging.devmuch.io/7777")
```

2​. Sistema permitirá utilizar apenas números no intervalo entre [-10000, 10000];

*Observações*
* Ao extrapolar os limites de -10000 e 10000, a aplicação se comporta de forma diferente  nos endpoints pensados na internacionalização. No endpoint /en, ao realizar a seguinte requisição o retorno difere do especificado no requisito 6 o status code retornado é 401, quando era esperado 400. Enquanto no endpoint em português este comportamento é respeitado:
```
from requests import get
get("http://challengeqa.staging.devmuch.io/en/10001")
{'_content': b'{"full": "Invalid data"}',
 '_content_consumed': True,
 '_next': None,
 'status_code': 401,
 'headers': {'Content-Type': 'application/json', 'Content-Length': '24', 'Server': 'Werkzeug/1.0.1 Python/3.7.9', 'Date': 'Sat, 05 Dec 2020 17:56:25 GMT'},
 'raw': <urllib3.response.HTTPResponse at 0x7fa89f7388e0>,
 'url': 'http://challengeqa.staging.devmuch.io/en/10001',
 'encoding': None,
 'history': [],
 'reason': 'UNAUTHORIZED',
 'cookies': <RequestsCookieJar[]>,
 'elapsed': datetime.timedelta(microseconds=815335),
 'request': <PreparedRequest [GET]>,
 'connection': <requests.adapters.HTTPAdapter at 0x7fa89f5a2760>}

 get("http://challengeqa.staging.devmuch.io/en/-10001")
 {'_content': b'{"full": "Invalid data"}',
  '_content_consumed': True,
  '_next': None,
  'status_code': 401,
  'headers': {'Content-Type': 'application/json', 'Content-Length': '24', 'Server': 'Werkzeug/1.0.1 Python/3.7.9', 'Date': 'Sat, 05 Dec 2020 17:59:00 GMT'},
  'raw': <urllib3.response.HTTPResponse at 0x7fa89f7a5c40>,
  'url': 'http://challengeqa.staging.devmuch.io/en/-10001',
  'encoding': None,
  'history': [],
  'reason': 'UNAUTHORIZED',
  'cookies': <RequestsCookieJar[]>,
  'elapsed': datetime.timedelta(microseconds=515990),
  'request': <PreparedRequest [GET]>,
  'connection': <requests.adapters.HTTPAdapter at 0x7fa89f7d04c0>}

 get("http://challengeqa.staging.devmuch.io/-10001")
{'_content': b'{"extenso": "Invalid data"}',
 '_content_consumed': True,
 '_next': None,
 'status_code': 400,
 'headers': {'Content-Type': 'application/json', 'Content-Length': '27', 'Server': 'Werkzeug/1.0.1 Python/3.7.9', 'Date': 'Sat, 05 Dec 2020 18:21:16 GMT'},
 'raw': <urllib3.response.HTTPResponse at 0x7fa89f27f160>,
 'url': 'http://challengeqa.staging.devmuch.io/-10001',
 'encoding': None,
 'history': [],
 'reason': 'BAD REQUEST',
 'cookies': <RequestsCookieJar[]>,
 'elapsed': datetime.timedelta(microseconds=476820),
 'request': <PreparedRequest [GET]>,
 'connection': <requests.adapters.HTTPAdapter at 0x7fa89f285c70>}

 get("http://challengeqa.staging.devmuch.io/10001")
{'_content': b'{"extenso": "Invalid data"}',
 '_content_consumed': True,
 '_next': None,
 'status_code': 400,
 'headers': {'Content-Type': 'application/json', 'Content-Length': '27', 'Server': 'Werkzeug/1.0.1 Python/3.7.9', 'Date': 'Sat, 05 Dec 2020 18:21:16 GMT'},
 'raw': <urllib3.response.HTTPResponse at 0x7fa89f27f160>,
 'url': 'http://challengeqa.staging.devmuch.io/-10001',
 'encoding': None,
 'history': [],
 'reason': 'BAD REQUEST',
 'cookies': <RequestsCookieJar[]>,
 'elapsed': datetime.timedelta(microseconds=476820),
 'request': <PreparedRequest [GET]>,
 'connection': <requests.adapters.HTTPAdapter at 0x7fa89f285c70>}


3​. Ao se fazer essa requisição, retornará um JSON cuja chave "extenso" terá, em seu valor, o número inteiro por extenso, que foi inserido na path

*Observações*:
* Ao fazer a seguinte requisição do tipo GET para o endpoint http://challengeqa.staging.devmuch.io/10000 o valor retornado desrespeita a regra de internacionalização(requisito 4), pois o valor retornado na chave "extenso" é o número dez mil escrito em inglês:
```
from requests import get
get("http://challengeqa.staging.devmuch.io/10000")
{'_content': b'{"extenso": "ten thousand"}',
 '_content_consumed': True,
 '_next': None,
 'status_code': 200,
 'headers': {'Content-Type': 'application/json', 'Content-Length': '27', 'Server': 'Werkzeug/1.0.1 Python/3.7.9', 'Date': 'Sat, 05 Dec 2020 17:27:56 GMT'},
 'raw': <urllib3.response.HTTPResponse at 0x7fa89f785790>,
 'url': 'http://challengeqa.staging.devmuch.io/10000',
 'encoding': None,
 'history': [],
 'reason': 'OK',
 'cookies': <RequestsCookieJar[]>,
 'elapsed': datetime.timedelta(microseconds=510777),
 'request': <PreparedRequest [GET]>,
 'connection': <requests.adapters.HTTPAdapter at 0x7fa89f560820>}

* Ao fazer a seguinte requisição do tipo GET para o endpoint http://challengeqa.staging.devmuch.io/en/-10000 o Content-Type retornado não é um json e sim um plain/text desrespeitando o requisito 3:
```
from requests import get
get("http://challengeqa.staging.devmuch.io/en/-10000")
{'_content': b'minus ten thousand',
 '_content_consumed': True,
 '_next': None,
 'status_code': 200,
 'headers': {'Content-Type': 'text/plain; charset=utf-8', 'Content-Length': '18', 'Server': 'Werkzeug/1.0.1 Python/3.7.9', 'Date': 'Sat, 05 Dec 2020 17:41:56 GMT'},
 'raw': <urllib3.response.HTTPResponse at 0x7fa89f47cee0>,
 'url': 'http://challengeqa.staging.devmuch.io/en/-10000',
 'encoding': 'utf-8',
 'history': [],
 'reason': 'OK',
 'cookies': <RequestsCookieJar[]>,
 'elapsed': datetime.timedelta(microseconds=563245),
 'request': <PreparedRequest [GET]>,
 'connection': <requests.adapters.HTTPAdapter at 0x7fa89f782d30>}

* Ao fazer a seguinte requisição do tipo GET para o endpoint http://challengeqa.staging.devmuch.io/en/10000 o json retornado não possui uma chave "extenso" e sim uma chave "full" diferindo da especificada no requisito 3:
```
from requests import get
get("http://challengeqa.staging.devmuch.io/en/10000")
{'_content': b'{"full": "ten thousand"}',
 '_content_consumed': True,
 '_next': None,
 'status_code': 200,
 'headers': {'Content-Type': 'application/json', 'Content-Length': '24', 'Server': 'Werkzeug/1.0.1 Python/3.7.9', 'Date': 'Sat, 05 Dec 2020 17:45:19 GMT'},
 'raw': <urllib3.response.HTTPResponse at 0x7fa89f780be0>,
 'url': 'http://challengeqa.staging.devmuch.io/en/10000',
 'encoding': None,
 'history': [],
 'reason': 'OK',
 'cookies': <RequestsCookieJar[]>,
 'elapsed': datetime.timedelta(microseconds=512535),
 'request': <PreparedRequest [GET]>,
 'connection': <requests.adapters.HTTPAdapter at 0x7fa89f84c490>}


4.Pensando-se na internacionalização deste, o serviço terá suporte, além de português, para tambem em inglês;

*Observações*
* O português suportado é o português de Portugal ou o português do Brasil? Caso seja português do Brasil, em números que contenham os números 16, 17 e 19 terão sua grafia incorreta. Pois estão em sua grafia no português de Portugal, seguem alguns exemplos:
```
from requests import get
get("http://challengeqa.staging.devmuch.io/16")
{'_content': b'{"extenso": "dezasseis"}',
 '_content_consumed': True,
 '_next': None,
 'status_code': 200,
 'headers': {'Content-Type': 'application/json', 'Content-Length': '24', 'Server': 'Werkzeug/1.0.1 Python/3.7.9', 'Date': 'Sat, 05 Dec 2020 18:11:56 GMT'},
 'raw': <urllib3.response.HTTPResponse at 0x7fa89f53b6a0>,
 'url': 'http://challengeqa.staging.devmuch.io/16',
 'encoding': None,
 'history': [],
 'reason': 'OK',
 'cookies': <RequestsCookieJar[]>,
 'elapsed': datetime.timedelta(microseconds=987081),
 'request': <PreparedRequest [GET]>,
 'connection': <requests.adapters.HTTPAdapter at 0x7fa89f2d49a0>}
```
```
get("http://challengeqa.staging.devmuch.io/117")
{'_content': b'{"extenso": "cento e dezassete"}',
 '_content_consumed': True,
 '_next': None,
 'status_code': 200,
 'headers': {'Content-Type': 'application/json', 'Content-Length': '32', 'Server': 'Werkzeug/1.0.1 Python/3.7.9', 'Date': 'Sat, 05 Dec 2020 18:14:09 GMT'},
 'raw': <urllib3.response.HTTPResponse at 0x7fa89f469ee0>,
 'url': 'http://challengeqa.staging.devmuch.io/117',
 'encoding': None,
 'history': [],
 'reason': 'OK',
 'cookies': <RequestsCookieJar[]>,
 'elapsed': datetime.timedelta(microseconds=492254),
 'request': <PreparedRequest [GET]>,
 'connection': <requests.adapters.HTTPAdapter at 0x7fa89f738fd0>}
```
```
get("http://challengeqa.staging.devmuch.io/5119")
{'_content': b'{"extenso": "cinco mil cento e dezanove"}',
 '_content_consumed': True,
 '_next': None,
 'status_code': 200,
 'headers': {'Content-Type': 'application/json', 'Content-Length': '41', 'Server': 'Werkzeug/1.0.1 Python/3.7.9', 'Date': 'Sat, 05 Dec 2020 18:15:05 GMT'},
 'raw': <urllib3.response.HTTPResponse at 0x7fa89f2c2490>,
 'url': 'http://challengeqa.staging.devmuch.io/5119',
 'encoding': None,
 'history': [],
 'reason': 'OK',
 'cookies': <RequestsCookieJar[]>,
 'elapsed': datetime.timedelta(microseconds=489293),
 'request': <PreparedRequest [GET]>,
 'connection': <requests.adapters.HTTPAdapter at 0x7fa89f2c2880>}

5.Caso não seja possível converter o valor inserido na path, chave “extenso” terá valor “Invalid data”;

6.​ Para estes casos, resposta deve ter status 400;

7.​ Para os casos válidos, resposta deve ter status 200.
