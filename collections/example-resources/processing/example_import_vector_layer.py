"""
Name : Import vector into PostgreSQL database
Group : Example
Import a loaded vector layer into a PostgreSQL database.
"""

import random
import string
import sys

import processing
import psycopg2
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterBoolean
from qgis.core import QgsProcessingParameterCrs
from qgis.core import QgsProcessingParameterDatabaseSchema
from qgis.core import QgsProcessingParameterProviderConnection
from qgis.core import QgsProcessingParameterVectorLayer
from qgis.core import QgsWkbTypes
from PyQt5.QtCore import QCoreApplication


def start_connection(db_connection):
    try:
        connection = psycopg2.connect('', service="%s" % db_connection)
    except psycopg2.OperationalError:
        sys.exit(1)
    return connection


def check_name_validity(db_connection, db_schema, vector_layer, overwrite_existing_table):
    table_name = vector_layer.sourceName()
    sql = ''' SELECT EXISTS (SELECT FROM information_schema.tables WHERE  table_schema = '%s' AND    table_name   = '%s');  ''' % (
        db_schema, table_name)
    cursor = start_connection(db_connection).cursor()
    cursor.execute(sql)
    table_exists = cursor.fetchone()[0]

    if table_exists == 1 and overwrite_existing_table is True:
        new_table_name = table_name
    elif table_exists == 1 and overwrite_existing_table is False:
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(4))
        new_table_name = table_name + '_' + result_str
    else:
        new_table_name = table_name
    start_connection(db_connection).commit()
    cursor.close()
    start_connection(db_connection).close()
    return new_table_name


# Function to get the EPSG code from the layer already loaded in QGIS.
def check_epsg_code(vector_layer):
    eps_code = vector_layer.sourceCrs().authid()
    return eps_code


def append_records(db_connection, db_schema, vector_layer, append_bool):
    table_name = vector_layer.sourceName()
    sql = ''' SELECT EXISTS (SELECT FROM information_schema.tables WHERE  table_schema = '%s' AND    table_name   = '%s');  ''' % (
        db_schema, table_name)
    cursor = start_connection(db_connection).cursor()
    cursor.execute(sql)
    table_exists = cursor.fetchone()[0]
    if table_exists == 1 and append_bool is True:
        insert_records = 'True'
    else:
        insert_records = 'False'
    start_connection(db_connection).commit()
    cursor.close()
    start_connection(db_connection).close()
    return insert_records


def vector_dimensions(vector_layer):
    geom_type = QgsWkbTypes.displayString(vector_layer.wkbType())
    if geom_type[-2:] == 'ZM':
        vector_dimension = 2
    elif geom_type[-1:] == 'M' or geom_type[-1:] == 'Z':
        vector_dimension = 1
    else:
        vector_dimension = 0
    return vector_dimension


class SaveVectorToDatabase(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer('InputLayer', 'Input Vector Layer', defaultValue=None))
        self.addParameter(
            QgsProcessingParameterProviderConnection('Connection', 'Database Connection', 'postgres',
                                                     defaultValue='demo_db'))
        self.addParameter(
            QgsProcessingParameterDatabaseSchema('Project', 'Database Schema', connectionParameterName='Connection',
                                                 defaultValue='public'))
        self.addParameter(QgsProcessingParameterCrs('InputCRS', 'Input CRS', defaultValue='EPSG:4326'))
        self.addParameter(QgsProcessingParameterCrs('OutputCRS', 'Output CRS', defaultValue='EPSG:4326'))
        self.addParameter(
            QgsProcessingParameterBoolean('Overwritetable', 'Overwrite Existing Table', defaultValue=False))
        self.addParameter(QgsProcessingParameterBoolean('Append', 'Append To Existing Records', defaultValue=False))
        self.addParameter(
            QgsProcessingParameterBoolean('VERBOSE_LOG', 'Verbose logging', optional=False, defaultValue=True))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(1, model_feedback)
        results = {}
        outputs = {}

        # Export to PostgreSQL (available connections)
        alg_params = {
            'ADDFIELDS': append_records(self.parameterAsConnectionName(parameters, 'Connection', context),
                                        self.parameterAsSchema(parameters, 'Project', context),
                                        self.parameterAsSource(parameters, 'InputLayer', context),
                                        self.parameterAsBool(parameters, "Append", context)),
            'APPEND': append_records(self.parameterAsConnectionName(parameters, 'Connection', context),
                                     self.parameterAsSchema(parameters, 'Project', context),
                                     self.parameterAsSource(parameters, 'InputLayer', context),
                                     self.parameterAsBool(parameters, "Append", context)),
            'A_SRS': None,
            'CLIP': False,
            'DATABASE': parameters['Connection'],
            'DIM': vector_dimensions(self.parameterAsSource(parameters, 'InputLayer', context)),
            'GEOCOLUMN': 'geom',
            'GT': '',
            'GTYPE': 0,
            'INDEX': False,
            'INPUT': parameters['InputLayer'],
            'LAUNDER': False,
            'OPTIONS': '',
            'OVERWRITE': parameters['Overwritetable'],
            'PK': 'id',
            'PRECISION': True,
            'PRIMARY_KEY': '',
            'PROMOTETOMULTI': True,
            'SCHEMA': self.parameterAsSchema(parameters, 'Project', context),
            'SEGMENTIZE': '',
            'SHAPE_ENCODING': '',
            'SIMPLIFY': '',
            'SKIPFAILURES': False,
            'SPAT': None,
            'S_SRS': parameters['InputCRS'],
            'TABLE': check_name_validity(self.parameterAsConnectionName(parameters, 'Connection', context),
                                         self.parameterAsSchema(parameters, 'Project', context),
                                         self.parameterAsSource(parameters, 'InputLayer', context),
                                         parameters['Overwritetable']),
            'T_SRS': parameters['OutputCRS'],
            'WHERE': ''
        }
        # print(alg_params)
        outputs['ExportToPostgresqlAvailableConnections'] = processing.run(
            'gdal:importvectorintopostgisdatabaseavailableconnections', alg_params, context=context, feedback=feedback,
            is_child_algorithm=True)
        return results

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return self.tr(
            "Import Vector layers into PostgreSQL Database using Ogr2ogr \n\
            <mark style='color:blue'><strong>Algorithm Parameters</strong></mark>\n\
            <i>\n* <mark style='color:black'><strong>Input Layer</strong></mark> - Loaded QGIS layer or OGR vector layer.\
            \n* <mark style='color:black'><strong>Connection</strong></mark> - PostgreSQL connection name. Must be a PostgreSQL service name.\
            \n* <mark style='color:black'><strong>Project</strong></mark> - Schema name where you need to import the vector layer into.\
            \n* <mark style='color:black'><strong>Input CRS</strong></mark> - CRS of the input layer.\
            \n* <mark style='color:black'><strong>Output CRS</strong></mark> - CRS of the layers once its imported into the database. Useful if you need to reproject your data\
            \n* <mark style='color:black'><strong>Overwrite existing table</strong></mark> - Boolean flag to indicate whether you need to overwrite an existing table in the database. This is true is the name of your vector matches the table in the database\
            \n* <mark style='color:black'><strong>Append to existing table</strong></mark> - Useful if you need to create a seamless layer i.e joining a roads layer from different municipalities to create a single road layer. If the table structure for the existing table and input table are different extra column will be created in the database table.\
            \n* <mark style='color:black'><strong>Verbose logging</strong></mark> - Allows users to see what command was generated by the algorithm\n\
            <mark style='color:black'><strong>NOTE</strong></mark>\n\
            <mark style='color:black'>The algorithm does some basic validation for table names. If a table already exists in the DB with the same name as the input layer it will check other flags ie <mark style='color:black'><strong>Overwrite</strong></mark> or <mark style='color:black'><strong>Append to existing table</strong></mark> and perfom the operation based on those inputs. If the <mark style='color:black'><strong>overwrite</strong></mark> or <mark style='color:black'><strong>Append to existing table</strong></mark> flags are not on and a table with the same name already exists then a new table is created suffixed by some random four letters i.e: 'roads_xyz'</mark>. It is the responsibility of the user to change the name in the DB\n\
            "
        )

    def name(self):
        return 'Import vector into PostgreSQL database'

    def displayName(self):
        return 'Import vector into PostgreSQL database'

    def group(self):
        return 'Example'

    def groupId(self):
        return 'Example'

    def createInstance(self):
        return SaveVectorToDatabase()
