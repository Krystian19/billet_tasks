INITIAL_DATA = { 
    'users': [
        {
            'username': 'Jan Guzman'
        },
        {
            'username': 'Wilowayne De La Cruz'
        },
    ]
}

def initialize_table(target, connection, **kw):
    tablename = str(target)
    if tablename in INITIAL_DATA and len(INITIAL_DATA[tablename]) > 0:
        connection.execute(target.insert(), INITIAL_DATA[tablename])
