import typer
from rich.console import Console
from . import make_anagrams, make_acronym

console = Console()
console.print('[u]uv-assignment[/u] - [i]PIAIC258257[/i]\n')

app = typer.Typer(help="Wordplay CLI")


@app.command()
def anagram(word: str, limit: int = 5):
    """Generate a random anagrams of a word."""
    results = make_anagrams(word, limit)
    console.print("[bold green]Results:[/bold green]\n" + '\n'.join([f" • [blue italic]{res}[/blue italic]" for res in results]))


@app.command()
def acronym(phrase: str):
    """Generate an acronym from a phrase."""
    result = make_acronym(phrase)
    console.print("[bold green]Result:[/bold green]", f"{result} ([i]{phrase}[/i])")


if __name__ == "__main__":
    app()