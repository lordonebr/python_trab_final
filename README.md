# python_trab_final

POS graduação

Curso: Desenvolvimento Web Full Stack

Disciplina: Frameworks back end: Python

Professor: Matheus Alcântara Souza

Trabalho final de Python: sistema de finanças pessoais

Aluno: André Guilherme de Almeida Santos

### URL do site publicado (obs: o heroku pode limpar o banco de dados de tempos em tempos automaticamente):
https://python-trab-final.herokuapp.com/
  

### Comandos básicos

- COMANDO para instalar dependências:
```
  pip install -r requirements.txt
```  

- COMANDO para criar a migração
```
  python manage.py makemigrations people
```  

- COMANDO para executar a migração:
```
  python manage.py migrate people
```  

- COMANDO para subir o servidor na porta 8000:
```
  python manage.py runserver
```  
  
  
### Imagens do projeto
- Tela principal sem receitas e despesas cadastradas
![alt text](https://github.com/lordonebr/python_trab_final/blob/master/img/TelaFluxoCaixa01.png?raw=true)

- Tela principal mostrando fluxo dos meses de forma agrupada
![alt text](https://github.com/lordonebr/python_trab_final/blob/master/img/TelaFluxoCaixa02.png?raw=true)

- Tela principal mostrando fluxo de um mês
![alt text](https://github.com/lordonebr/python_trab_final/blob/master/img/TelaFluxoCaixa03.png?raw=true)

- Tela cadastrar nova despesa
![alt text](https://github.com/lordonebr/python_trab_final/blob/master/img/TelaNovaDespesa.png?raw=true)

- Tela editar uma despesa
![alt text](https://github.com/lordonebr/python_trab_final/blob/master/img/TelaEditarDespesa.png?raw=true)

- Tela cadastrar nova receita
![alt text](https://github.com/lordonebr/python_trab_final/blob/master/img/TelaNovaReceita.png?raw=true)

- Tela editar uma receita
![alt text](https://github.com/lordonebr/python_trab_final/blob/master/img/TelaEditarReceita.png?raw=true)

- Tela do relatório de contas a pagar
![alt text](https://github.com/lordonebr/python_trab_final/blob/master/img/TelaRelatorioPagar.png?raw=true)

- Tela do relatório de contas a receber
![alt text](https://github.com/lordonebr/python_trab_final/blob/master/img/TelaRelatorioReceber.png?raw=true)
  

### Páginas
* Página inicial:
```
  ...
  EX: http://localhost:8000/
```    
  
  * Cadastrar despesa:
```
  .../despesa/
```    

  * Editar despesa de id = id_despesa:
```
  .../despesa/{id_despesa}/
```   

  * Cadastrar receita:
```
  .../receita/
```    

  * Editar receita de id = id_receita:
```
  .../receita/{id_receita}/
```   

  * Tela relatório: contas a pagar
```
  .../relatorio/despesas
```  

  * Tela relatório: contas a receber
```
  .../relatorio/receitas
```  

### Rotas
* Rota para obter a página principal:
```
  GET ...
```    

* Rota para setar um novo valor de saldo inicial no banco de dados:
```
  POST ...
```    

* Rota para abrir a tela de criar despesa:
```
  GET .../despesa/
```    

* Rota para criar uma nova despesa no banco de dados:
```
  POST .../despesa/
```    

* Rota para abrir a tela de editar uma despesa de um id:
```
  GET .../despesa/<int:id_despesa>
```    

* Rota para editar uma despesa de um id no banco de dados:
```
  POST .../despesa/<int:id_despesa>
```   

* Rota para deletar uma despesa de um id do banco de dados:
```
  DELETE .../despesa/<int:id_despesa>
```  

* Rota para abrir a tela de criar receita:
```
  GET .../receita/
```    

* Rota para criar uma nova receita no banco de dados:
```
  POST .../receita/
```    

* Rota para abrir a tela de editar uma receita de um id:
```
  GET .../receita/<int:id_receita>
```    

* Rota para editar uma receita de um id no banco de dados:
```
  POST .../receita/<int:id_receita>
```   

* Rota para deletar uma receita de um id do banco de dados:
```
  DELETE .../receita/<int:id_receita>
```  

* Rota para abrir a tela do relatorio de contas a pagar:
```
  GET .../relatorio/despesas
```  

* Rota para filtrar o relatorio de contas a pagar por uma data de vencimento, retorna uma página:
```
  POST .../relatorio/despesas/filtro
```  

* Rota para abrir a tela do relatorio de contas a receber:
```
  GET .../relatorio/receitas
```  

* Rota para filtrar o relatorio de contas a receber por uma data de expectativa, retorna uma página:
```
  POST .../relatorio/receitas/filtro
```  
