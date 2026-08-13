from agents.planner.agent import plan_user_request


def process_user_request(question: str):
    plan = plan_user_request(question)

    return {
        "success": True,
        "message": "Planner Agent executed successfully.",
        "user_query": plan.question
    }

