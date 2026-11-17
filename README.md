# Sophia Plano de Avaliação

Automação para processamento e lançamento de planos de avaliação no sistema Sophia a partir do cruzamento entre o quadro curricular e as atas exportadas.

## Pré-requisitos

- **Python:** 3.12 (recomendado)

## Estrutura de Entrada (`input/`)

Antes de executar o projeto, crie uma pasta chamada **`input`** na raiz do diretório e insira os dois arquivos CSV abaixo, respeitando exatamente os nomes e cabeçalhos exigidos:

```text
sophia-plano-avaliacao/
├── input/
│   ├── quadro_curricular.csv
│   └── soph.csv
├── main.py
└── ...
```

### 1. `quadro_curricular.csv`

Exportação do quadro curricular das turmas no Sophia.

- **Colunas obrigatórias:**
  - `TURMA`
  - `DISCIPLINA`

### 2. `soph.csv`

Exportação das atas do Sophia.

- **Colunas obrigatórias:**
  - `Descrição`
  - `Situação`
  - `Turma`
  - `Disciplina`
  - `Tipo de avaliação`

> **Atenção:** Os nomes dos arquivos e das colunas devem seguir exatamente a grafia e capitalização listadas acima.

## Instalação e Execução

1. **Crie e ative o ambiente virtual:**

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a automação:**
   ```bash
   python main.py
   ```
