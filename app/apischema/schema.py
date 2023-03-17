from pydantic import BaseModel
import inspect
from typing import Type, Optional
from pydantic import BaseModel
from fastapi import Form


def as_form(cls: Type[BaseModel]):
    new_parameters = []

    for field_name, model_field in cls.__fields__.items():
        model_field: ModelField  # type: ignore

        new_parameters.append(
             inspect.Parameter(
                 model_field.alias,
                 inspect.Parameter.POSITIONAL_ONLY,
                 default=Form(...) if model_field.required else Form(model_field.default),
                 annotation=model_field.outer_type_,
             )
         )

    async def as_form_func(**data):
        return cls(**data)

    sig = inspect.signature(as_form_func)
    sig = sig.replace(parameters=new_parameters)
    as_form_func.__signature__ = sig  # type: ignore
    setattr(cls, 'as_form', as_form_func)
    return cls


# Create ToDoRequest Base Model
class ToDoRequest(BaseModel):
    task: str


@as_form
class Update_template_schema(BaseModel):
    internal_id: int
    data: str
    name: str


@as_form
class New_template_schema(BaseModel):
    name: str
    data: str


@as_form
class New_user_schema(BaseModel):
    name: str
    email: str


@as_form
class New_campaign_schema(BaseModel):
    name: str


class Generate_email_schema(BaseModel):
    template_data: str
    _id: int | None = None
    name: str | None = None
    data: str | None = None


class Load_template_schema(BaseModel):
    _id: int


class Subscriber_status(BaseModel):
    subscribed: Optional[bool]
    unsubscribed: Optional[bool]
    resubscribed: Optional[bool]


class Email_to_send_task(BaseModel):
    campaign_id: int
    campaign_name:str
    template_id: int
    subscriber_id: int
    subscriber_email: str
    subscriber_name: str
    encoded_params:bytes
    base_url: str
