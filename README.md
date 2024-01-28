## Billet Tasks

Simple Task management CRUD API

### Requirements

```sh
$ docker --version
Docker version 24.0.2, build cb74dfc # or later
```

### How to setup

```sh
# and wait for all services to be up
docker compose up
```

And voilà, your web server should be running @ http://localhost:3000

### How to run tests

```sh
# while having the containers of the project up and running
docker exec -ti billet_api pytest .
```

### Endpoints

Users

```sh
# returns a list of all the existing users
GET /v1/users

# response
[
    {
        "id": 1,
        "username": "john.doe",
        "created_at": ""
    }
]
```

```sh
# returns a single user (if it exists)
GET /v1/users/{userId}

# response
{
    "id": 1,
    "username": "john.doe",
    "created_at": ""
} # or null in case it does not exist
```

```sh
# creates a user
POST /v1/users

# payload sample
{
    "username": "john.doe@gmail.com",
}

# response sample
{
    "id": 1,
    "username": "john.doe@gmail.com",
    "created_at": "Y-M-D"
}
```

```sh
# returns a list of all the tasks assigned to the specified user (if it exists)
GET /v1/users/{userId}/tasks

# response
[
    {
        "id": 1,
        "name": "john.doe",
        "desc": "Generic description",
        "status": "PENDING",
        "expires_at": "Y-M-D", # Optional
        "created_at": ""
    }
]
```

```sh
# deletes a user
DELETE /v1/users/{user_id}

# response
{
    "success": True,
    "detail": "xxx.yyy"
}
```

Tasks:

```sh
# returns a list of all the existing tasks
GET /v1/tasks

# response
[
    {
        "id": 1,
        "name": "john.doe",
        "desc": "Generic description",
        "status": "PENDING",
        "expires_at": "Y-M-D", # Optional
        "created_at": ""
    }
]
```

```sh
# creates a task
POST /v1/tasks

# payload
{
    "name": "john.doe",
    "desc": "Generic description",
    "status": "PENDING",
    "expires_at": "Y-M-D" # Optional
}

# response
{
    "success": true,
    "detail": "xxx.yyy",
    "payload": {
        "id": 1,
        "name": "john.doe",
        "desc": "Generic description",
        "status": "PENDING",
        "expires_at": "Y-M-D" # or null
    }
}
```

```sh
# updates a task
PUT /v1/tasks/{taskId}

# payload
{
    "name": "john.doe",
    "desc": "Generic description",
    "status": "PENDING",
    "expires_at": "Y-M-D" # Optional
}

# response
{
    "success": true,
    "detail": "xxx.yyy",
    "payload": {
        "id": 1,
        "name": "john.doe",
        "desc": "Generic description",
        "status": "PENDING",
        "expires_at": "Y-M-D", # or null
        "created_at": ""
    }
}
```

```sh
# assigns a task to a user
PUT /v1/tasks/{taskId}/assign/user/{userId}

# response
{
    "success": true,
    "detail": "xxx.yyy",
}
```

```sh
# unassigns a task from a user
PUT /v1/tasks/{taskId}/unassign/user/{userId}

# response
{
    "success": true,
    "detail": "xxx.yyy",
}
```

```sh
# deletes a task
DELETE /v1/tasks/{taskId}

# response
{
    "success": true,
    "detail": "xxx.yyy",
}
```
