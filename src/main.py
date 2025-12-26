import typer
from rich.console import Console 
from .core.models import ProjectSpec 
from .generator.builder import ProjectBuilder 
from .core.agent import LoomAgent


app = typer.Typer()
console = Console()


@app.command()
def init(
    language: str = typer.Option(..., help="Language preset (python/rust)"),
    name: str = typer.Option("my-project", help="Project name"),
    details: str = typer.Option("", help="Extra details")
):
    """
        Scaffold a Nix Environment
    """
    
    builder = ProjectBuilder()
    agent = LoomAgent()

    full_prompt = f"Create a {language} project named '{name}'. {details}"
    
    spec = agent.design_project_spec(full_prompt)

    if not spec:
        console.print(f"[bold red]Preset '{language}' not found.")
        raise typer.Exit(code=1)
    
    builder.generate(spec)


if __name__ == "__main__":
    app()
