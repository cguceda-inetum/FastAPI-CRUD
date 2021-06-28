from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db
from models import Post as ModelPost
from schemas import Post as SchemaPost
from typing import List

router = APIRouter()


@router.get("/posts/", response_model=List[SchemaPost])
def get_all_posts():
    db_posts = db.session.query(ModelPost).all()
    return db_posts


@router.get("/posts/{post_id}", response_model=SchemaPost)
def get_post(post_id: int):
    db_post = db.session.query(ModelPost).get(post_id)
    return db_post


@router.post("/posts/", response_model=SchemaPost)
def create_post(post: SchemaPost):
    db_post = ModelPost(**vars(post))
    db.session.add(db_post)
    db.session.commit()
    return db_post


@router.patch("/posts/{post_id}", response_model=SchemaPost)
def modify_post(post: SchemaPost):
    db_post = ModelPost(**vars(post))
    db.session.merge(db_post)
    db.session.commit()
    return db_post


@router.delete("/posts/{post_id}", response_model=SchemaPost)
def delete_post(post_id: int):
    db_post = db.session.query(ModelPost).get(post_id)
    db.session.delete(db_post)
    db.session.commit()
