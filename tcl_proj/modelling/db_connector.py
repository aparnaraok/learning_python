import csv
import logging
import logging.config
from param_parser import ParseJson

logging.config.fileConfig("logging.conf")
# create logger
logger = logging.getLogger("modelLogger")

class DbConnector:
    def __init__(self):
        '''Initializing
        '''
        logging.info("=" * 50)
        logging.info("Fetching the database connectivity details ....")
        logging.info("=" * 50)
        # self.json_data = ParseJson().load_json_content()

    def get_db_creds(self, json_data):
        '''Returns the DB credentials
        '''
        db_conn_list = []
        for key in json_data["parameters"]:
            if key == "fetch_conn":
                if (json_data["parameters"][key]["read_from_file"]):
                    conn_properties = json_data["parameters"][key]["file_properties"]
                    for connections in conn_properties:
                        for conn in conn_properties[connections]:
                            if conn["read_mode"]:
                                db_file_name = conn["file_name"]
                                db_file_path = os.path.join(os.getcwd(), "db_creds", db_file_name)
                                with open(db_file_path, "r") as csv_file:
                                    csv_reader = csv.reader(csv_file, delimiter=',')
                                    next(csv_reader)
                                    for row in csv_reader:
                                        name = row[0]
                                        host_name = row[1]
                                        port = row[2]
                                        db_type = row[3]
                                        db_name = row[4]
                                        username = row[5]
                                        password = row[6]

                                        db_conn_list.append((name, host_name, port, db_type, db_name, username, password
                                                             ))
                elif (json_data["parameters"][key]["read_from_db"]):
                    conn_details = json_data["parameters"][key]["db_properties"]
                    for connections in conn_details:
                        for conn in conn_details[connections]:
                            if conn["enabled"]:
                                name = conn["name"]
                                host_name = conn["hostname"]
                                port = conn["port"]
                                db_type = conn["database_type"]
                                db_name = conn["database_name"]
                                username = conn["username"]
                                password = conn["password"]
                                db_conn_list.append((name, host_name, port, db_type, db_name, username, password))
                else:
                    logging.error("Please set the read_mode for any of the database / file to true in config JSON file")

        if len(db_conn_list) > 1:
            db_conn_list = db_conn_list[0]
        else:
            db_conn_list = db_conn_list
        logging.info("Selected Database  : : %s ", db_conn_list)

        if not(db_conn_list):
            logging.error("Please make sure that you have enabled the read mode (file / DB)  for DB conn details fetch...")

        return db_conn_list

# db_connector = DbConnector()
# a = db_connector.get_db_creds()
