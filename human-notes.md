#### 1​. Servidor HTTP que funcionará apenas para requisições GET.

Considerando o requisito, serão aceitas somente requisições que utilizem o verbo GET.

Utilizando de testes exploratórios, foram realizadas algumas requisições utilizando outros verbos HTTP como por exemplo o verbo HEAD este que se comporta de maneira identica ao método GET de acordo com a [RFC-7231](https://tools.ietf.org/html/rfc7231#section-4.3.2), mas para requisições deste tipo somente os cabeçalhos são retornados. Também foram feitas requisições utilizando o verbo OPTIONS, em ambos os casos o status de retorno foi 200, conforme definido no requisito 7 para casos válidos.

Embora os cenários supracitados tenham um comportamento esperado no protocolo utilizado, o requisito diz que apenas o verbo GET deve ser aceito, logo o mesmo não é cumprido.

Também outros testes realizados utilizando os verbos PATCH, PUT, POST e DELETE. O status retornado nestes casos estão respeitando as especificações do HTTP onde está retornando 405 informando que não é um método permitido.

#### 2​. Sistema permitirá utilizar apenas números no intervalo entre [-10000, 10000]
Definindo os valores limites aceitos pela aplicação sendo qualquer número inteiro entre -10000 e 10000, os primeiros testes foram com os números de 1 à 20, pois são números que possuem uma grafia única e não são compostos a partir da união da grafia de outros números, como por exemplo 55, que é composto pela união dos números 50 e 5.

Também foram extrapolados os valores limites definidos neste requisito, a aplicação na versão em inglês ao realizar uma requisição de um número que extrapole os limites estabelecidos, é desrespeitado o requisito 6, onde deveria ser retornado o status 400 mas na realidade está sendo retornado 401.

Considerando o número 0 como fronteira entre os números posítivos e negativos realizei testes com os números 1 e -1, a aplicação se comportou conforme esperado de acordo com os requisitos.

#### 3​. Ao se fazer essa requisição, retornará um JSON cuja chave "extenso" terá, em seu valor, o número inteiro por extenso, que foi inserido na path

Considerando que todo o tipo do conteúdo da requisição deverá ser JSON e este JSON deverá conter a chave "extenso". # 1

Durante os testes exploratórios este requisito não é cumprido na versão em inglês da aplicação, pois não é retornado um JSON com a chave "extenso" e sim a chave "full". Ainda na versão em inglês, ao realizar um requisição para o limite negativo (-10000), o conteúdo retornado não é um JSON e sim text/plain.

#### 4.Pensando-se na internacionalização deste, o serviço terá suporte, além de português, para tambem em inglês;

Quanto ao português suportado é o português de Portugal ou o português do Brasil?

Caso seja português do Brasil, em testes exploratórios foi encontrado que números terminados em 16, 17 e 19 terão sua grafia incorreta. Pois estão em sua grafia no português de Portugal.

Na versão em português da aplicação ao se fazer uma requisição para o valor positivo do limite definido no requisito 2 (10000), a chave "extenso" possuí o conteúdo do número enviado com sua grafia em inglês, desrespeitando as regras de internacionalização definidas no requisito 4.

Sugestão para a implementação de internacionalização, seria a utilização do header [Accept-Language](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language) onde o cliente informa quais os idiomas que ele é capaz de compreender e qual é o idioma preferencial. Com isso elimina-se a necessidade de criação de um novo endpoint para cada novo idioma suportado pelo serviço.

#### 5.Caso não seja possível converter o valor inserido na path, chave “extenso” terá valor “Invalid data”;

#### 6.​ Para estes casos, resposta deve ter status 400;
De maneira exploratória foi constatado que na versão em português da aplicação, caso seja enviado um valor inválido (qualquer valor que não seja um número inteiro), o status recebido é 401 assim desrespeitando o requisito 6.

Constatado que na versão em inglês da aplicação, caso seja enviado um valor que extrapole os limites estabelecidos no requisito 2(-10000 a 10000), o status retornado está sendo 401 assim desrespeitando o requisito 6.

#### 7.​ Para os casos válidos, resposta deve ter status 200.


#### Observações adicionais
Ao verificar o header Server retornado pela aplicação, são encontradas informações referentes ao Werkzeug o servidor de desenvolvimento interno do framework Flask. Esta não é a maneira adequada para a disponibilização de uma aplicação Flask em produção.

 Inclusive podendo gerar algumas falhas de segurança, como por exemplo, se tentarmos acessar ao endpoint */console* é liberado o acesso ao usuário e caso o mesmo tenha o PIN solicitado o usuário poderá utilizar o console do Werkzeug em um ambiente de produção caso o modo de debug esteja habilitado.

O cenário descrito acima está acontecendo atualmente.
