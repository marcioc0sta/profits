from fastapi import APIRouter

router = APIRouter()


@router.get('/', tags=['/'])
async def root():
    return {"message": "calculate profit"}
