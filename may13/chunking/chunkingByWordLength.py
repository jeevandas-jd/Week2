

def chunkingTXT(text, n):
    
    #Chunk the text into n-length chunks.
    
    # Split the text into words
    words = text.split()
    
    # Create a list to hold the chunks
    chunks = []
    
    # Iterate over the words and create chunks
    for i in range(0, len(words), n):
        chunk = ' '.join(words[i:i+n])
        chunks.append(chunk)
    
    return chunks

if __name__ == "__main__":

    text=open("/home/jeevandas/KlaWa/Week2/may13/chunking/sample.txt").read()

    n=5
    chunks = chunkingTXT(text, n)
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}: {chunk}")