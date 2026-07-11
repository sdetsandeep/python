import chromadb

client = chromadb.PersistentClient(path="mydb")

collection = client.create_collection("books")

print("Collection Created Successfully")
print(collection.get())