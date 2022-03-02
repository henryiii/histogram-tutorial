import nox
from pathlib import Path

nox.needs_version = ">=2022.1.7"
DIR = Path(__file__).parent.resolve()


@nox.session
def pyodide(session: nox.Session) -> None:
    session.install("jupyterlite[contents,check]")
    session.run("jupyter", "lite", "init")
    output = DIR / "_output"
    build = output / "build"
    paths = [
        output / "jupyterlite.schema.v0.json",
        *build.glob("*.js"),
        *build.glob("*.js.map"),
    ]
    for path in paths:
        txt = path.read_text()
        txt = txt.replace(
            "https://cdn.jsdelivr.net/pyodide/v0.19.0",
            "https://cdn.jsdelivr.net/pyodide/dev",
        )
        path.write_text(txt)

    session.run("jupyter", "lite", "build")

    if "--serve" in session.posargs:
        session.install("jupyterlite[serve]")
        session.run("jupyter", "lite", "serve")
