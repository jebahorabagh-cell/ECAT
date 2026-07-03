from pathlib import Path
import json,logging

BASE=Path.cwd()
for d in ["logs","output","projects","temp","config"]:
    (BASE/d).mkdir(exist_ok=True)

cfg=BASE/"config"/"config.json"
if not cfg.exists():
    cfg.write_text(json.dumps({"theme":"light","window":[1100,700],"last_output":"output"},indent=2))

logging.basicConfig(filename=BASE/"logs"/"ecat.log",
level=logging.INFO,
format="%(asctime)s %(levelname)s %(message)s")

def initialize():
    logging.info("ECAT Started")
