# 👤 Reconhecimento Facial em Tempo Real com Python

Este projeto implementa um sistema de **reconhecimento facial em tempo real** utilizando a webcam, comparando rostos capturados com imagens previamente cadastradas.

A aplicação utiliza a biblioteca **face_recognition**, baseada em **dlib**, junto com **OpenCV**, para detectar e reconhecer faces de forma simples e eficiente.

---

## 🎯 Funcionalidades

- Detecção de rostos em tempo real pela webcam
- Reconhecimento facial baseado em imagens cadastradas
- Exibição do nome da pessoa reconhecida
- Suporte a múltiplos rostos simultaneamente
- Encerramento seguro do programa ao pressionar **ESC**

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- OpenCV
- face_recognition
- dlib
- NumPy

---

## 📁 Estrutura do Projeto

```text
facial_recognition_project/
│
├── pessoas/              # Imagens das pessoas cadastradas
│   ├── elon.jpg
│   ├── obama.png
│   └── dilma.jpeg
│
├── main.py               # Código principal
├── requirements.txt      # Dependências do projeto
└── README.md
```
---

## ⚙️ Instalação

### 1️⃣ Clonar o repositório
```bash
git clone [https://github.com/seu-usuario/facial_recognition_project.git](https://github.com/seu-usuario/facial_recognition_project.git)
cd facial_recognition_project
```

### 2️⃣ Criar e activar um ambiente virtual
```bash
# Criar o ambiente virtual
python3 -m venv venv

# Activar no Linux/macOS
source venv/bin/activate

# Activar no Windows
# venv\Scripts\activate
```

### 3️⃣ Instalar as dependências do sistema (Linux)

[!IMPORTANT]
A biblioteca dlib exige compiladores C++ instalados no sistema para funcionar correctamente.
```bash
sudo apt update
sudo apt install -y \
  cmake \
  build-essential \
  libopenblas-dev \
  liblapack-dev \
  libx11-dev \
  libgtk-3-dev
```

### 4️⃣ Instalar as dependências Python
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
---

## ▶️ Como Executar

-Preparar os dados: Adicione imagens na pasta pessoas/.

⚠️ Atenção: Utilize apenas 1 rosto por imagem.

Formatos aceites: .jpg, .png, .jpeg.

Iniciar a aplicação:
```bash
python main.py
```

-Controles:

A webcam será iniciada automaticamente.

Pressione a tecla ESC para encerrar o programa.

---

## 🧠 Como Funciona o Face Recognition

O projecto utiliza um pipeline de visão computacional dividido em quatro etapas:

🔹 1. Detecção Facial

Localiza as coordenadas (bounding boxes) onde existem rostos na imagem.
```bash
import face_recognition
# Detecta a localização das faces
face_locations = face_recognition.face_locations(imagem)
```

🔹 2. Extração de Características (Encodings)

Transforma o rosto num vetor matemático de $128$ dimensões.

Gera os encodings para a primeira face detectada
```bash
face_encoding = face_recognition.face_encodings(imagem)[0]
```

Este vetor representa características únicas como a distância entre olhos e contornos faciais.

🔹 3. Comparação de Rostos

Calcula a distância euclidiana entre os vetores. Se a distância for menor que um limiar pré-definido (geralmente $0.6$), a identidade é confirmada.

🔹 4. Resultado

Match encontrado: Exibe o nome do ficheiro da imagem original.

Sem correspondência: O rosto é rotulado como "Desconhecido".

---

### ⚠️ Limitações

Não é indicado para ambientes de alta segurança (pode ser contornado com fotografias).

Sensibilidade a iluminação extrema ou ângulos de rosto muito acentuados.

Possibilidade de falsos positivos em cenários de elevada complexidade visual.

---

## 🚀 Próximos Passos

[ ] Exibir o nível de confiança (probabilidade) na interface.

[ ] Registar logs de reconhecimento numa base de dados (SQLite/PostgreSQL).

[ ] Criar uma interface web ou API REST com FastAPI.

[ ] Dockerizar a aplicação para facilitar a implementação.

[ ] Implementar detecção de vivacidade (liveness detection).

---

## 📄 Licença

Este projecto é de carácter educacional e experimental. Sinta-se à vontade para estudar, modificar e evoluir o código.

## 👨‍💻 Autor

Silas Manoel Graduando em Sistemas de Informação – UFPE
