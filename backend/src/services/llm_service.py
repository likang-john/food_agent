import ast
from typing import Dict, Any, Optional
from src.services.llm_client import HelloAgentsLLM

PLANNER_PROMPT_TEMPLATE = """
你是一个顶级的营养学规划专家。你的任务是将用户提出的复杂问题分解成一个由多个简单步骤组成的行动计划。
请确保计划中的每个步骤都是一个独立的、可执行的子任务，并且严格按照逻辑顺序排列。
你的输出必须是一个Python列表，其中每个元素都是一个描述子任务的字符串。

问题: {question}

请严格按照以下格式输出你的计划，```python与```作为前后缀是必要的:
```python
["步骤1", "步骤2", "步骤3", ...]
```
"""
EXECUTOR_PROMPT_TEMPLATE = """
你是一位顶级的营养学执行专家。你的任务是严格按照给定的计划，一步步地解决问题。
你将收到原始问题、完整的计划、以及到目前为止已经完成的步骤和结果。
请你专注于解决“当前步骤”，并仅输出该步骤的最终答案，不要输出任何额外的解释或对话。

# 原始问题:
{question}

# 完整计划:
{plan}

# 历史步骤与结果:
{history}

# 当前步骤:
{current_step}

请仅输出针对“当前步骤”的回答:
"""
EXTRACT_PROMPT_TEMPLATE = """
你是一个顶级的营养学专家。你的任务是识别出用户给出文本中的所有食物并给出大致的卡路里。
请确保识别出的都是食物的名称, 卡路里是一个整数。
你的输出必须是一个Python字典，字典的key是食物名称，value是对应的卡路里。

问题: {response}

请参考以下格式输出你识别的结果，```python与```作为前后缀是必要的, 期间的内容严格按照python数组输出
```python
["步骤1", "步骤2", "步骤3", ...]
```
"""

class Executor:
    def __init__(self, llm_client: HelloAgentsLLM):
        self.llm_client = llm_client

    def execute(self, question: str, plan: list[str]) -> str:
        history = ""
        final_answer = ""
        ans = ""

        print("\n--- 正在执行计划 ---")
        for i, step in enumerate(plan, 1):
            print(f"\n-> 正在执行步骤 {i}/{len(plan)}: {step}")
            prompt = EXECUTOR_PROMPT_TEMPLATE.format(
                question=question, plan=plan, history=history if history else "无", current_step=step
            )
            messages = [{"role": "user", "content": prompt}]

            response_text = self.llm_client.think(messages=messages) or ""

            history += f"步骤 {i}: {step}\n结果: {response_text}\n\n"
            final_answer = response_text
            ans += final_answer + "\n\n"
            print(f"✅ 步骤 {i} 已完成，结果: {final_answer}")

        return ans


class Planner:
    def __init__(self, llm_client: HelloAgentsLLM):
        self.llm_client = llm_client

    def plan(self, question: str) -> list[str]:
        prompt = PLANNER_PROMPT_TEMPLATE.format(question=question)
        messages = [{"role": "user", "content": prompt}]

        print("--- 正在生成计划 ---")
        response_text = self.llm_client.think(messages=messages) or ""
        print(f"✅ 计划已生成:\n{response_text}")

        try:
            plan_str = response_text.split("```python")[1].split("```")[0].strip()
            plan = ast.literal_eval(plan_str)
            return plan if isinstance(plan, list) else []
        except (ValueError, SyntaxError, IndexError) as e:
            print(f"❌ 解析计划时出错: {e}")
            print(f"原始响应: {response_text}")
            return []
        except Exception as e:
            print(f"❌ 解析计划时发生未知错误: {e}")
            return []

# --- 4. 智能体 (Agent) 整合 ---
class PlanAndSolveAgent:
    def __init__(self, llm_client: HelloAgentsLLM):
        self.llm_client = llm_client
        self.planner = Planner(self.llm_client)
        self.executor = Executor(self.llm_client)

    def run(self, question: str):
        print(f"\n--- 开始处理问题 ---\n问题: {question}")
        plan = self.planner.plan(question)
        if not plan:
            print("\n--- 任务终止 --- \n无法生成有效的行动计划。")
            return
        final_answer = self.executor.execute(question, plan)
        print(f"\n--- 任务完成 ---\n最终答案: {final_answer}")
        return final_answer

def extract_food_items(agent:HelloAgentsLLM, response: str) -> dict:
    prompt = EXTRACT_PROMPT_TEMPLATE.format(response=response)
    messages = [{"role": "user", "content": EXTRACT_PROMPT_TEMPLATE}]
    response_text = agent.think(messages=messages)
    food_str = response_text.split("```python")[1].split("```")[0].strip()
    food_dict = ast.literal_eval(food_str)
    if not isinstance(food_dict, dict):
        return {}
    return food_dict

def process_food_query(query: str, location: Optional[str] = None, dietary_preferences: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    llm_client = HelloAgentsLLM()
    agent = PlanAndSolveAgent(llm_client)
    response = agent.run(query)

    return {
        "response": response,
        "food_items": [],
        "calories": [],
        "recommendations": ""
    }


if __name__ == "__main__":
    response = process_food_query("宫保鸡丁怎么做？")
    print(response)