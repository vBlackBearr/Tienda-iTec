import aiohttp


async def request(method, url, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.request(method, url, **kwargs) as response:
            return response


async def getPartners():
    response = await request("GET", "http://localhost:8000/backend/partners")

    if response.status == 200:
        result = await response.json()
        return result


async def getPartner(partner_id):
    response = await request("GET", f"http://localhost:8000/backend/partners/{partner_id}")

    if response.status == 200:
        result = await response.json()
        return result
    else:
        return None


async def postPartner(new_partner):
    response = await request("POST", "http://localhost:8000/backend/partners", json=new_partner)

    if response.status == 200:
        result = await response.json()
        return result
    else:
        return None


async def updatePartner(partner_id, updated_partner):
    response = await request("PUT", f"http://localhost:8000/backend/partners/{partner_id}", json=updated_partner)

    if response.status == 200:
        result = await response.json()
        return result
    else:
        return None


async def deletePartner(partner_id):
    response = await request("DELETE", f"http://localhost:8000/backend/partners/{partner_id}")

    if response.status == 200:
        return True
    else:
        return False


async def getRawMaterials():
    response = await request("GET", "http://localhost:8000/backend/raw_materials")

    if response.status == 200:
        result = await response.json()
        return result
    else:
        return []


async def getRawMaterial(raw_material_id):
    response = await request("GET", f"http://localhost:8000/backend/raw_materials/{raw_material_id}")

    if response.status == 200:
        result = await response.json()
        return result
    else:
        return {}


async def postRawMaterial(new_raw_material):
    response = await request("POST", "http://localhost:8000/backend/raw_materials", json=new_raw_material)

    if response.status == 200:
        result = await response.json()
        return result
    else:
        return None


async def updateRawMaterial(raw_material_id, updated_raw_material):
    response = await request("PUT", f"http://localhost:8000/backend/raw_materials/{raw_material_id}",
                             json=updated_raw_material)

    if response.status == 200:
        result = await response.json()
        return result
    else:
        return None


async def deleteRawMaterial(raw_material_id):
    response = await request("DELETE", f"http://localhost:8000/backend/raw_materials/{raw_material_id}")

    if response.status == 200:
        return True
    else:
        return False


async def getProducts():
    url = "http://localhost:8000/backend/products"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                # Manejar otros códigos de estado si es necesario
                print(f"Error: {response.status}")


async def getProduct(product_id):
    response = await request("GET", f"http://localhost:8000/backend/products/{product_id}")

    if response.status == 200:
        result = await response.json()
        return result
    else:
        return None


async def postProduct(new_product):
    response = await request("POST", "http://localhost:8000/backend/products", json=new_product)

    if response.status == 200:
        result = await response.json()
        return result
    else:
        return None


async def updateProduct(product_id, updated_product):
    response = await request("PUT", f"http://localhost:8000/backend/products/{product_id}", json=updated_product)

    if response.status == 200:
        result = await response.json()
        return result
    else:
        return None


async def deleteProduct(product_id):
    response = await request("DELETE", f"http://localhost:8000/backend/products/{product_id}")

    if response.status == 200:
        return True
    else:
        return False


# async def getSales():
#     response = await request("GET", "http://localhost:8000/backend/sales")
#
#     if response.status == 200:
#         result = await response.json()
#         return result
#     else:
#         return []
async def getSales():
    url = "http://localhost:8000/backend/sales"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                # Manejar otros códigos de estado si es necesario
                print(f"Error: {response.status}")
    


async def getSale(sale_id):
    response = await request("GET", f"http://localhost:8000/backend/sales/{sale_id}")

    if response.status == 200:
        result = await response.json()
        return result
    else:
        return None

async def postSale(new_sale):
    response = await request("POST", "http://localhost:8000/backend/sales", json=new_sale)

    if response.status == 200:
        result = await response.json()
        return result
    else:
        return None

async def updateSale(sale_id, updated_sale):
    response = await request("PUT", f"http://localhost:8000/backend/sales/{sale_id}", json=updated_sale)

    if response.status == 200:
        result = await response.json()
        return result
    else:
        return None

async def deleteSale(sale_id):
    response = await request("DELETE", f"http://localhost:8000/backend/sales/{sale_id}")

    if response.status == 200:
        return True
    else:
        return False


async def getUsers():
    url = "http://localhost:8000/backend/users"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                # Manejar otros códigos de estado si es necesario
                print(f"Error: {response.status}")


async def getSaleStates():
    url = "http://localhost:8000/backend/users"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                # Manejar otros códigos de estado si es necesario
                print(f"Error: {response.status}")