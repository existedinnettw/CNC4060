"""Fail unless the wheel ships every assembly and the package metadata FreeCAD reads."""

import sys
import zipfile

WANT = [
    "cnc4060/package.xml",
    "cnc4060/pyproject.toml",
    "cnc4060/cads/4060CNC.FCStd",
    "cnc4060/cads/X-axis.FCStd",
    "cnc4060/cads/Y-axis.FCStd",
    "cnc4060/cads/Z-axis.FCStd",
    "cnc4060/cads/Z-carriage.FCStd",
]

(wheel,) = sys.argv[1:]
names = set(zipfile.ZipFile(wheel).namelist())
missing = [w for w in WANT if w not in names]
parts = sum(1 for n in names if n.startswith("cnc4060/cads/parts/") and n.endswith(".FCStd"))
print(f"{wheel}: {len(names)} files, {parts} parts")
if missing or parts == 0:
    sys.exit(f"missing from the wheel: {missing or 'cads/parts/*.FCStd'}")
