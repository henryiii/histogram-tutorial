import nox
from pathlib import Path

nox.needs_version = ">=2022.1.7"
DIR = Path(__file__).parent.resolve()


@nox.session
def pyodide(session: nox.Session) -> None:
    session.install("jupyterlite[contents,check]>=0.1.0b5")
    session.run("jupyter", "lite", "init")
    session.run("jupyter", "lite", "build")

    if "--serve" in session.posargs:
        session.install("jupyterlite[serve]")
        session.run("jupyter", "lite", "serve")
