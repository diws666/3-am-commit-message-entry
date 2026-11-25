import os

LINE = (
    "fix: production is down at 3 a.m. I have rolled back the deploy, "
    "the rollback, and my confidence in that order."
)


def write_entry(output_dir: str) -> None:
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    write_entry(out_dir)
    print("wrote", len(LINE.encode("utf-8")), "bytes to", os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
