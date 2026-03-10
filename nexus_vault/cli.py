import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from .vault import NexusVault
from .generator import generate_secure_password
import os

app = typer.Typer(help="🛡️ Nexus-Vault: Professional File Encryption Utility")
console = Console()

def show_banner():
    banner = Panel(
        "[bold cyan]🛡️ NEXUS-VAULT v1.1[/bold cyan]\n[dim]High-Security File Encryption & Management[/dim]",
        border_style="cyan"
    )
    console.print(banner)

@app.command()
def lock(file_path: str, password: str = typer.Option(..., prompt=True, hide_input=True)):
    """🔒 Lock a file with AES-256 encryption."""
    show_banner()
    try:
        vault = NexusVault(password)
        with console.status("[bold yellow]Encrypting file...[/bold yellow]"):
            vault.lock_file(file_path)
        console.print(f"[bold green]✔ Successfully locked:[/bold green] {file_path}.nvlt")
    except Exception as e:
        console.print(f"[bold red]✘ Error:[/bold red] {str(e)}")

@app.command()
def unlock(vault_path: str, password: str = typer.Option(..., prompt=True, hide_input=True)):
    """🔓 Unlock an encrypted .nvlt file."""
    show_banner()
    try:
        vault = NexusVault(password)
        with console.status("[bold yellow]Decrypting file...[/bold yellow]"):
            vault.unlock_file(vault_path)
        console.print(f"[bold green]✔ Successfully unlocked:[/bold green] {vault_path[:-5]}")
    except Exception as e:
        console.print(f"[bold red]✘ Error:[/bold red] {str(e)}")

@app.command()
def generate(length: int = 24, symbols: bool = True):
    """🎲 Generate a secure random password for your vault."""
    show_banner()
    password = generate_secure_password(length, symbols)
    console.print(Panel(f"[bold white]{password}[/bold white]", title="[green]Generated Secure Password[/green]", border_style="green"))
    console.print("[dim]Note: Please save this password in a secure place. Loss of password means data loss![/dim]")

if __name__ == "__main__":
    app()
