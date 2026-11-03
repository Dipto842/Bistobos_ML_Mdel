import pickle
from unittest import result
from pymongo import MongoClient



model= pickle.load(
    open('model.pkl','rb')
)

encoding = pickle.load(
    open('encoding.pkl','rb')   
)

vector= pickle.load(
    open('vector.pkl','rb')
)


# mogobd connection
cline = MongoClient("mongodb+srv://Boos:C73zWfyeXuuiQjpx@cluster0.ssb3nmc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

bd= cline['Boss']
colechon = bd['Data']

# print(colechon)

# Data fine 

def  find_product (question):
    question=question.lower()
    for i in colechon.find():
        foditem=i['name'].lower()
        if foditem in question:
            return i
    return None        
# check in this funchon 
# item = find_product("pizza er dam koto")

# print(item)

# Price Intent

def get_Price (question):
    item =find_product(question)
    
    if item:
        return (
            f"{item['name']} er price "
            f"{item['price']} taka"
        )
    return "Sorry, I don't have the price information for that item."

# check in this function

# ite = get_Price("pizza er dam koto")

# print(ite)


# availability Intent

def get_Availability (question):
    item = find_product(question)
    if item:
        return(
            f"{item['name']} is available. "
            
        )
    return "Sorry, that item is not available."


item=get_Availability("pizza ache" )
# check in this function
# print(item)

# discount_questions

def get_Discound(question):
    item= find_product(question)
    if item:
        discount = item.get("discount", 0)
        return(
            f"{item['name']} er discount {discount}%"
            
        )
    return "Sorry, I don't have the discount information for that item."

# check in this function
# item = get_Discound("fish fry er discount koto")
# print(item)


# menu_query

def get_Menu():
    items= colechon.find()
    menuData =[]
    for item in items:
        menuData.append(
            item['name']
        )
    return (
            "Amader menu te ei item gulo ache: " + ", ".join(menuData)
        )

    # check in this function
# item = get_Menu()
# print(item)


# delivery_query
def get_Delivery():
    return "Amra delivery service provide kori. Apni amader website theke order korte paren."
   

    # order_query

def get_Order():
    return "Apni amader website theke order korte paren. Apnar order confirm hole amra apnar kache delivery korbo."

    # opening_query 
def opening_time():
    return "Amader restaurant protidin 10:00 AM theke 10:00 PM porjonto khola thake."

    # payment_query 
def payment_method():
    return "Apni cash, credit card, debit card,  er maddhome payment korte paren."
# greeting
def greeting():
    return "Hello! Amader restaurant e apnake swagatam."



    #  ML sathe counet

def chatBot(question):
    vecotor = vector.transform([question])

    result = model.predict(vecotor)[0]

    # print("Question:", question)
    # print("Raw Result:", result)
    # print("Type:", type(result))

    encoding_result = encoding.inverse_transform([result])[0]

    # check in this function
    # print("encoding_result", encoding_result)
    # print(encoding.classes_)
    # print("TEST QUESTION:", question)
    # print("RAW RESULT:", result)
    # print("INTENT:", encoding_result)



    if encoding_result == "price_query":
        return get_Price(question)
    if encoding_result == "availability_query":
        return get_Availability(question)
    if encoding_result == "discount_query":
        return get_Discound(question)
    if encoding_result == "menu_query":
        return get_Menu()
    if encoding_result == "delivery_query":
        return get_Delivery()
    if encoding_result == "order_query":
        return get_Order()
    if encoding_result == "opening_query":
        return opening_time()
    if encoding_result == "payment_query":
        return payment_method()
    if encoding_result == "greeting":
        return greeting()

    return "Sorry, I couldn't understand your question."


    # question = "শুক্রবার খোলা থাকে?"
    # ansar = chatBot(question)
    # print(ansar)

    # question = "chicken te kono offer cholche"
    # chatBot(question)

    # question = "restaurant er menu chai"
    # ansar = chatBot(question)
    # print(ansar)
    