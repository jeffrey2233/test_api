import requests

target_url = "https://todo.pixegami.io/"


# API 應回傳一個訊息字串，例如：{"message": "Hello World from Todo API"}
def test_get_message():
    response = requests.get(target_url)
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert isinstance(data["message"], str)
    print(data)

def test_create_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    create_task_data = create_task_response.json()
    print(create_task_data)

    task_id = create_task_data["task"]["task_id"]
    get_task_response = requests.get(target_url + f"get-task/{task_id}")
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    print(get_task_data)
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]

def test_can_update_task():
    #creat a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]
    
    #update the task
    new_payload = {
        "user_id": payload["user_id"],
        "task_id": task_id,
        "content": "my updated content",
        "is_done": True
    } 
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200
    #get and validate the changed task
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()    
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["is_done"] == new_payload["is_done"]   

def create_task(payload):
    return requests.put(target_url + "/create-task", json=payload)

def update_task(payload):
    return requests.put(target_url + "/update-task", json=payload)

def get_task(task_id):
    return requests.get(target_url + f"get-task/{task_id}")

def new_task_payload():
    return {
        "content": "my test content",
        "user_id": "test_user",
        "is_done": False
    }

