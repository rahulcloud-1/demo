from fastapi import FastAPI, Request
from pydantic import BaseModel
from openai import AzureOpenAI
import json
from fastapi.middleware.cors import CORSMiddleware  # Import CORSMiddleware

app = FastAPI()

# Define request body model
class ImageGenerationRequest(BaseModel):
    model: str
    prompt: str
    n: int

client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint="https://il-openai-poc1.openai.azure.com/",
    api_key="321caa2fd2e4493897e027a9a1469bc0",
)

@app.post("/generate/image")
async def generate_image(request: Request, image_request: ImageGenerationRequest):
    model = image_request.model
    prompt = image_request.prompt
    n = image_request.n

    result = client.images.generate(
        model=model,
        prompt=prompt,
        n=n
    )

    image_url = json.loads(result.model_dump_json())['data'][0]['url']
    return {"image_url": image_url}

# Add CORS middleware with allow_origins=["*"] to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
































# from fastapi import FastAPI, Request
# from pydantic import BaseModel
# from openai import AzureOpenAI
# import json

# app = FastAPI()

# # Define request body model
# class ImageGenerationRequest(BaseModel):
#     model: str
#     prompt: str
#     n: int

# client = AzureOpenAI(
#     api_version="2024-02-01",
#     azure_endpoint="https://il-openai-poc1.openai.azure.com/",
#     api_key="321caa2fd2e4493897e027a9a1469bc0",
# )

# @app.post("/generate/image")
# async def generate_image(request: Request, image_request: ImageGenerationRequest):
#     model = image_request.model
#     prompt = image_request.prompt
#     n = image_request.n

#     result = client.images.generate(
#         model=model,
#         prompt=prompt,
#         n=n
#     )

#     image_url = json.loads(result.model_dump_json())['data'][0]['url']
#     return {"image_url": image_url}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)


























# from fastapi import FastAPI
# from openai import AzureOpenAI
# import json
# import uvicorn

# app = FastAPI()

# # Initialize AzureOpenAI client
# client = AzureOpenAI(
#     api_version="2024-02-01",
#     azure_endpoint="https://il-openai-poc1.openai.azure.com/",
#     api_key="321caa2fd2e4493897e027a9a1469bc0",
# )

# @app.get("/generate/image")
# async def generate_image():
#     # Generate image using DALL-E 3
#     result = client.images.generate(
#         model="Dalle3",  # the name of your DALL-E 3 deployment
#         prompt="An image displaying a variety of clothing items with a debit card and balloons.",
#         n=1
#     )

#     image_url = json.loads(result.model_dump_json())['data'][0]['url']
#     return {"image_url": image_url}

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

































# # Note: DALL-E 3 requires version 1.0.0 of the openai-python library or later
# import os
# from openai import AzureOpenAI
# import json

# client = AzureOpenAI(
#     api_version="2024-02-01",
#     azure_endpoint="https://il-openai-poc1.openai.azure.com/",
#     api_key="321caa2fd2e4493897e027a9a1469bc0",
# )

# result = client.images.generate(
#     model="Dalle3", # the name of your DALL-E 3 deployment
#     prompt="An image displaying a variety of clothing items with a debit card and balloons.",
#     n=1
# )

# image_url = json.loads(result.model_dump_json())['data'][0]['url']
# print (image_url)
