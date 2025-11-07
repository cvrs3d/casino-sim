# Casino Simulation Architecture

## Overview
The Casino Simulation system is built using a microservices architecture with event-driven communication via RabbitMQ message broker.

## Architecture Diagram
```
    [User UI/CLI] → API Gateway
                       |
                       ↓
      ┌───────── Player Service ────────┐
      │                                  │
      └───────── Game Service ──────────┘
                      |
                      ↓
           Message Broker (RabbitMQ)
             /        |         \
          ↙           ↓           ↘
  Transaction    Admin Service  Visualizer
   Service                       Service
```

## Services

### Player Service
**Purpose**: Manage player accounts, balances, and basic operations
**Technology**: FastAPI + SQLAlchemy
**Database**: SQLite (per service)
**Port**: 8001

**Responsibilities**:
- Create player accounts
- Manage player balances
- Handle deposits and withdrawals
- Store player status (active/flagged/suspended)

### Game Service
**Purpose**: Execute slot game logic and resolve bets
**Technology**: FastAPI
**Port**: 8002

**Responsibilities**:
- Manage multiple slot game types (Lucky 7, MegaSpin, Diamond Reel)
- Accept and process bets
- Calculate win/lose outcomes
- Publish bet results to message broker

### Transaction Service
**Purpose**: Log all system events and transactions
**Technology**: FastAPI + SQLAlchemy
**Database**: SQLite
**Port**: 8003

**Responsibilities**:
- Subscribe to events from message broker
- Log all transactions (deposits, withdrawals, bets, results)
- Provide query API for transaction history
- Maintain audit trail

### Admin Service
**Purpose**: Monitor for fraud and manage player flags
**Technology**: FastAPI + SQLAlchemy
**Database**: SQLite
**Port**: 8004

**Responsibilities**:
- Subscribe to bet events
- Detect fraud patterns (consecutive wins, unusual betting)
- Flag suspicious players
- Suspend player accounts
- Provide admin dashboard API

### Visualizer Service
**Purpose**: Real-time dashboard for system monitoring
**Technology**: Streamlit
**Port**: 8501

**Responsibilities**:
- Subscribe to events from message broker
- Display live metrics (active players, total bets, wins)
- Show activity charts and trends
- Display recent events
- Monitor flagged players

## Communication Patterns

### Synchronous Communication
- REST APIs between services for direct queries
- Client → Service API calls

### Asynchronous Communication
- Event publishing via RabbitMQ
- Services subscribe to relevant event queues
- Loose coupling between services

## Event Flow Example: Placing a Bet

1. Client calls Player Service API to place bet
2. Player Service validates balance and deducts bet amount
3. Player Service calls Game Service API to process bet
4. Game Service executes game logic and determines outcome
5. Game Service publishes `bet_resolved` event to RabbitMQ
6. Transaction Service receives event and logs transaction
7. Admin Service receives event and checks for fraud patterns
8. Visualizer Service receives event and updates dashboard
9. If fraud detected, Admin Service flags player
10. Player Service receives flag notification and updates status

## Data Models

### Player
- id: integer
- name: string
- balance: float
- status: enum (active, flagged, suspended)

### Transaction
- id: integer
- player_id: integer
- type: enum (deposit, withdraw, bet, result, flag)
- amount: float
- game_id: string (optional)
- timestamp: datetime

### Slot Game
- id: string
- name: string
- min_bet: float
- max_bet: float
- win_probability: float
- payout_multiplier: float

## Technology Stack

- **Language**: Python 3.10+
- **Web Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Database**: SQLite (development), PostgreSQL (production)
- **Message Broker**: RabbitMQ
- **Dashboard**: Streamlit
- **Containerization**: Docker + Docker Compose
- **Testing**: pytest

## Deployment

The system is designed to run in Docker containers orchestrated by Docker Compose. Each service has its own container with isolated dependencies.

### Running the System
```bash
docker compose up --build
```

### Accessing Services
- Player Service: http://localhost:8001
- Game Service: http://localhost:8002
- Transaction Service: http://localhost:8003
- Admin Service: http://localhost:8004
- Visualizer Dashboard: http://localhost:8501
- RabbitMQ Management: http://localhost:15672

## Scalability Considerations

- Each service can be scaled independently
- Message broker provides buffering for high load
- Database per service ensures isolation
- Can migrate to Kubernetes for production
- Can replace SQLite with PostgreSQL for better performance

## Security Considerations

- Add authentication/authorization (JWT tokens)
- Encrypt sensitive data in transit (TLS)
- Rate limiting on APIs
- Input validation on all endpoints
- Secure RabbitMQ with proper credentials

## Future Enhancements

- Add more game types (roulette, blackjack)
- Implement distributed tracing (OpenTelemetry)
- Add API gateway (Kong, Nginx)
- Implement caching (Redis)
- Add metrics collection (Prometheus)
- Add ML-based fraud detection
