from ..routers.admin import get_db, get_current_user
from fastapi import status
from ..models import Todos
from .utils import *

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

# def test_admin_read_all_authenticated(test_todo):
#     response = client.get("/adm    in/todo")
#     assert response.status_code == 200
#     print("#"*33)
#     print(response.json())
#     assert response.json() == [{"title":"Learn to code!", 
#                                 "description":"Need to learn everyday!",
#                                 "priority":5,
#                                 "complete":False,
#                                 "id":1,
#                                 "owner_id":1}]
    

def test_admin_read_all_authenticated(test_todo):
    response = client.get("/admin/todo")
    assert response.status_code == status.HTTP_200_OK
    print("#"*33)
    print(response.json())
    print("#"*33)
    assert response.json() == [{'complete': False, 'title': 'Learn to code!',
                                'description': 'Need to learn everyday!', 'id': 1,
                                'priority': 5, 'owner_id': 1}]