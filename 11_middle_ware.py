from fastapi import FastAPI,Request

app=FastAPI()

@app.middleware("http")
async def middle_ware(request:Request,call_stack):
    print("request sent")

    response=await call_stack(request)

    print("request recieve")

    return response
    