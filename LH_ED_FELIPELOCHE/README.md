# ETL Indicium Challenge - Development Process

## 📝 Challenge Context
This project was developed as part of the Indicium Tech challenge, focusing on creating an ETL pipeline that integrates data from the Northwind database (PostgreSQL) with order information (CSV). The main objective was to create an automated process for data extraction, transformation, and loading using Apache Airflow and Meltano.

## 🛠️ Technologies Used
- Docker and Docker Compose
- Apache Airflow 2.7.3
- PostgreSQL 13 (Airflow) and 12 (Northwind)
- Python 3.10
- Meltano (for ETL)

## 🔄 Development Process

### Phase 1: Environment Setup and Initial Configuration
- Migrated the development environment from Windows to Ubuntu for better compatibility
- Acquired basic knowledge of Linux commands required for the project
- Configured the Python environment with `venv`

### Phase 2: Implementation and Challenges
- **First Attempt**: Manual folder configuration on Windows
- **Second Attempt**: Migrated to Ubuntu and configured Docker
- **Third Attempt**: Implemented Airflow using the official `docker-compose`
- **Fourth Attempt**: Integrated Meltano and created DAGs
- **Fifth Attempt**: Refactored with a custom Dockerfile

### Key Challenges Encountered
1. Version compatibility between Python, SQLAlchemy, and Airflow
2. Correct configuration of paths for Meltano
3. Integration between different Docker containers
4. Managing dependencies within the Docker environment

## 🚀 How to Run (Current Version)

### Prerequisites
- Docker and Docker Compose installed
- Git
- Linux operating system (recommended)

### Installation
1. Clone the repository
   ```bash
   git clone https://github.com/your-user/LH_ED_FELIPELOCHE.git
   cd LH_ED_FELIPELOCHE
   ```
2. Configure the environment
	```bash
	echo "AIRFLOW_UID=$(id -u)" > .env
	```
3. Start the containers
	```bash
	docker-compose build --no-cache
	docker-compose up
	```

4. Access Airflow
	```bash
	URL: http://localhost:8081
	Username: admin
	Password: admin
	```

## 📋 Next Steps
Fix the Meltano integration with local files
Fully implement data transformations
Optimize the file storage structure
Implement automated tests

## 🎯 Learnings
Infrastructure: Importance of official documentation and deep understanding of the tools used  
Docker: Managing containers and networks, importance of correct versions  
ETL: Complexity of the data extraction and loading process, especially with multiple sources  
Development: Value of persistence and iterative problem-solving  

## ⚠️ Important Notes
The current project represents a work-in-progress version
Some functionalities still need to be implemented/fixed
The complete integration between Airflow and Meltano is under development
