# from fastapi import FastAPI, Request
# from pydantic import BaseModel

# app = FastAPI()

# @app.post('/')
# async def Test2(request: Request):
#     print(await request.body())  #This is returning future type make the awaiat req here with async of the function
#     return "Hello World"

# def test(Q: str):  # THis is going to be considerred as the query not  so to have request make function as att as type Request
#     return "hello"


#now when I want to make the body in non json format i.e. convert the jason to a type we can use "Decode Method" only issue is that cant be applied directly we need to wrap the 
# await body function and then use it as the byte steam is not completed tiill we complete the await function causing thhe unnecesarry errors
# @app.post('/')
# async def Test2(request: Request):
#     # print(await request.body().decode())   # this causes the internal server error thus making wrap the entire body of await function then use it
#     print((await request.body()).decode())  # this is how to use decode 
#     return "Hello World"


# this is simple way of accesing the request body but for larger applications there is an even reliable way
# for that we are gonna use "pydanting" 
# thus import pydanting first to be specific "BAseModel"
# @app.post('/')   # position of app path also plays significant role in api building as this is causing error as the class is also inside this route which shouldent be here
#thats why get class Test out of the app Route

# class Test (BaseModel): #class Test Inherited from baseModel which is part of pydant 
#     name: str
#     age : int # this basemodel class provide an interesting feature of auto parsing . This age variable even if passed a string it extracts the numbers from it if available else throw errror


# @app.post('/')
# def Test(t: Test):
#     print(t) # there is no need to deecode the json here as it gives direct the non json formaat
#             # So there is no need to manually redecode this as this throghs internal server exception 

#     return "hello world"

