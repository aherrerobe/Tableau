from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils.querying import get_projects_dataframe


TS_CONFIG = {
        'my_env': {
                'server': 'https://YourTableauServer.com',
                'api_version': '<YOUR_API_VERSION>',
                'username': '<YOUR_USERNAME>',
                'password': '<YOUR_PASSWORD>',
                'site_name': '<YOUR_SITE_NAME>',
                'site_url': '<YOUR_SITE_CONTENT_URL>'
        }
}


conn = TableauServerConnection(config_json=TS_CONFIG, env='test_env')
conn.sign_in()

#  uncomment the two lines of code below to output details of your available Tableau Server projects
# projects_df = get_projects_df(conn)
# print(projects_df)

#  publish a data source without embedding credentials
response = conn.publish_data_source(datasource_file_path='FILE_PATH_TO_TDSX_FILE',
                                    datasource_name='YOUR_DATA_SOURCE_NAME',
                                    project_id='YOUR_PROJECT_ID')
print(response.json())

#  publish a data source with embedded credentials
response = conn.publish_data_source(datasource_file_path='FILE_PATH_TO_TDSX_FILE',
                                    datasource_name='YOUR_DATA_SOURCE_NAME',
                                    project_id='YOUR_PROJECT_ID',
                                    embed_credentials_flag=True,
                                    connection_username='YOUR_USERNAME',
                                    connection_password='YOUR_PASSWORD')
print(response.json())

conn.sign_out()
