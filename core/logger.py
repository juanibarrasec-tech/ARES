from rich.console import Console
console = Console()

def info(msg):
    console.print(f"[cyan][INFO][/cyan] {msg}")

def good(msg):
    console.print(f"[green][OK][/green] {msg}")

def warn(msg):
    console.print(f"[yellow][WARN][/yellow] {msg}")

def error(msg):
    console.print(f"[red][ERROR][/red] {msg}")
