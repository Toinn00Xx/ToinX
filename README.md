# ToinX AttxK - Hacker Suite (Termux/Debian)

## Descrição
Ferramenta hacker estilo suite para Termux com Proot Debian, usando interface ncurses em Python. Possui splash animado, menu colorido, confirmação antes de rodar cada ferramenta, feedback de execução e gerenciamento de ferramentas via arquivo JSON.

## Funcionalidades
- Splash screen animado com ASCII art e cores
- Menu colorido com navegação por setas
- Confirmação antes de rodar qualquer ferramenta
- Feedback visual de sucesso, erro ou cancelamento
- Arquivo `tools.json` para adicionar, remover ou modificar comandos facilmente

## Requisitos
- Termux com Proot Debian instalado
- Python 3 instalado (`apt install python3`)
- Ferramentas externas configuradas no `tools.json`

## Instalação e uso
1. Clone o repositório:
```bash
git clone https://github.com/seuusuario/ToinX.git
cd ToinX
