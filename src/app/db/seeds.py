INITIAL_DATA = { 
    'users': [
        {
            'username': 'Jan Guzman'
        },
        {
            'username': 'Wilowayne De La Cruz'
        },
    ],
    'tasks': [
        {
            'name': 'Bañar al perro',
            'desc': 'alguien tiene que hacerlo',
            'expires_at': '11-02-2025',
        },
        {
            'name': 'cortar el cesped',
            'desc': 'ha crecido demasiado',
            'expires_at': '10-14-2024',
        },
    ],
    'users2tasks': [
        {
            'user_id': 1,
            'task_id': 1,
        },
        {
            'user_id': 1,
            'task_id': 2,
        },
        {
            'user_id': 2,
            'task_id': 1,
        },
        {
            'user_id': 2,
            'task_id': 2,
        },
    ],
}

def initialize_table(target, connection, **kw):
    tablename = str(target)
    if tablename in INITIAL_DATA and len(INITIAL_DATA[tablename]) > 0:
        connection.execute(target.insert(), INITIAL_DATA[tablename])
