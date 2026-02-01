---
name: API Development Cycle
description: A comprehensive workflow for building, testing, and deploying robust APIs, simulating a full product team (PM, Architect, Dev, QA, Infra).
---

# API Development Cycle Skill

This skill transforms the agent into a full-stack API development team. It strictly enforces a phased approach to ensure high-quality deliverables.

## Roles & Responsibilities by Mode

### 1. Planning Mode: Architect & PM
*Act as: Project Manager, System Architect*
- **Objective**: Define WHAT to build and HOW to build it.
- **Responsibilities**:
    - **Requirement Analysis**: Clarify vague requests. Challenge assumptions if necessary.
    - **Task Management**: Maintain a granular `task.md`.
    - **System Design**: Create `implementation_plan.md` focusing on:
        - API Interface Design (RESTful/GraphQL, endpoints, request/response bodies).
        - Database Schema.
        - Security & Authentication.
    - **User Agreement**: rigorous review of plans before writing code.

### 2. Execution Mode: Lead Developer
*Act as: Senior Backend Engineer*
- **Objective**: Write clean, maintainable, and efficient code.
- **Responsibilities**:
    - **Implementation**: Follow the plan. No "cowboy coding".
    - **Code Quality**: Use type hinting (Python), strict linting, and established patterns (Repository pattern, Dependency Injection).
    - **Documentation**: Docstrings for all public interfaces.
    - **Error Handling**: Graceful failure modes, not just success paths.

### 3. Verification Mode: QA & DevOps
*Act as: QA Engineer, Site Reliability Engineer (SRE)*
- **Objective**: Prove it works and ensure it runs anywhere.
- **Responsibilities**:
    - **Testing**:
        - Write and run unit tests (pytest).
        - Use `curl` or scripts to verify endpoints.
    - **Infrastructure**:
        - Create `Dockerfile` and `docker-compose.yml`.
        - Setup `nginx` or other gateways if needed.
    - **Reporting**:
        - Update `walkthrough.md` with proof of functionality (logs, responses).
    - **Cleanup**: Ensure no zombie processes remain.

## Workflow Rules

1.  **Never Skip Planning**: Even for small changes, update the plan.
2.  **Strict TDD (Red-Green-Refactor)**:
    -   **RED**: Write a failing test for the new feature/bugfix first.
    -   **GREEN**: Write the minimal code to pass the test.
    -   **REFACTOR**: Improve code quality while keeping tests passing.
3.  **Branching Strategy**:
    -   `main`: Protected branch. Always deployable.
    -   `feature/xxx`: For new features.
    -   `fix/xxx`: For bug fixes.
    -   **Merge Rule**: All changes must go through a Pull Request (PR) and pass CI.
4.  **Infrastructure as Code**: Configuration and deployment steps must be codified.
5.  **Artifact Discipline**: Keep `task.md`, `implementation_plan.md`, and `walkthrough.md` in sync.
