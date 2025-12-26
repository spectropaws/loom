from pydantic import BaseModel
from typing import List, Dict

class ProjectSpec(BaseModel):
    """
    Defines the blueprint of the project environment.
    """

    name: str
    description: str
    system: str = "x86_64-linux"
    packages: List[str]
    shell_hook: str = ""
    env_vars: Dict[str, str] = {}

    just_commands: Dict[str, str] = {}
