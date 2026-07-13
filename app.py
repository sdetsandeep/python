import chromadb


#print("Step 1 : Library Loaded")

client = chromadb.PersistentClient(path="mydb")

#print("Step 2 : Connected to Database")

collection = client.get_or_create_collection(name="books")
#collection = client.get_or_create_collection(name="books1")
print("Step 3 : Collection Ready")

# to see the collections in db 
print(client.list_collections())

"""
collection.add(
ids =["1"],
documents= ["Python is Very easy programming Lanugage .."],
   
  )

collection.add(
  
   ids =["2"],
documents= ["java is  also a Very easy programming Lanugage . but toughest more than python."],
)

collection.add(
    ids=["3"],
    documents=["LangChain is a framework."],
    metadatas=[
        {
            "author":"Sandeep",
            "subject":"AI"
        }
    ]
)
print("Step 4 : Document Added")

"""

print("Result 1 is ===============================================\n")

result1 = collection.query(
    query_texts=["Python language"],
    n_results=3
)

print(result1)

print("Result 2 is ===============================================\n")
result2 = collection.query(
    query_texts=["Java programming"],
    n_results=3
)

print(result2)

print("Result  3is ===============================================\n")

result3  =collection.query(
    query_texts=["Artificial Intelligence"],
    n_results=3
)

print(result3)