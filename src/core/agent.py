from openai import OpenAI
import instructor
from .models import ProjectSpec
from src import config


class LoomAgent:
    def __init__(self):
        openai_client = OpenAI(
            base_url = config.settings.LLM_API_URL,
            api_key = config.settings.LLM_API_KEY
        )
        self.client = instructor.from_openai(openai_client)

    def design_project_spec(self, prompt: str):
        # not in dotenv for now
        SYSTEM_PROMT = """
        You are an export NixOS engineer.
        Your job is to convert user requirements into a structured JSON specification.
        Always prefer the nixpkgs names for packages (e.g. python3 not python).
        """

        project_spec = self.client.chat.completions.create(
            model = config.settings.LLM_MODEL_NAME,
            response_model = ProjectSpec,

            messages=[
                {"role": "system", "content": SYSTEM_PROMT},
                {"role": "user", "content": prompt}
            ],
        )

        return project_spec


