from tortoise.models import Model
from tortoise.fields import IntField, BooleanField, CharField  # تم تصحيح الحروف الكبيرة والإملاء


class Todo(Model):
    id = IntField(pk=True)  # I كبيرة
    task = CharField(max_length=100, null=False)
    done = BooleanField(default=False, null=False)  # تصحيح Field و default