from pathlib import Path
import json

p = 'massadata.json'
s = Path(p).read_text(encoding='utf8')
o = json.loads(s)


def main():
    total_sum = []
    entries = o['entries']
    for entry in entries:
        total_sum.append(entry["total"])
    print(sum(total_sum))


if __name__ == '__main__':
    main()
