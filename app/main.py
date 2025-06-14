from fastapi import FastAPI
import uvicorn
from router import employee,supplier,member,inventory,sale,sale_detail,product,purchase
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="超超批发系统")

# 允许的前端地址
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 或指定前端地址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employee.router,prefix="/employee",tags=["雇员接口"])
app.include_router(supplier.router,prefix="/supplier",tags=["供应商接口"])
app.include_router(member.router,prefix="/member",tags=["会员接口"])
app.include_router(inventory.router,prefix="/inventory",tags=["库存接口"])
app.include_router(sale.router,prefix="/sale",tags=["销售接口"])
app.include_router(sale_detail.router,prefix="/sale_detail",tags=["销售明细接口"])
app.include_router(product.router,prefix="/product",tags=["商品接口"])
app.include_router(purchase.router,prefix="/purchase",tags=["采购接口"])


if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True)