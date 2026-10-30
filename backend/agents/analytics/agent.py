
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from api.schemas import AnalyticsResponse

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

structured_llm = llm.with_structured_output(
    AnalyticsResponse,
    method="json_schema"
)


def analyze_results(
    question: str,
    sql: str,
    results: list[dict]
) -> AnalyticsResponse:
    """
    Analyzes SQL execution results and generates
    meaningful insights and visualization recommendations.
    """

    prompt = f"""
You are the Analytics Agent for QPilot,
an Agentic SQL Analytics Platform.

Your job is to interpret database query results
and communicate useful analytical findings.

USER QUESTION:
{question}

EXECUTED SQL:
{sql}

DATABASE RESULTS:
{results}

INSTRUCTIONS:

1. Write a concise summary answering the user's question.
2. Identify meaningful patterns, comparisons, trends,
   or unusual observations supported by the results.
3. Generate insights using only the supplied data.
4. Do not invent statistics, values, or explanations.
5. Recommend a visualization only when it adds value.
6. Select an appropriate chart type from:
   bar, line, pie, scatter, histogram, box.
7. Specify the correct data fields for the chart axes.
8. If visualization is not useful, set recommended to false
   and chart_type, x_axis, y_axis, and title to null.
9. Explain your visualization decision in the reason field.

Return the response using the required structured schema.
"""

    return structured_llm.invoke(prompt)
