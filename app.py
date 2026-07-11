import chromadb

print("Step 1 : Library Loaded")

client = chromadb.PersistentClient(path="mydb")

print("Step 2 : Connected to Database")