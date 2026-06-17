# CLI de Análise de Logs

Ferramenta de linha de comando para análise, filtragem e enriquecimento de ficheiros de log Apache e Nginx (access log e error log). Processa logs linha por linha, identifica níveis de severidade, agrupa eventos por hora, consulta uma API pública de geolocalização de IP e exporta os dados enriquecidos em CSV.

## Funcionalidades

- Leitura de logs nos formatos Apache e Nginx (access log e error log)
- Filtragem por nível de severidade (`ERROR`, `WARN`, `INFO`, `DEBUG`)
- Extração e agrupamento de eventos por hora
- Deteção de endereços IP e enriquecimento com dados de geolocalização (país, cidade)
- Geração de resumo estatístico (total de logs, erros, warnings, frequência por hora)
- Exportação dos dados enriquecidos em CSV
- Exibição de resumo no terminal

## Requisitos

- Python 3.8+
- Conexão com internet (para consulta à API de geolocalização)

## Uso

### Análise básica (apenas terminal)

```bash
python main.py --file logs/apache_access_1.log
```

### Análise com exportação CSV

```bash
python main.py --file logs/apache_access_1.log --output reports/resultado.csv
```

### Filtrar por nível de severidade

```bash
# Apenas erros
python main.py --file logs/apache_access_1.log --level ERROR

# Apenas warnings
python main.py --file logs/apache_access_1.log --level WARN

# Apenas info
python main.py --file logs/apache_access_1.log --level INFO

# Com filtro e exportação
python main.py --file logs/apache_access_1.log --level ERROR --output reports/erros.csv
```

### Analisar diferentes formatos de log

```bash
# Apache access log
python main.py --file logs/apache_access_1.log --output reports/apache.csv

# Apache error log
python main.py --file logs/apache_error_1.log --output reports/apache_erros.csv

# Nginx access log
python main.py --file logs/nginx_access_1.log --output reports/nginx.csv

# Nginx error log
python main.py --file logs/nginx_error_1.log --output reports/nginx_erros.csv
```

### Argumentos

| Argumento | Descrição |
|-----------|-----------|
| `--file` | Caminho do ficheiro de log (obrigatório) |
| `--level` | Filtrar por nível (`ERROR`, `WARN`, `INFO`, `DEBUG`) |
| `--output` | Caminho do ficheiro CSV de saída (opcional) |

### Exemplo de saída no terminal

```
=== RESUMO DA ANALISE ===
Total de logs processados: 20
Total de ERROR: 3
Total de WARN: 4
Frequencia por hora:
  10:00 - INFO: 8, WARN: 3, ERROR: 1
  11:00 - INFO: 5, ERROR: 2, WARN: 1
```

### Exemplo de CSV gerado

```csv
hora,tipo,total,pais,cidade
10:00,INFO,8,Desconhecido,Desconhecido
10:00,WARN,3,Desconhecido,Desconhecido
10:00,ERROR,1,Desconhecido,Desconhecido
11:00,INFO,5,Desconhecido,Desconhecido
11:00,ERROR,2,Desconhecido,Desconhecido
11:00,WARN,1,Desconhecido,Desconhecido
```

## Estrutura do projeto

```
log-analyzer/
├── main.py              # Ponto de entrada com argparse
├── detector.py          # Deteção do formato do log
├── parser.py           # Parsing de logs Apache e Nginx
├── aggregator.py        # Agregação e estatísticas
├── geo_enricher.py      # Consulta à API de geolocalização
├── exporter.py          # Exportação CSV
└── README.md
```
