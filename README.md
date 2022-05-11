# API Serializers

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

In this task you will implement serializers and views for the following models:

1. `Genre`
2. `Actor`
3. `CinemaHall`
4. `Movie`
5. `MovieSession`

For every `<entity>` from `actors`, `genres`, `cinema_halls`, `movies`, `movie_sessions` such
endpoints should be implemented:
* `GET api/cinema/<entity>/` - should return a list of the all entity items
* `POST api/cinema/<entity>/` - should create a new entity based on passed data
* `GET api/cinema/<entity>/<pk>/` - should return an entity with given id
* `PUT api/cinema/<entity>/<pk>/` - should update the entity with given id based on passed data
* `DELETE api/cinema/<entity>/<pk>/` - should delete the entity with given id

Additional requirements:
1. For the list movie endpoint, genres and actors should be returned as lists of strings.
`"genres"` list should contain names of the genres, and the `"actors"` list should contain full names of actors and actresses.
Example:
```
GET api/cinema/movies/ 
```

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "title": "Harry Potter and the Philosopher's Stone",
        "description": "The first movie about Harry Potter",
        "duration": 210,
        "genres": [
            "drama"
        ],
        "actors": [
            "Emma Watson",
            "Daniel Radcliffe"
        ]
    }
]
```
2. At the same time movie detail endpoint should provide complete information about the genres and actors.

Example:
```
GET /api/cinema/movies/1/
```

```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "title": "Harry Potter and the Philosopher's Stone",
    "description": "The first movie about Harry Potter",
    "duration": 210,
    "genres": [
        {
            "id": 1,
            "name": "drama"
        }
    ],
    "actors": [
        {
            "id": 1,
            "first_name": "Emma",
            "last_name": "Watson",
            "full_name": "Emma Watson"
        },
        {
            "id": 2,
            "first_name": "Daniel",
            "last_name": "Radcliffe",
            "full_name": "Daniel Radcliffe"
        }
    ]
}
```

3. For `movies_session` list endpoint you should return the following information:
    * `"id"` - the id of the movie session;
    * `"show_time"` - the start time of the session
    * `"movie_title"` - the title of the movie
    * `"cinema_hall_name"` - the name of the cinema hall for the session
    * `"cinema_hall_capacity"` - the capacity of the cinema hall for the session

Example:
```
GET /api/cinema/movie_sessions/
```

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 2,
        "show_time": "2023-07-22T12:15:00Z",
        "movie_title": "Harry Potter and the Prisoner of Azkaban",
        "cinema_hall_name": "Green",
        "cinema_hall_capacity": 150
    },
    {
        "id": 1,
        "show_time": "2022-06-15T12:25:00Z",
        "movie_title": "Harry Potter and the Philosopher's Stone",
        "cinema_hall_name": "Black",
        "cinema_hall_capacity": 300
    }
]
```

4. At the same time for the movie session detail endpoint, complete information about the movie should be provided.

Example:
```
GET /api/cinema/movie_sessions/1/
```

```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "show_time": "2022-06-15T12:25:00Z",
    "movie": {
        "id": 1,
        "title": "Harry Potter and the Philosopher's Stone",
        "description": "The first movie about Harry Potter",
        "duration": 210,
        "genres": [
            "drama"
        ],
        "actors": [
            "Emma Watson",
            "Daniel Radcliffe"
        ]
    },
    "cinema_hall": {
        "id": 2,
        "name": "Black",
        "rows": 20,
        "seats_in_row": 15,
        "capacity": 300
    }
}
```


Hint: Use `ModelViewSet` to create views.
