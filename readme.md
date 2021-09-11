<h1>Ac 03 de arquitetura</h1>
<br>
<h2>ra: 1903593</h2>
<br>
<h3>Padrões de projetos usados</h3>
<ul> 
<li>Strategy</li>
<li>Factory</li>
</ul>
<br>
<h3>Módulos</h3>
<ul> 
<li>calculadora.py</li>
<li>fabricaDeOperacaoes.py</li>
<li>operacoes.py</li>
<li>teste.py</li>
</ul>
<br>
<h4>operacoes.py</h4>
<p>Módulo onde esta contido todas as operações matemáticas da calculadora, que herdam de uma classe
abstrada chamada "Operacao" existente neste mesmo módulo</p>
<br>
<h4>fabricaDeOperacaoes.py</h4>
<p>Módulo responsável por criar objetos de operacoes do módulo "operacoes.py", e retornar esses objetos para o modulo calculadora.py</p>
<br>
<h4>calculadora.py</h4>
<p>Módulo responsável por entrar em contato com o módulo "fabricaDeOperacaoes.py" e gerar um objeto de uma determinada operação, juntamente
com dois valores para que sejam usados nesta operação. Caso a operação sejá inválida, será retornado que a operação foi inválida.</p>
<br>
<h4>teste.py</h4>
<p>Módulo responsável por fazer a execução dos testes para cada operação existente na calculadora.</p>