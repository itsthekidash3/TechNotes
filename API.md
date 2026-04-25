API: Rules that let software systems communicate.

API styles/protocols:
- REST: Resource-based web APIs, typically JSON.
- GraphQL: Query language; clients request exactly what they need.
- gRPC: High-performance RPC for microservices (Protocol Buffers).
- SOAP: XML-based, common in enterprise.
- WebSocket: Persistent, bi-directional, low-latency communication.

HTTP methods (common in REST):
- GET, POST, PUT, DELETE (over HTTPS)

Common status codes:
- 200: Success
- 400: Client error
- 500: Server error

Request components:
- Headers, cookies

Authentication:
- Tokens (incl. JWT: header + payload + signature)
- OAuth
- Session-based auth

API tools/specs:
- OpenAPI
- Swagger
- Postman

Key features:
- Pagination
- Versioning
- Query params vs path params
- Idempotency (safe to retry without unintended effects)

Performance & scaling:
- Caching (e.g., Redis), rate limiting, load balancing
- Indexing, performance testing
- Vertical vs horizontal scaling

API gateway examples:
- AWS API Gateway
- NGINX
- Kong

Frameworks:
- Flask
- Django
- FastAPI
- Node.js
- Spring

Integration patterns:
- Sync vs async
- Webhooks
- batch processing
- message queues


API thinking:

                                                                                                                                                                                 
  1. What am I sending?                                                                                                                                                           
  2. What are they promising back?                                                                    
  3. What do I do with it? 
