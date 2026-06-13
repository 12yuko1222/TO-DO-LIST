from tortoise.models import Model
from tortoise.fields import intField,BooleanFiled,CharField


class Todo(Model):
    id=intField(pk=True)
    task=CharField(max_length=100,null=False)
    done=BooleanFiled(defult=False,null=False)