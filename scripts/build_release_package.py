#!/usr/bin/env python3
"""Build a deterministic manual-install DRA release archive."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
INTEGRATION = ROOT / "custom_components" / "deploy_relay"
DIST = ROOT / "dist"
PROVENANCE = ROOT / "docs" / "RUNTIME_PROVENANCE.json"

LEGAL_FILES = (
    "LICENSE",
    "COPYRIGHT.md",
    "AUTHORS.md",
    "BRANDING.md",
    "THIRD_PARTY.md",
    "README.md",
)

FIXED_TIME = (1980, 1, 1, 0, 0, 0)


def _version() -> str:
    manifest = json.loads((INTEGRATION / "manifest.json").read_text(encoding="utf-8"))
    version = str(manifest["version"]).strip()
    if not version:
        raise SystemExit("manifest version is empty")
    return version


def _archive_files() -> list[tuple[Path, str]]:
    files: list[tuple[Path, str]] = []
    for path in sorted(INTEGRATION.rglob("*")):
        if not path.is_file():
            continue
        if "__pycache__" in path.parts or path.suffix in {".pyc", ".pyo"}:
            continue
        rel = path.relative_to(ROOT).as_posix()
        files.append((path, rel))

    for name in LEGAL_FILES:
        path = ROOT / name
        if not path.is_file():
            raise SystemExit(f"required release file missing: {name}")
        files.append((path, name))

    if not PROVENANCE.is_file():
        raise SystemExit("runtime provenance is missing")
    files.append((PROVENANCE, "RUNTIME_PROVENANCE.json"))

    return sorted(files, key=lambda item: item[1])


def main() -> int:
    version = _version()
    package_root = f"deploy-relay-agent-v{version}"
    DIST.mkdir(parents=True, exist_ok=True)

    archive = DIST / f"{package_root}.zip"
    checksum = DIST / f"{package_root}.zip.sha256"

    if archive.exists():
        archive.unlink()
    if checksum.exists():
        checksum.unlink()

    files = _archive_files()
    with zipfile.ZipFile(
        archive,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as zf:
        for source, relative in files:
            info = zipfile.ZipInfo(
                filename=f"{package_root}/{relative}",
                date_time=FIXED_TIME,
            )
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            zf.writestr(info, source.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

    digest = sha256(archive.read_bytes()).hexdigest()
    checksum.write_text(f"{digest}  {archive.name}\n", encoding="utf-8")

    print(f"archive={archive}")
    print(f"sha256={digest}")
    print(f"files={len(files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
