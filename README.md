# Instruções para executar o código

Antes de executar o código, realize os procedimentos apresentados nas sessões: **Instalação de bibliotecas e ambiente virtual para execução do código** e **Método de resolução de captcha manual**

### Instalação de bibliotecas e ambiente virtual para execução do código
Para sistemas Linux, sugiro seguir o passo a passo de site para criação de um **virtualev**: https://www.linode.com/docs/guides/create-a-python-virtualenv-on-ubuntu-18-04/.

Para execução em sistemas windows, sugiro a utilização da IDE PyCharm. Pode ser baixado em: https://www.jetbrains.com/pt-br/pycharm/download/?section=windows. Nesse caso, crie um novo projeto com arquivos apresentados nesse repositório.

Com o ambiente virtual criado e ativado, execute o seguinte comando no terminal (serve para ambos os tipos de sistema):

```console
pip install -r requirements.txt
```
### Método de resolução de captcha manual:
Observações: Atualmente, o StackOverflow tem usado mecanismo de proteção **Captcha** para evitar o uso de scripts em sua plataforma. Os scripts desenvolvidos para esse projeto, não tratam esse tipo de ocorrência. Para questão de testes, esse foi resolvido manualmente antes da execução do código com o objetivo de realizar um bypass momentâneo ao mecanismo de proteção.

![image](https://github.com/vininaka/stackoverflow_request/assets/66442324/b6985caf-a5f0-4b53-88fe-71142e6f336a)

* Acesse: https://stackoverflow.com/
* Na barra superior de pesquisa, insira um nome de erro qualquer conforme previsto nos testes sugeridos e aperte para buscar. **Exemplo: ValueError**
* Um Captcha de verificação irá aparecer para ser resolvido
* Resolva o captcha manualmente

 Pronto, agora o código está pronto para ser executado!

# Execução de scripts
* **executor.py**: Arquivo orquestrador responsável por ler um arquivo .py e procurar possíveis soluções no StackOVerflow. Para facilitar as execuções, esse arquivo pede um argumento de entrada(```--script_name```)
* **code.py**: Arquivo com um código padrão. De acordo com as instruções sugeridas, esse script deve conter um erro.
* **fetcher.py**: Arquivo responsável por realizar requisições a página do StackOverflow.

Para execução em sistemas Linux:
```console
python executor.py --script_name code.py
```
Para execução em sistemas Windows. Com a IDE PyCharm, novo projeto criado e o seu interpretador devidamente configurado com as bibliotecas, o seu ambiente esta praticamente pronto para ser executado.

Para a execução do arquivo **executor.py**, insira os argumentos de entrada seguindo os seguintes passos:
![image](https://github.com/vininaka/stackoverflow_request/assets/66442324/270ecf89-ec92-403b-8a9a-9a1086d1b729)
![image](https://github.com/vininaka/stackoverflow_request/assets/66442324/e4511f85-2137-4671-9e8c-a96932de7281)

# Exemplo de execução:
1 - Chamada do executor.py:
![image](https://github.com/vininaka/stackoverflow_request/assets/66442324/36c166c6-2efe-4420-98a9-296ff7ea1a98)

2 - Lista de soluções do StackOverflow:
![image](https://github.com/vininaka/stackoverflow_request/assets/66442324/e3e7359c-fe5e-4200-8716-54f3314cfd73)

3 - Acesso a primeira solução do StackOverflow:
