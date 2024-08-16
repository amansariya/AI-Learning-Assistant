# AI Learning Assistant

## Introduction
**AI Learning Assistant** is a web-based application designed to be embedded into Canvas. It serves as a chatbot that has the knowledge of the course and can help answer students' queries with respect to the course. It combines FastAPI for backend services, Gradio for the user interface, and LangFlow for advanced AI workflows using Retrieval-Augmented Generation (RAG) pipelines. This application is containerized using Docker for easy deployment and scalability.

### Key Features:
- **Interactive chat interface** powered by Gradio
- **FastAPI backend** for routing and application management
- **LangFlow integration** for sophisticated AI responses
- **Dockerized setup** with a configurable Gunicorn server

## Architecture Overview
The application is designed with a modular architecture, combining FastAPI, Gradio, and LangFlow components. Docker is used to containerize the application, making it portable and easy to deploy across various environments.

- **FastAPI**: Acts as the main backend framework, managing routing and serving the Gradio interface.
- **Gradio**: Provides the frontend chat interface where users can interact with the AI.
- **LangFlow**: Handles the RAG pipeline for generating AI responses based on user input.
- **OpenAI API**: LangFlow uses OpenAI's GPT model to answer questions.
- **Astra Vector Database**: LangFlow uses Astra DB to ingest the files that provide the system with course-related knowledge as well as a retrieval pipeline to answer questions based on the entries in this database.
- **Docker**: Containerizes the entire application, ensuring consistency across different deployment environments.
- **Microsoft Azure**: Uses Container Registry and App Service to host the web application.

## Installation and Setup

### Prerequisites
- Docker installed on your system
- Python 3.11 or higher
- Access to OpenAI API and Astra DB credentials


### Description of Key Files
- **app.py**: The main application file that integrates FastAPI, Gradio, and LangFlow.
- **Dockerfile**: Specifies the Docker image configuration, including dependencies and the runtime environment.
- **gunicorn.conf.py**: Configuration file for Gunicorn, specifying worker processes, logging, and binding settings.
- **Vector Store RAG.json**: JSON configuration file that defines the LangFlow RAG pipeline for processing AI queries.

## Key Components

### FastAPI Application
The FastAPI application serves as the backend, routing requests and serving the Gradio interface. It integrates seamlessly with Gradio to provide an interactive user experience.

- **Main Route**: `/` - Redirects to the Gradio interface.
- **Gradio Integration**: The Gradio interface is mounted onto the FastAPI application, making it accessible via a specified route (`/gradio`).

### Gradio Interface
Gradio provides the frontend for the chat interface, allowing users to interact with the AI in a conversational manner.

- **Chat Interface**: Users can type messages and receive AI-generated responses in a chat-like interface.
- **Backend Processing**: User inputs are processed through the LangFlow RAG pipeline, which generates contextually relevant responses.

### LangFlow Integration
LangFlow is integrated into the application to manage AI workflows using a JSON configuration file (`Vector Store RAG.json`). This configuration defines the pipeline for generating responses based on user input.

- **Pipeline Configuration**: Managed via the JSON file, defining how input is processed and how responses are generated.
- **Flow Execution**: The `run_flow_from_json` function is used to execute the defined pipeline asynchronously within the application.
