import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

def carregar_json(nome_arquivo):
caminho = DATA_DIR / nome_arquivo

```
with open(caminho, "r", encoding="utf-8") as arquivo:
    return json.load(arquivo)
```

def carregar_csv(nome_arquivo):
caminho = DATA_DIR / nome_arquivo

```
with open(caminho, "r", encoding="utf-8") as arquivo:
    return list(csv.DictReader(arquivo))
```

perfil = carregar_json("perfil_usuario.json")
produtos = carregar_json("produtos_financeiros.json")
transacoes = carregar_csv("transacoes.csv")
historico = carregar_csv("historico_atendimento.csv")

print("=== TESTE DA BASE DE CONHECIMENTO ===")

print(f"\nUsuário: {perfil['nome']}")
print(f"Renda mensal: R$ {perfil['renda_mensal']:.2f}")

print(f"\nTransações carregadas: {len(transacoes)}")
print(f"Produtos financeiros carregados: {len(produtos)}")
print(f"Atendimentos carregados: {len(historico)}")

total_entradas = sum(
float(item["valor"])
for item in transacoes
if item["tipo"] == "entrada"
)

total_saidas = sum(
float(item["valor"])
for item in transacoes
if item["tipo"] == "saida"
)

saldo = total_entradas - total_saidas

print(f"\nTotal de entradas: R$ {total_entradas:.2f}")
print(f"Total de saídas: R$ {total_saidas:.2f}")
print(f"Saldo do período: R$ {saldo:.2f}")

print("\nProdutos disponíveis:")
for produto in produtos:
print(f"- {produto['nome']}")

print("\n=== FIM DO TESTE ===")
