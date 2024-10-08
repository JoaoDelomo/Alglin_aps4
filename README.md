
# APS 4

## Projeto de Projeção 3D

Este projeto implementa uma projeção 3D de um cubo e de um prisma utilizando a biblioteca Pygame para desenhar as formas na tela, permitindo que o cubo ou o prisma rotacionem.

### Autor
João Gabriel Delomo

## Instruções para Baixar e Instalar

### 1. Clonar o repositório:
Execute o seguinte comando no terminal para clonar o repositório:

```bash
git clone <https://github.com/JoaoDelomo/Alglin_aps4>
```

### 2. Entrar no diretório do projeto:
```bash
cd APS_4
```

### 3. Criar e ativar o ambiente virtual (opcional, mas recomendado):
No terminal, crie e ative um ambiente virtual com os comandos abaixo:

```bash
# Para criar o ambiente virtual
python -m venv venv

# Para ativar o ambiente no Linux/macOS
source venv/bin/activate

# Para ativar o ambiente no Windows
venv\Scripts\activate
```

### 4. Instalar as dependências:
Após ativar o ambiente virtual, execute o seguinte comando para instalar as dependências do projeto:

```bash
pip install .
```

### 5. Executar o projeto:
Após a instalação, você pode rodar o projeto com o seguinte comando:

```bash
aps_4
```

Ou, se preferir, execute o arquivo `main.py` diretamente:

```bash
python -m aps_4.main
```

Isso irá iniciar o projeto.

## Manipulação das Figuras

Após iniciar o projeto, você pode manipular as figuras (cubo e prisma) e interagir com a simulação utilizando as teclas abaixo:

- **Tecla `C`**: Seleciona o cubo como a figura exibida na tela.
- **Tecla `P`**: Seleciona o prisma como a figura exibida na tela.
- **Tecla `L`**: Ativa ou desativa o feixe de luz que passa pelo prisma. Quando ativado, o feixe gera um arco-íris saindo do prisma.
- **Teclas de setas (`↑`, `↓`, `←`, `→`)**: Controlam a rotação da figura selecionada.
- **Tecla `W`**: Aproxima a câmera da figura, trazendo-a para mais perto.
- **Tecla `S`**: Afasta a câmera da figura, afastando-a da tela.

### Descrição do Feixe de Luz:
Quando o prisma está selecionado e o feixe de luz é ativado, um feixe branco entra pelo meio de uma das faces do prisma, e um arco-íris sai pelo meio da face oposta, simulando a dispersão da luz.

