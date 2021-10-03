# import our modules
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# Build the request framework
transport = RequestsHTTPTransport(url='http://localhost:8000/graphql', use_json=True)

# Create the client
client = Client(transport=transport, fetch_schema_from_transport=True)
        
# define a simple query
query = gql('''
mutation createNewPost{
    createNewPost(title:"new title 4",content:"new content 4"){
        ok
    }
}
''')

# execute and print this query
print(client.execute(query))

query = gql('''
{
    allPosts{
        title
        timeCreated
    }
}
''')

# execute and print this query
print(client.execute(query))