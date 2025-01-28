# ETL Indicium Challenge - Processo de Desenvolvimento

## 📝 Contexto do Desafio
Este projeto foi desenvolvido como parte do desafio da Indicium Tech, focando na criação de um pipeline ETL que integra dados do banco Northwind (PostgreSQL) com informações de pedidos (CSV). O objetivo principal era criar um processo automatizado de extração, transformação e carga de dados usando Apache Airflow e Meltano.

## 🛠️ Tecnologias Utilizadas
- Docker e Docker Compose
- Apache Airflow 2.7.3
- PostgreSQL 13 (Airflow) e 12 (Northwind)
- Python 3.10
- Meltano (para ETL)

## 🔄 Processo de Desenvolvimento

### Fase 1: Ambiente e Configuração Inicial
- Migração do ambiente de desenvolvimento do Windows para Ubuntu para melhor compatibilidade
- Aprendizado básico de comandos Linux necessários para o projeto
- Configuração do ambiente Python com venv

### Fase 2: Implementação e Desafios
- **Primeira Tentativa**: Configuração manual das pastas no Windows
- **Segunda Tentativa**: Migração para Ubuntu e configuração do Docker
- **Terceira Tentativa**: Implementação do Airflow usando docker-compose oficial
- **Quarta Tentativa**: Integração com Meltano e criação de DAGs
- **Quinta Tentativa**: Refatoração usando Dockerfile personalizado

### Principais Desafios Encontrados
1. Compatibilidade de versões entre Python, SQLAlchemy e Airflow
2. Configuração correta dos caminhos para o Meltano
3. Integração entre diferentes containers Docker
4. Gerenciamento de dependências no ambiente Docker

## 🚀 Como Executar (Versão Atual)

### Pré-requisitos
- Docker e Docker Compose instalados
- Git
- Sistema operacional Linux (recomendado)

### Instalação
1. Clone o repositório
git clone https://github.com/seu-usuario/LH_ED_FELIPELOCHE.git
cd LH_ED_FELIPELOCHE

2. Configure o ambiente
echo "AIRFLOW_UID=$(id -u)" > .env

3. Inicie os containers
docker-compose build --no-cache
docker-compose up

4. Acesse o Airflow
URL: http://localhost:8081
Usuário: admin
Senha: admin

📋 Próximos Passos

Correção da integração Meltano com arquivos locais
Implementação completa das transformações de dados
Otimização da estrutura de armazenamento dos arquivos
Implementação de testes automatizados

🎯 Aprendizados

Infraestrutura: Importância da documentação oficial e da compreensão profunda das ferramentas utilizadas  
Docker: Gerenciamento de containers e redes, importância das versões corretas  
ETL: Complexidade do processo de extração e carga de dados, principalmente com múltiplas fontes  
Desenvolvimento: Valor da persistência e da abordagem iterativa na resolução de problemas  

⚠️ Notas Importantes

O projeto atual representa uma versão em desenvolvimento
Algumas funcionalidades ainda precisam ser implementadas/corrigidas
A integração completa entre Airflow e Meltano está em processo de finalização
