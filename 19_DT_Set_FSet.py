# -------------------------------
# 5. Set Types
# -------------------------------

# Set (Unique Values)
languages = {"Python", "Java", "C++","Python"}

print("Set :", languages)
print("Data Type :", type(languages))
print()

# add some element to set  languages

languages.add("C Sharp");

print("Now the Set is  :", languages)

# -------------------------------
# Frozen Set (Cannot be Changed)
# -------------------------------

fset = frozenset({"Apple", "Banana", "Mango"})

print("Frozen Set :", fset)
print("Data Type :", type(fset))
print()





"""
1. Set क्या होता है?

Definition (आसान भाषा में):

Set एक ऐसा Collection है जिसमें केवल Unique (अलग-अलग) Elements होते हैं। Duplicate Values अपने आप हट जाती हैं।

Set को Curly Braces {} में लिखा जाता है।

Example
fruits = {"Apple", "Banana", "Mango"}

print(fruits)

Output

{'Apple', 'Banana', 'Mango'}
Duplicate Values
fruits = {"Apple", "Banana", "Apple", "Mango", "Banana"}

print(fruits)

Output

{'Apple', 'Banana', 'Mango'}

देखिए,

Apple दो बार था।
Banana दो बार था।

लेकिन Output में केवल एक-एक बार आया।

यही Set की सबसे बड़ी विशेषता है।

Set में Order निश्चित नहीं होता
numbers = {10, 20, 30, 40}

print(numbers)

Output कभी

{20, 10, 40, 30}

या

{40, 20, 10, 30}

आ सकता है।

क्योंकि Set Ordered Collection नहीं है।

Set Mutable होता है

यानी इसमें नए Elements जोड़ और हटा सकते हैं।

Add
fruits = {"Apple", "Banana"}

fruits.add("Mango")

print(fruits)

Output

{'Apple', 'Banana', 'Mango'}
Remove
fruits.remove("Banana")

print(fruits)

Output

{'Apple', 'Mango'}
Set का Real-life Example

मान लीजिए क्लास में बच्चों के नाम हैं:

Rahul
Mohit
Rahul
Ankit
Mohit

अगर Set बनाएँ

students = {"Rahul", "Mohit", "Rahul", "Ankit"}

Output

{'Rahul', 'Mohit', 'Ankit'}

Duplicate Names हट गए।

2. Frozen Set क्या होता है?

Definition

Frozen Set भी Set की तरह Unique Values रखता है, लेकिन इसे बनाने के बाद बदला नहीं जा सकता।

यानी यह Immutable Set है।

Example
fruits = frozenset({"Apple", "Banana", "Mango"})

print(fruits)

Output

frozenset({'Apple', 'Banana', 'Mango'})
इसमें Add नहीं कर सकते
fruits = frozenset({"Apple", "Banana"})

fruits.add("Mango")

Output

AttributeError
Remove भी नहीं कर सकते
fruits.remove("Apple")

Output

AttributeError
Set और Frozen Set में अंतर
Set	Frozen Set
Mutable (बदला जा सकता है)	Immutable (बदला नहीं जा सकता)
add() कर सकते हैं	add() नहीं कर सकते
remove() कर सकते हैं	remove() नहीं कर सकते
{} से बनता है	frozenset() Function से बनता है
बदलने योग्य Collection	स्थायी (Permanent) Collection
याद रखने की ट्रिक

🧺 Set = खुली टोकरी (Open Basket)

आप इसमें फल डाल भी सकते हैं और निकाल भी सकते हैं।

🍎 🍌 🥭

🧊 Frozen Set = फ्रीज़र में जमी हुई टोकरी (Frozen Basket)

एक बार रख दिया,

अब न कुछ जोड़ सकते,

न निकाल सकते।

कब Use करते हैं?
Set

जब Data बदलता रहता हो।

जैसे

Students
Subjects
Languages
Cities
Frozen Set

जब Data कभी नहीं बदलना हो।

जैसे

Week Days
Months
Fixed Permissions
Constant Categories
Exam Definition

Set: Set Python का एक Mutable Collection है जिसमें केवल Unique Elements होते हैं और Duplicate Values अपने आप हट जाती हैं।

Frozen Set: Frozen Set Python का एक Immutable Collection है जिसमें केवल Unique Elements होते हैं, लेकिन इसे बनाने के बाद इसमें कोई परिवर्तन (Add, Remove या Update) नहीं किया जा सकता।

"""