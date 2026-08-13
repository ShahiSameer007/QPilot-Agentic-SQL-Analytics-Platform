from api.schemas import ExecutionPlan


def plan_user_request(question: str) -> ExecutionPlan:
    """
    Creates an execution plan for the user's request.
    """

    return ExecutionPlan(
        task="analyze_sql",
        question=question
    )