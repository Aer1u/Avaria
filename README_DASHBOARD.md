# Dashboard de Estoque Minimalista

Um dashboard elegante e funcional para gestão de estoque, com design corporativo minimalista.

## 🎨 Design

**Estilo**: Minimalismo Corporativo Elegante
- **Paleta**: Azul Profundo (#003d82) + Cinza + Branco
- **Tipografia**: Poppins (títulos) + Inter (conteúdo)
- **Layout**: Grid assimétrico com cards elevados
- **Animações**: Transições suaves e feedback visual imediato

## 🚀 Funcionalidades

✅ **Carregamento Automático de Dados**
- Lê dados de arquivo JSON na pasta `/public`
- Compatível com GitHub Pages
- Fácil atualização: basta alterar o arquivo `dados-estoque.json`

✅ **Barra de Pesquisa em Tempo Real**
- Busca por Produto, Posição ou ID Palete
- Debounce de 300ms para melhor performance
- Feedback visual imediato

✅ **Sistema de Filtros**
- Filtro por Capacidade
- Filtro por Nível
- Filtro por Drive Misturado
- Aplicação instantânea sem necessidade de botão "aplicar"

✅ **Visualizações de Dados**
- Cards de estatísticas (Total de Paletes, Quantidade, Posições, Capacidade Média)
- Tabela expansível com detalhes completos
- Indicadores visuais de status

✅ **Responsividade**
- Design mobile-first
- Funciona perfeitamente em desktop, tablet e mobile

## 📂 Estrutura do Projeto

```
dashboard-estoque/
├── client/
│   ├── public/
│   │   └── dados-estoque.json    ← Arquivo de dados (EDITAR AQUI)
│   ├── src/
│   │   ├── components/
│   │   │   ├── SearchBar.tsx     ← Barra de pesquisa
│   │   │   ├── DataTable.tsx     ← Tabela de dados
│   │   │   ├── StatCard.tsx      ← Cards de estatísticas
│   │   │   └── FilterPanel.tsx   ← Painel de filtros
│   │   ├── hooks/
│   │   │   └── useEstoqueData.ts ← Hook para carregar e filtrar dados
│   │   ├── pages/
│   │   │   └── Home.tsx          ← Página principal
│   │   └── index.css             ← Estilos globais
│   └── index.html
├── package.json
└── README_DASHBOARD.md
```

## 🔄 Como Atualizar os Dados

### Opção 1: Editar o arquivo JSON diretamente

1. Abra `client/public/dados-estoque.json`
2. Edite os dados conforme necessário
3. Salve o arquivo
4. O dashboard atualizará automaticamente

### Opção 2: Converter de Excel para JSON

Se você tem um arquivo Excel atualizado:

```bash
python3 << 'EOF'
import pandas as pd
import json

# Ler a planilha Excel
df = pd.read_excel('seu-arquivo.xlsx', sheet_name='Página1')

# Converter para JSON
data = df.to_dict(orient='records')

# Salvar como JSON
with open('client/public/dados-estoque.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✓ Arquivo convertido: {len(data)} registros")
EOF
```

## 🌐 Deploy no GitHub Pages

1. Faça push do projeto para seu repositório GitHub
2. Vá para Settings → Pages
3. Selecione "Deploy from a branch"
4. Escolha a branch `main` e pasta `/ (root)`
5. Clique em Save

O dashboard estará disponível em: `https://seu-usuario.github.io/dashboard-estoque`

## 💻 Desenvolvimento Local

```bash
# Instalar dependências
pnpm install

# Iniciar servidor de desenvolvimento
pnpm dev

# Build para produção
pnpm build

# Preview da build
pnpm preview
```

## 📊 Formato dos Dados

O arquivo `dados-estoque.json` deve ter a seguinte estrutura:

```json
[
  {
    "Posição atual": "G300001F0011",
    "Capacidade": 16,
    "Produto": "5016-01",
    "Quantidade/palete": 10,
    "Nivel": "0,1,2,3",
    "Profundidade": "1,2,3,4",
    "Quantidade Total": 160,
    "Drive Misturado": "",
    "ID Palete": "",
    "Qtd. de Palete": 1.0,
    "Data de Alteração": "16/02/2026",
    "Obsevarção": ""
  }
]
```

## 🎯 Customizações

### Alterar Cores

Edite as variáveis CSS em `client/src/index.css`:

```css
:root {
  --primary: oklch(0.35 0.18 250); /* Azul profundo */
  --foreground: oklch(0.15 0.02 250); /* Cinza escuro */
  /* ... outras cores ... */
}
```

### Alterar Tipografia

Edite as fontes em `client/index.html`:

```html
<link href="https://fonts.googleapis.com/css2?family=SuaFonte:wght@400;700&display=swap" rel="stylesheet" />
```

### Adicionar Novos Filtros

Edite `client/src/components/FilterPanel.tsx` e `client/src/hooks/useEstoqueData.ts`

## 📝 Notas

- O dashboard carrega dados de um arquivo JSON estático, ideal para GitHub Pages
- Não requer backend ou banco de dados
- Todos os filtros e buscas funcionam no navegador (frontend)
- A performance é excelente mesmo com milhares de registros

## 🤝 Suporte

Para dúvidas ou sugestões, entre em contato com o desenvolvedor.

---

**Versão**: 1.0.0  
**Última atualização**: Fevereiro 2026
