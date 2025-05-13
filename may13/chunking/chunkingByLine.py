def chunkingByline(file):
  
    lines=[]

    with open(file, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines
if __name__ == "__main__":
    file=  "/home/jeevandas/KlaWa/Week2/may13/chunking/sample.txt"
    chunkSize=5
    lines = chunkingByline(file)
    for i, line in enumerate(lines):
        print(f"Line {i+1}: {line}")