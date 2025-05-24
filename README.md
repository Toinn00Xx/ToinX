# ToinX AttxK

**Ferramenta hacker visual e modular para Proot Debian (Termux).**  
Interface interativa com **`python3 + curses`**, design animado, splash screen, feedback visual, e suporte para adicionar/remover ferramentas via `tools.json`.

---

## Preview

By: Toinn00Xx | ToinX AttxK

---

## Recursos

- Splash screen animado
- Menu interativo com `curses`
- Tela de confirmação antes de cada ataque
- Feedback ao finalizar ou erro
- Modular: adicione ferramentas no `tools.json`

---

## Instalação no Termux com Proot Debian

```bash
pkg install proot-distro
proot-distro install debian
proot-distro login debian

No Debian:

apt update && apt install git python3 -y
git clone https://github.com/Toinn00Xx/ToinX.git
cd ToinX
python3 toinx_attack.py


---

Como adicionar ferramentas

Edite o arquivo tools.json:

{
  "BruteGram": "python3 brutegram/brutegram.py",
  "Wi-Fi Hack": "sudo wifite",
  "Hack Câmeras": "python3 camhack/camhack.py",
  "Nova Ferramenta": "comando_da_ferramenta"
}


---

Créditos

Desenvolvido por Toinn00Xx
GitHub: github.com/Toinn00Xx


---

⚠️ Uso somente educacional. O autor não se responsabiliza por mau uso.
