# lab_feature_store
 Feature Store Construction and Attribute Engineering in the Machine Learning Pipeline

# Instruções
Construção de Feature Store e Engenharia de Atributos no Pipeline de Machine Learning

Execute os comandos abaixo no terminal ou prompt de comando.

Cria um ambiente virtual

`python3 -m venv featvenv`


Ativa o ambiente virtual criado

`source featvenv/bin/activate`


Instala todas as dependências listadas no arquivo requirements.txt no ambiente virtual

`pip install -r requirements.txt`


Associa o ambiente virtual ao código fonte do nosso pipeline
Quando você executa pip install -e . em um diretório que contém um arquivo setup.py ou pyproject.toml, o pip instala o pacote definido nesse diretório. A instalação no modo editável cria apenas uma ligação entre o seu ambiente de desenvolvimento (por exemplo, o ambiente virtual) e o diretório do código-fonte. 
Isso significa que quaisquer alterações feitas no código-fonte serão refletidas imediatamente no ambiente onde o pacote está instalado, sem a necessidade de reinstalação.

`pip install -e .`


Reativa o ambiente virtual (útil se você tiver desativado anteriormente na mesma sessão)

`source featvenv/bin/activate`


Executa o script Python localizado em src/feature_store.py dentro do ambiente virtual

`python src/feature_store.py`


Desativa o ambiente virtual, retornando ao ambiente global do sistema

`deactivate`



## Telas

![Screenshot1](/images/grafico1.png)

![Screenshot2](/images/grafico2.png)

![Screenshot3](/images/final.png)