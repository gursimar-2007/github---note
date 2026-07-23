filename = "large_file.bin"
size_gb = 10
chunk_size = 1024 * 1024  # 1 MB
chunk = b"\0" * chunk_size

with open(filename, "wb") as f:
    for _ in range(size_gb * 1024):
        f.write(chunk)

print(f"{filename} ({size_gb} GB) created.")
