from pathlib import Path

home = Path.home()

src = Path(__file__).parent
include = src / ".include"
develop = src / ".develop"
