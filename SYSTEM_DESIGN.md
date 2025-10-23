# SYSTEM DESIGN

## Introduction
This document provides comprehensive architecture documentation for a Bank & Credit Card Platform. It includes details on architecture, request flows, and implementation specifics.

## Architecture Overview
```mermaid
graph TD;
    A[User] -->|Initiate Request| B[API Gateway];
    B --> C[Authentication Service];
    B --> D[Transaction Service];
    B --> E[Account Service];
    C --> F[User Database];
    D --> G[Transaction Database];
    E --> H[Account Database];
```  
- **User**: The end-user interacting with the platform.  
- **API Gateway**: Entry point for all client requests.  
- **Authentication Service**: Manages user authentication and authorization.  
- **Transaction Service**: Handles all transaction-related operations.  
- **Account Service**: Manages user accounts and profiles.  
- **Databases**: Store user and transaction data.

## Request Flows
### User Registration Flow
```mermaid
sequenceDiagram
    participant User
    participant API Gateway
    participant Auth Service
    participant User Database
    User->>API Gateway: Register
    API Gateway->>Auth Service: Validate user info
    Auth Service->>User Database: Store user data
    User Database-->>Auth Service: Confirmation
    Auth Service-->>API Gateway: Success
    API Gateway-->>User: Registration Successful
```

### Transaction Processing Flow
```mermaid
sequenceDiagram
    participant User
    participant API Gateway
    participant Transaction Service
    participant Transaction Database
    User->>API Gateway: Initiate Transaction
    API Gateway->>Transaction Service: Process Transaction
    Transaction Service->>Transaction Database: Store Transaction
    Transaction Database-->>Transaction Service: Confirmation
    Transaction Service-->>API Gateway: Success
    API Gateway-->>User: Transaction Successful
```

## Implementation Details
- **Technologies Used**:  
  - Backend: Node.js, Express  
  - Database: MongoDB  
  - Frontend: React  

- **Key Classes and Methods**:  
  - `UserController`: Handles user registration and authentication.  
  - `TransactionController`: Manages transaction processing.  
  
- **Database Schema Overview**:  
  - User Collection: { userId, username, passwordHash, email }  
  - Transaction Collection: { transactionId, userId, amount, status }  

## Conclusion
This document outlines the architecture of the Bank & Credit Card Platform, detailing the implementation and request flows necessary for understanding the system's functioning.