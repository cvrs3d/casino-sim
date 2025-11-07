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



