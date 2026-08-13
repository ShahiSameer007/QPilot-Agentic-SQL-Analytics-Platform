def get_health_status():
    return {
        "status": "healthy",
        "service": "QPilot Backend",
        "version": "1.0.0"
    }


def process_query(question: str):
    return {
        "success": True,
        "message": "Query received successfully.",
        "user_query": question
    }

