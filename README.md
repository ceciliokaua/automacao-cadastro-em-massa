🤖 Automação de Cadastro de Produtos com PyAutoGUI
Este projeto é um script de automação robótica de processos (RPA) que realiza o cadastro automático de uma lista de produtos em um sistema web, utilizando a biblioteca PyAutoGUI para interagir com a interface gráfica e o Pandas para manipulação de dados.

📋 Sobre o Projeto
O objetivo principal é eliminar o trabalho manual de preenchimento de formulários, extraindo dados de um arquivo .csv e inserindo-os automaticamente em campos específicos do navegador.

Principais Funcionalidades:
Leitura de Dados: Carregamento de dados de produtos via arquivo CSV.

Interação com Navegador: Acesso automático ao sistema web.

Preenchimento Inteligente: Digitação automática de código, marca, tipo, categoria, preço unitário, custo e observações.

Navegação Automatizada: Uso de comandos de teclado (Tab, Enter) para transitar entre os campos do formulário.

🛠️ Tecnologias Utilizadas
Python 3.x

PyAutoGUI: Para automação de mouse e teclado.

Pandas: Para leitura e tratamento da base de dados (CSV).

Time: Para gerenciamento de intervalos de segurança entre comandos.

🚀 Como Executar o Projeto
Clone o repositório:

Bash
git clone https://github.com/ceciliokaua/projeto-automacao-com-pyautogui.git
Instale as dependências:

Bash
pip install pyautogui pandas
Configure as coordenadas (opcional):
Caso precise ajustar os cliques do mouse para o seu monitor, utilize o arquivo auxiliar.py para identificar as posições (x, y) atuais.

Rode o script principal:

Bash
python projeto.py
⚠️ Observações de Segurança
O PyAutoGUI assume o controle do mouse e teclado. Caso precise interromper a execução rapidamente, mova o mouse para um dos quatro cantos da tela (recurso FailSafe).

Certifique-se de que a janela do navegador esteja na posição correta antes de iniciar.

📄 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para usar e adaptar!

Desenvolvido por Kauã Cecilio
