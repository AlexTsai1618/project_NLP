from pathlib import Path
import os
d=Path(testDB.db).resolve().parents[2]
print(os.path.join(d,test.db))
