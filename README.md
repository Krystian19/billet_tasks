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

### Questions

> How would you handle pagination and ordering of tasks ?

In the case of pagination i would use a `page_size` and `offset` counter to as a
pagination mechanism, and in the case of ordering the tasks by default they should
be ordered by `created_at` DESC, so that you get the latest ones first, and provide
the users with an option to sort them by `expires_at` so that they get the most "urgent"
tasks first on the list.

> What measures would you take to ensure operational safety ?

Implementing some sort of authentication mechanism, so that we can control who does what is a must,
additionally i can see a good use case for some sort of API throttling mechanism to prevent
abuse from external users.

> How would you scale this application if the number of users and tasks increases significantly ?

There's a quote that represents this problem perfectly:

```sh
"Premature optimization is the root of all evil"
```

How i would go about it, is to identify the bottlenecks that are affecting the end users first,
which in turn can be easily translated into technical problems.

- Why is the UI so slow ?
  - Why are the overall requests taking longer to respond ?
    - is it a server side issue ?, a database related issue ?, etc ...
      - if it's a server issue, what are the symptoms ?
        - higher CPU usage than usual ?
        - higher memory usage than usual ?
          - is it a memory leak ?
      - if it's a database issue, what are the symptoms ?
        - any particular query that is taking longer than it should ?
        - higher CPU usage than usual ?
        - higher memory usage than usual ?

And by following that structured line of thought, one should be able to identify the bottleneck and
the nature of the problem that is affecting the end user's experience, and by then, we can choose how
to solve it (logical optimization, do we need to scale because of the sheer amount of traffic ?, etc...)

> How would you manage database updates without downtime ?

As far as i understand, there's no such thing as "no downtime", it's more of a game of minimizing downtime,
to make it almost not noticeable.

If by "updates" you mean just running code migrations (creation of tables, adding new columns, etc..), you may
face issues if consumers are currently interacting with the tables/columns you are actively updating.

We can deal with that issue by making sure that migrations are executed before the code that makes use of said
migrations is deployed, thus greatly minimizing the window for potential issues.
