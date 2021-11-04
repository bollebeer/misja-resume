from pathlib import Path
import json

p = "/Users/misja/Repositories/misja-resume/static/img/interests"
pathlist = Path(p).glob('**/*.jpeg')
for path in pathlist:
     if path.is_file():
        cmd = f"cwebp 100 {path.name} -o {path.stem}.webp"
        print(cmd)

books = []

pathlist = Path(p).glob('**/*.webp')
for path in pathlist:
     if path.is_file():
       books.append({
           "src": f"img/interests/{path.name}",
           "alt": path.stem
       })

print(json.dumps(books, indent=2))