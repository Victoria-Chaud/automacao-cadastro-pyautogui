# 🖥️ Automação de Cadastro com PyAutoGUI e Pandas

Este projeto foi desenvolvido como **prática do curso Python Turbo da Hashtag Treinamentos**.  
O objetivo é automatizar o processo de login e cadastro de produtos em um sistema web, usando **Python + PyAutoGUI** para simular interações de teclado e mouse, e **Pandas** para ler a base de dados.

🔗 Repositório: [Victoria-Chaud/automacao-cadastro-pyautogui](https://github.com/Victoria-Chaud/automacao-cadastro-pyautogui)

---

## 🚀 Tecnologias usadas
- [Python 3](https://www.python.org/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/)
- [Pandas](https://pandas.pydata.org/)

---

## 📂 Estrutura

---

## ⚙️ Como rodar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/Victoria-Chaud/automacao-cadastro-pyautogui.git
   cd automacao-cadastro-pyautogui
   pip install pyautogui pandas
   python codigo.py

---

## 📌 Observações importantes

Os valores de coordenadas (x, y) usados pelo PyAutoGUI podem mudar dependendo do seu monitor.
Para descobrir, use o script auxiliar:

import pyautogui, time
time.sleep(5)
print(pyautogui.position())

O arquivo produtos.csv deve conter as colunas:

codigo, marca, tipo, categoria, preco_unitario, custo, obs

---

✍️ Autor

Projeto prático desenvolvido por Victoria Chaud, como parte do Python Turbo da Hashtag Treinamentos.


---

👉 Agora é só salvar esse `README.md` na sua pasta, dar:  

```powershell
git add README.md
git commit -m "Adiciona README.md com descrição do projeto"
git push
