
from agents.analytics.agent import analyze_results


QUESTION = (
    "Which are the top 3 product categories by total revenue "
    "from completed orders, excluding discontinued products?"
)

SQL = """
SELECT c.category_name,
       SUM(p.price * oi.quantity) AS total_revenue
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
JOIN categories c ON p.category_id = c.category_id
WHERE o.status = 'completed'
  AND p.discontinued = 0
GROUP BY c.category_name
ORDER BY total_revenue DESC
LIMIT 3;
"""

RESULTS = [
    {"category_name": "Electronics", "total_revenue": 1440.0},
    {"category_name": "Home & Kitchen", "total_revenue": 570.0},
    {"category_name": "Books", "total_revenue": 360.0}
]


def main():
    print("=" * 60)
    print("QPilot Analytics Agent Test")
    print("=" * 60)

    analysis = analyze_results(
        question=QUESTION,
        sql=SQL,
        results=RESULTS
    )

    print("\n[1] Analytical Summary")
    print("-" * 60)
    print(analysis.summary)

    print("\n[2] Key Insights")
    print("-" * 60)
    for insight in analysis.insights:
        print(f"- {insight}")

    print("\n[3] Visualization Recommendation")
    print("-" * 60)
    print(analysis.visualization.model_dump())

    print("\n" + "=" * 60)
    print("Analytics Agent test completed.")
    print("=" * 60)


if __name__ == "__main__":
    main()
