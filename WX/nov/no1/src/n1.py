# ///////////////////////////////
# n1.pu = Testing out models
# ///////////////////////////////

# --- Imports ----

import os

from dotenv import load_dotenv
from rich import print as rpr

# --- Vars ----

load_dotenv("src/.azz")
NV_T = os.getenv("NOV")

# --- Main ----


def n1_main():
    pass


# --- Subs ----
def brint_env():
    rpr(f"[bold green]NOV:[/bold green] {NV_T}")
