import json
from pathlib import Path

files = ["priv_nad.json", "priv_my.json", "priv_hy.json", "priv_bs.json", "obsh_bs_mini.json"]  # ← свои файлы сюда

all_configs = []

for fn in files:
    data = json.loads(Path(fn).read_text(encoding="utf-8"))
    if isinstance(data, list):
        all_configs.extend(data)
    elif isinstance(data, dict):
        all_configs.append(data)

Path("rstnnl7202_gen_cfgs_crypt_2602").write_text(
    json.dumps(all_configs, ensure_ascii=False, indent=2),
    encoding="utf-8"
)