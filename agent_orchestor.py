import os
import json
import importlib
from datetime import datetime

AGENTS_FOLDER = "agents"
OUTPUT_FOLDER = "agent_outputs"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def normalize_output(raw_output):
    """
    Convert any agent output into structured JSON format.
    """

    if isinstance(raw_output, dict):
        return raw_output

    if isinstance(raw_output, str):
        try:
            # Try parsing JSON directly
            return json.loads(raw_output)
        except:
            # If not JSON → wrap as text response
            return {"response": raw_output.strip()}

    return {"response": str(raw_output)}


def execute_all_agents():

    final_output = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "agents": {}
    }

    for filename in os.listdir(AGENTS_FOLDER):

        if filename.endswith(".py") and not filename.startswith("__"):

            module_name = filename[:-3]
            module_path = f"{AGENTS_FOLDER}.{module_name}"

            try:
                module = importlib.import_module(module_path)

                # Auto-detect runnable attribute
                if hasattr(module, "run"):
                    raw_output = module.run()

                elif hasattr(module, module_name.replace("_agent", "")):
                    # If agent object exists but no run() → skip execution
                    continue

                else:
                    continue

                structured_output = normalize_output(raw_output)

                final_output["agents"][module_name] = structured_output

            except Exception as e:
                final_output["agents"][module_name] = {
                    "error": str(e)
                }

    return final_output


def save_json(data, filename="latest.json"):

    path = os.path.join(OUTPUT_FOLDER, filename)

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    return path


if __name__ == "__main__":

    data = execute_all_agents()
    path = save_json(data)

    print(f"JSON saved at: {path}")
