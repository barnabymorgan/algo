::: mermaid
sequenceDiagram
    Client->>Rate Limiter: 1st Request (Accepted)
    Rate Limiter->>API Server: 1st Request
    Client->>Rate Limiter: 2nd Request (Accepted)
    Rate Limiter->>API Server: 2nd Request
    Client->>Rate Limiter: 3rd Request (Rejected)
    Rate Limiter-->>Client: Too many requests

:::
