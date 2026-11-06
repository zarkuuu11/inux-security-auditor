import os
import subprocess
import platform
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=5)
        return result.stdout.strip()
    except Exception:
        return "N/A"

def check_ssh_root_login():
    config_path = "/etc/ssh/sshd_config"
    if not os.path.exists(config_path):
        return "Not Found", "Warning"
    
    output = run_command(f"grep -i '^PermitRootLogin' {config_path}")
    if "no" in output.lower():
        return "Disabled (Secure)", "Success"
    elif "yes" in output.lower():
        return "Enabled (Insecure)", "Danger"
    else:
        return "Default / Not Set", "Warning"

def check_open_ports():
    output = run_command("ss -tuln | grep LISTEN")
    count = len(output.splitlines()) if output else 0
    return f"{count} active listening ports", "Info"

def check_updates():
    if os.path.exists("/usr/bin/apt"):
        updates = run_command("apt-get -s upgrade | grep -i 'upgraded,'")
        return updates if updates else "System is up to date", "Success"
    return "Package manager not supported", "Warning"

def main():
    console.print(Panel.fit("[bold cyan]Linux Security & Compliance Auditor[/bold cyan]\n[italic]Created for IT STEP Academy Project[/italic]", border_style="cyan"))
    
    console.print(f"\n[bold]Operating System:[/bold] {platform.system()} {platform.release()}")
    console.print(f"[bold]Hostname:[/bold] {platform.node()}\n")

    table = Table(title="Security Audit Results", show_header=True, header_style="bold magenta")
    table.add_column("Check Item", style="dim", width=30)
    table.add_column("Finding / Status", width=35)
    table.add_column("Status Level", justify="right")

    ssh_status, ssh_level = check_ssh_root_login()
    table.add_row("SSH Root Login", ssh_status, f"[{'green' if ssh_level=='Success' else 'red'}]{ssh_level}[/]")

    ports_status, ports_level = check_open_ports()
    table.add_row("Active Listening Ports", ports_status, f"[yellow]{ports_level}[/]")

    updates_status, updates_level = check_updates()
    table.add_row("Pending System Updates", updates_status, f"[{'green' if updates_level=='Success' else 'yellow'}]{updates_level}[/]")

    console.print(table)
    console.print("\n[bold green]Audit completed successfully![/bold green]\n")

if __name__ == "__main__":
    main()
