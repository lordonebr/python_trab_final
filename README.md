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
  http://localhost:8000/
```    
  
  * Cadastrar despesa:
```
  http://localhost:8000/despesa/
```    

  * Editar despesa de id = id_despesa:
```
  http://localhost:8000/despesa/{id_despesa}/
```   

  * Cadastrar receita:
```
  http://localhost:8000/receita/
```    

  * Editar receita de id = id_receita:
```
  http://localhost:8000/receita/{id_receita}/
```   

  * Tela relatório: contas a pagar
```
  http://localhost:8000/relatorio/despesas
```  

  * Tela relatório: contas a receber
```
  http://localhost:8000/relatorio/receitas
```  
