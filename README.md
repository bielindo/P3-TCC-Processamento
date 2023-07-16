# P3 - Projeto TCC (Sistema de monitoramento e rastreamento de objetos indoor) - Processamento de Dados

Este é o terceiro e último repositório do projeto de Trabalho de Conclusão de Curso (TCC) sobre localização indoor, intitulado "Processamento de Dados com Python". O objetivo deste projeto é demonstrar a aplicação de técnicas de processamento e análise de dados utilizando a linguagem de programação Python.

## Descrição

O projeto é composto por diversas funcionalidades que permitem a coleta, processamento e análise de dados provenientes de dispositivos com tecnologia de beacon. As principais funcionalidades do projeto são:

1. **Coleta de Dados:** Utilizando a biblioteca de conexão MQTT, o projeto é capaz de coletar dados emitidos por dispositivos beacon em um ambiente.

2. **Agrupamento de Dados:** Os dados coletados são agrupados e organizados em listas de acordo com o dispositivo de origem.

3. **Análise e Processamento de Dados:** A partir dos dados agrupados, são aplicadas técnicas de análise e processamento para identificar dispositivos comuns e remover valores discrepantes.

4. **Estimação de Coordenadas:** Utilizando técnicas matemáticas, o projeto é capaz de estimar as coordenadas tridimensionais de dispositivos com base nas distâncias medidas em relação a pontos de referência conhecidos.

5. **Interface Gráfica:** Uma interface gráfica é disponibilizada para visualização e análise dos resultados obtidos.

## Requisitos

Para executar o projeto, você precisa ter instalado os seguintes componentes:

- Python 3.x
- Bibliotecas Python: numpy, matplotlib

## Como Executar o Projeto

1. Clone este repositório em sua máquina local:

    git clone [https://github.com/seu-usuario/tcc-processamento.git](https://github.com/bielindo/tcc-processamento.git)

2. Instale as bibliotecas necessárias utilizando o pip:

    pip install numpy matplotlib

3. Navegue até o diretório do projeto:

    cd tcc-processamento

4. Execute o arquivo `main.py` para iniciar o programa:

    python main.py


A interface gráfica será aberta, e você poderá interagir com as diferentes funcionalidades do projeto.

## Contribuição

Se você quiser contribuir com o projeto, sinta-se à vontade para fazer um fork do repositório, criar uma branch com suas modificações e enviar um pull request. Todas as contribuições são bem-vindas!

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.

