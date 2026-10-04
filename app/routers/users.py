from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_all_users():
    return {"name" : "Lda","name" : "Lodu"}

@router.get("/{item_num}")
async def which_num(item_num : int):
    return item_num
