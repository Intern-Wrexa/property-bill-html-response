import requests
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()


# root fucntion
@app.get("/")
async def root():
  html_content = """
    <html>
        <head>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                h1 {
                    font-size: 48px;
                    color: #333;
                }
            </style>
        </head>
        <body>
            <h1>Api Made By D</h1>
        </body>
    </html>
    """
  return HTMLResponse(content=html_content)



# get property details for old bill and html as response
@app.get("/fetch-property-details/old-bill/load-response/")
async def fetch_property_details(zone: str, ward: str, propertyId: str, subNo: str):
    url = f"https://erp.chennaicorporation.gov.in/ptis/citizensearch/searchPropByBillNumber!search.action?isNew=N&zoneNo={zone}&wardNo={ward}&propertyId={propertyId}&subNo={subNo}"

    response = requests.get(url)

    if response.status_code == 200:
        return HTMLResponse(content=response.text)
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch details")


# get property details for new bill and html as response
@app.get("/fetch-property-details/new-bill/load-response/")
async def fetch_property_details(zone: str, ward: str, bill: str):
    url = f"https://erp.chennaicorporation.gov.in/ptis/citizensearch/searchPropByBillNumber!search.action?isNew=Y&newzoneNo={zone}&newwardNo={ward}&newbillNo={bill}"

    response = requests.get(url)

    if response.status_code == 200:
        return HTMLResponse(content=response.text)
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch details")

