import chromadb

print("Step 1 : Library Loaded")

client = chromadb.PersistentClient(path="mydb")

print("Step 2 : Connected to Database")

collection = client.get_or_create_collection(name="books")
#collection = client.get_or_create_collection(name="books1")
print("Step 3 : Collection Ready")

# to see the collections in db 
print(client.list_collections())

collection.add(
ids =["1"],
documents= ["Python is Very easy programming Lanugage .."],
   
  )

collection.add(
  
   ids =["2"],
documents= ["java is  also a Very easy programming Lanugage . but toughest more than python."],
)

print("Step 4 : Document Added")

print(collection.get())