from openrouter_service import ask_ai
from sqlalchemy import text

def generate_sql(question):

    prompt = f"""
You are a SQL generator AI.

Convert to SQLite SELECT query.

Table name: fabrics

Columns:
id
name
quantity
sustainability_score

ONLY return SQL query.
NO explanation.

Question:
{question}
"""

    sql = ask_ai(prompt)

    return sql.strip()


def execute_safe_query(db, sql):

    if not sql.lower().startswith("select"):
        raise Exception("Only SELECT allowed")

    result = db.execute(text(sql))

    rows = result.fetchall()

    columns = result.keys()

    data = []

    for row in rows:
        item = {}
        for i, col in enumerate(columns):
            item[col] = row[i]
        data.append(item)

    return data