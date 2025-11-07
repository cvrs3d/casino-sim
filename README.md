# Casino IS Simulation 🎰  
A simulated casino information system implemented via microservices, designed for academic project use (seminar/semester paper + demo).  
The system pushes the concept of players, slot games, administrators, transaction logging and visualization in a distributed architecture.

---

## Table of Contents  
- [Project Overview](#project-overview)  
- [Architecture](#architecture)  
- [Services](#services)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Running the System](#running-the-system)  
- [Domain Model & Key Flows](#domain-model--key-flows)  
- [Technology Stack](#technology-stack)  
- [Project Structure](#project-structure)  
- [Extensions & Future Work](#extensions--future-work)  
- [License & Academic Use](#license--academic-use)  

---

## Project Overview  
This project simulates a casino information system where:  
- **Players** can deposit, withdraw, place bets on slot games and maintain a balance.  
- **Slot Games** (three distinct types) receive bets, calculate outcomes (win/lose), update player balances and emit events.  
- **Administrators** monitor for fraud/fault patterns (such as abnormal betting or win streaks) and can flag/suspend players.  
- A **Transaction Logging Service** records all major events (deposits, bets, results, flags) in a human-readable log.  
- A **Visualization Dashboard** monitors key metrics (counts, in-flight bets, balance distributions, flagged players).  
- The system is built as a set of loosely-coupled microservices communicating via a message broker.

This setup allows demonstration of modern architectural patterns: asynchronous messaging, service decomposition, event logging, and real-time visualization — all suitable for an academic exposé on “Computational Models in Informatics”.

---

## Architecture  
```Below is a simplified representation of the architecture:

    [User UI/CLI] → API Gateway
                       |
                       ↓
      ┌───────── Player Service ────────┐
      │ │
      └───────── Game Service ──────────┘
                      |
                      ↓
           Message Broker (RabbitMQ)
             /        |         \
          ↙           ↓           ↘
  Transaction Service Admin Service Visualizer Service
```


- Players deposit & withdraw via the Player Service.  
- Bets are routed to the Game Service, which resolves outcomes and emits events.  
- The broker manages event distribution.  
- Transaction and Admin services subscribe to events; Visualizer also listens for dashboard updates.

---

## Services  
| Service Name            | Responsibility                                                  |
|-------------------------|-----------------------------------------------------------------|
| Player Service          | Manage player accounts, balances, deposits/withdrawals.         |
| Game Service            | Execute slot game logic, accept bets, compute win/lose results.|
| Transaction Service     | Log all events/transactions into storage, provide query APIs.  |
| Admin Service           | Monitor for fraud patterns, flag/suspend players.              |
| Visualizer Service      | Provide dashboard UI for live metrics and event flows.         |

---

## Getting Started  

### Prerequisites  
- Docker & Docker Compose installed.  
- (Optional) Python 3.10+ for local development without containers.  
- A modern web browser to open the dashboard.  

### Running the System  
1. Clone the repository:  
  ```bash
  git clone <your-repo-url>
  cd casino-sim
  ```

2. Build and start all services with Docker Compose:
  ```bash
  docker compose up --build
  ```

3. Open your browser to access:
  - Dashboard: http://localhost:8501 (Visualizer)
  - Broker UI: http://localhost:15672 (RabbitMQ Management — user: guest / password: guest)

4. Use the Player Service API (e.g., via curl, Postman) to create players, deposit funds, place bets.

5. Monitor logs, dashboard metrics, and transaction logs as the system runs.

---

## Domain Model & Key Flows

### Domain Entities
- Player: id, name, balance, status (active/flagged/suspended)
- SlotGame: id, name, bet_min, bet_max, payout_multiplier, win_probability
- Transaction: id, player_id, type (deposit/withdraw/bet/result/flag), amount, game_id, timestamp

### Example Flow: Place Bet
- Player Service receives POST /players/{id}/bets with amount and game type.
- Checks that balance >= bet → deducts bet amount.
- Routes request to Game Service: POST /games/{game_id}/bet.
- Game Service computes outcome (win/lose) → if win, computes payout.
- Game Service emits event:
  ```json
  {
   "type": "bet_resolved",
   "player_id": 123,
   "game_id": "Lucky7",
   "bet_amount": 50,
   "result": "win",
   "win_amount": 90,
   "timestamp": 1690000000
  }
  ```
- Transaction Service consumes event → writes record to transaction log.
- Admin Service consumes event → evaluates fraud rule (e.g., >3 wins in a row).
- Visualizer Service updates dashboard metrics.

---

## Technology Stack
- Language: Python 3.x
- Microservices Frameworks: FastAPI or Flask for REST APIs
- Message Broker: RabbitMQ
- Containerization: Docker & Docker Compose
- Databases: SQLite or PostgreSQL (one per service)
- Visualization: Streamlit dashboard
- Testing: pytest for unit/integration tests
- Logging/Monitoring: Structured logs, correlation IDs

---

## Project Structure
See the directory layout in the root of this repository.

Key folders include:
- services/ – each microservice with Dockerfile, src/, tests/.
- common/ – shared utilities/event-schemas.
- docs/ – architecture diagrams, sequence diagrams, API specs.
- docker-compose.yml – orchestrates all containers for local run.

---

## Extensions & Future Work
Possible enhancements for deeper simulation or production-style:

- Add additional game types (roulette, blackjack) with more complex rules.
- Introduce scaling: multiple game workers, horizontal scaling with Kubernetes.
- Integrate distributed tracing (OpenTelemetry + Jaeger).
- Use a persistent event log (e.g., Apache Kafka) for replay and auditing.
- Add user authentication and authorization (players, admins).
- Add real-time web frontend for players to log in and play.
- Enhance fraud detection with ML or statistical models.

---

## License & Academic Use
This project is developed for academic purposes (semester project) and may be used freely for learning, research, and demonstration. Commercial use is not intended without explicit permission.



