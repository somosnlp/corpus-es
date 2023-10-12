from pathlib import Path
import pandas as pd
import re
import uuid

patron = r"_\d+_\d+_\d+"
values = list(Path("images").glob("*.jpg"))
images = [value.stem for value in values]
images = list(map(lambda x: re.sub(patron, "", x), images))
prompts = list(map(lambda x: x.replace("_", " "), images))

df = pd.DataFrame({"prompt": prompts, "image": values})
df["uuid"] = df["image"].apply(lambda x: str(uuid.uuid4()))
df.to_csv("final_dataset.csv", index=False)