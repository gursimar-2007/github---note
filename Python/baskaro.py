# Creates a 10 GB file almost instantly (if the filesystem supports sparse files)

file_size_gb = 10
filename = "large_file.bin"

with open(filename, "wb") as f:
    f.seek(file_size_gb * 1024 * 1024 * 1024 - 1)
    f.write(b"\0")

print(f"{filename} ({file_size_gb} GB) created.")
