import aiohttp




async def request(method, url, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.request(method, url, **kwargs) as response:
            return response


async def getPartners():

    url = "http://localhost:8000/backend/partners"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return {"status_code": 200, "data": result}
            else:
                # Otro tipo de error
                print(f"Error: {response.status}")
                return {"error": f"Unexpected error: {response.status}", "status_code": response.status}


async def getPartner(partner_id):
    url = f"http://localhost:8000/backend/partners/{partner_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return {"status_code": 200, "data": result}
            elif response.status == 404:
                # Venta no encontrada
                print(f"Error: Partner with id {partner_id} not found.")
                return {"error": "Raw Material not found", "status_code": 404}
            else:
                # Otro tipo de error
                print(f"Error: {response.status}")
                return {"error": f"Unexpected error: {response.status}", "status_code": response.status}


async def postPartner(new_partner):
    response = await request("POST", "http://localhost:8000/backend/partners", json=new_partner)

    if response.status == 200:
        result = await response.json()
        return result
    else:
        return None


async def updatePartner(partner_id, partner_data):
    url = f"http://localhost:8000/backend/partners/{partner_id}"

    async with aiohttp.ClientSession() as session:
        async with session.put(url, json=partner_data) as response:
            if response.status == 200:
                result = await response.json()
                return {"status_code": 200, "data": result}
            elif response.status == 404:
                print(f"Error: Partner with id {partner_id} not found.")
                return {"error": "Partner not found", "status_code": 404}
            else:
                print(f"Error: {response.status}")
                return {"error": f"Unexpected error: {response.status}", "status_code": response.status}


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


async def getRawMaterial(raw_material):
    url = f"http://localhost:8000/backend/raw_materials/{raw_material}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return {"status_code": 200, "data": result}
            elif response.status == 404:
                # Venta no encontrada
                print(f"Error: Sale with id {raw_material} not found.")
                return {"error": "Raw Material not found", "status_code": 404}
            else:
                # Otro tipo de error
                print(f"Error: {response.status}")
                return {"error": f"Unexpected error: {response.status}", "status_code": response.status}


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

async def getRawMaterials():
    url = "http://localhost:8000/backend/raw_materials"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                # Manejar otros códigos de estado si es necesario
                print(f"Error: {response.status}")


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


async def getSales():
    url = "http://localhost:8000/backend/sales"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                print(f"Error: {response.status}")


async def getEarnings():
    url = "http://localhost:8000/backend/earnings"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                print(f"Error: {response.status}")


async def getSale(sale_id):
    url = f"http://localhost:8000/backend/sales/{sale_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return {"status_code": 200, "data": result}
            elif response.status == 404:
                # Venta no encontrada
                print(f"Error: Sale with id {sale_id} not found.")
                return {"error": "Sale not found", "status_code": 404}
            else:
                # Otro tipo de error
                print(f"Error: {response.status}")
                return {"error": f"Unexpected error: {response.status}", "status_code": response.status}


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


async def getPurchases():
    url = "http://localhost:8000/backend/purchases"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                print(f"Error: {response.status}")