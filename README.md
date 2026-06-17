# CLI de Análise de Logs

Ferramenta de linha de comando para análise, filtragem e enriquecimento de ficheiros de log (Apache, Nginx ou logs personalizados). Processa logs linha por linha, identifica níveis de severidade, agrupa eventos por hora, consulta uma API pública de geolocalização de IP e exporta um resumo estatístico em CSV.

## Funcionalidades

- Leitura de logs nos formatos Apache, Nginx e logs personalizados (ex.: ESP32)
- Filtragem por nível de severidade (`ERROR`, `WARN`, `INFO`, `DEBUG`)
- Extração e agrupamento de eventos por hora
- Deteção de endereços IP e enriquecimento com dados de geolocalização (país, cidade, ISP, região)
- Geração de resumo estatístico (total de logs, erros, warnings, frequência por hora)
- Exportação do relatório em formato CSV
- Exibição de resumo no terminal
- Tratamento de erros (ficheiro não encontrado, API indisponível, formato inválido)
- Processamento de grandes volumes de logs

## Requisitos

- Python 3.8+
- Conexão com internet (para consulta à API de geolocalização)

## Instalação

```bash
git clone https://github.com/user/log-analyzer.git
cd log-analyzer
pip install -r requirements.txt  # se aplicável
```

## Uso

```bash
python main.py --file logs.txt --level ERROR --output resultado.csv
```

### Argumentos

| Argumento | Descrição |
|-----------|-----------|
| `--file` | Caminho do ficheiro de log a analisar (obrigatório) |
| `--level` | Filtrar por nível de severidade (`ERROR`, `WARN`, `INFO`, `DEBUG`) |
| `--output` | Nome do ficheiro CSV de saída (opcional) |

### Exemplo de saída (terminal)

```
=== RESUMO DA ANÁLISE ===
Total de logs processados: 1500
Total de ERROR: 45
Total de WARN: 120
Frequência por hora:
  10:00 - 15 ocorrências
  11:00 - 8 ocorrências
```

### Exemplo de CSV gerado

```csv
hora,tipo,total,pais,cidade
10:00,ERROR,5,Angola,Luanda
10:00,WARN,3,Brasil,São Paulo
```

## Estrutura do projeto

```
log-analyzer/
├── main.py              # Ponto de entrada com argparse
├── log_parser.py        # Leitura e parsing de logs
├── geo_enricher.py      # Consulta à API de geolocalização
├── aggregator.py        # Agregação e estatísticas
├── exporter.py          # Exportação CSV
├── requirements.txt     # Dependências
└── README.md
```

## Requisitos Funcionais (RF)

| ID | Descrição |
|----|-----------|
| RF01 | Ler ficheiros de log em formatos compatíveis |
| RF02 | Validar existência do ficheiro antes do processamento |
| RF03 | Analisar cada linha do ficheiro para extrair informações |
| RF04 | Reconhecer níveis de severidade (ERROR, WARN, INFO, DEBUG) |
| RF05 | Filtrar logs por nível via linha de comando |
| RF06 | Extrair timestamp de cada entrada do log |
| RF07 | Agrupar eventos de log por hora |
| RF08 | Contar ocorrências por nível de log |
| RF09 | Detetar endereços IP nas entradas do log |
| RF10 | Consultar API pública de geolocalização de IP |
| RF11 | Adicionar dados de geolocalização aos logs processados |
| RF12 | Gerar resumo estatístico (totais e frequência por hora) |
| RF13 | Exportar relatório em formato CSV |
| RF14 | Aceitar parâmetros via CLI com argparse |
| RF15 | Permitir escolha do nome/local do ficheiro CSV |
| RF16 | Exibir resumo da análise no terminal |
| RF17 | Tratar erros (ficheiro, API, formato inválido) |
| RF18 | Manter histórico com Git |
| RF19 | Processar grandes volumes sem falhar |
| RF20 | Finalizar corretamente após gerar o relatório |

## Licença

MIT
