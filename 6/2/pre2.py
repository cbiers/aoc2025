import sys

def is_numeric_line(line: str) -> bool:
    """Return True if the line consists only of digits, spaces and newline."""
    s = line.rstrip('\n')
    return bool(s) and all(c.isdigit() or c == ' ' for c in s)

def main():
    for line in sys.stdin:
        if not is_numeric_line(line):
            # Keep non-numeric lines (with *, +, etc.) exactly as they are
            sys.stdout.write(line)
            continue

        # Split on any whitespace -> tokens are pure digit strings now
        tokens = line.split()
        padded = [t.zfill(4) for t in tokens]
        new_line = " ".join(padded)

        # Preserve newline if present
        if line.endswith('\n'):
            new_line += '\n'

        sys.stdout.write(new_line)

if __name__ == "__main__":
    main()
