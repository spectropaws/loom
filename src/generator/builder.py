import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from rich.console import Console 
from src.core.models import ProjectSpec


console = Console()


class ProjectBuilder:
    def __init__(self):
        template_dir = Path(__file__).parent / "templates"
        self.env = Environment(loader=FileSystemLoader(template_dir))

    def generate(self, spec: ProjectSpec, output_dir: Path = Path(".")):
        """
        Generates the flake.nix and justfile based on the spec.
        """
        console.print(f"[bold blue]Building environment for: {spec.name}[/bold blue]")

        # 1. Render flake.nix
        self._render_file("flake.nix.j2", "flake.nix", spec, output_dir)

        # 2. Render justfile
        self._render_file("justfile.j2", "Justfile", spec, output_dir)
        
        console.print("[bold green]Files generated successfully![/bold green]")
        console.print(f"Location: {output_dir.absolute()}")


    def _render_file(self, template_name: str, output_name: str, spec: ProjectSpec, output_dir: Path):
        template = self.env.get_template(template_name)
        # Convert Pydantic model to dict for Jinja
        content = template.render(**spec.model_dump())

        output_dir = output_dir / spec.name
        output_dir.mkdir(exist_ok=True)

        output_path = output_dir / output_name
        with open(output_path, "w") as f:
            f.write(content)
