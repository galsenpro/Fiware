#
# Copyright 2015 Telefonica Investigacion y Desarrollo, S.A.U
#
# This file is part of IoT orchestrator
#
# IoT orchestrator is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# IoT orchestrator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with IoT orchestrator. If not, see http://www.gnu.org/licenses/.
#
# For those usages not covered by this license please contact with
# iot_support at tid dot es
#
# Author: IoT team
#
import json

from orchestrator.core.flow.base import FlowBase
from orchestrator.common.util import CSVOperations
from orchestrator.common.util import ContextFilterService
from orchestrator.common.util import ContextFilterSubService
from settings.dev import IOTMODULES


class Projects(FlowBase):

    def projects(self,
                 DOMAIN_ID,
                 DOMAIN_NAME,
                 ADMIN_USER,
                 ADMIN_PASSWORD,
                 ADMIN_TOKEN):

        '''Get Projects of a domain.

        In case of HTTP error, return HTTP error

        Params:
        - DOMAIN_ID: id of domain
        - DOMAIN_NAME: name of domain
        - SERVICE_ADMIN_USER: Service admin username
        - SERVICE_ADMIN_PASSWORD: Service admin password
        - SERVICE_ADMIN_TOKEN: Service admin token
        Return:
        - project array list
        '''
        data_log = {
            "DOMAIN_ID": "%s" % DOMAIN_ID,
            "DOMAIN_NAME": "%s" % DOMAIN_NAME,
            "ADMIN_USER": "%s" % ADMIN_USER,
            "ADMIN_PASSWORD": "%s" % ADMIN_PASSWORD,
            "ADMIN_TOKEN": self.get_extended_token(ADMIN_TOKEN)
        }
        self.logger.debug("FLOW projects invoked with: %s" % json.dumps(
            data_log, indent=3)
        )
        try:
            if not ADMIN_TOKEN:
                if not DOMAIN_ID:
                    ADMIN_TOKEN = self.idm.getToken(DOMAIN_NAME,
                                                    ADMIN_USER,
                                                    ADMIN_PASSWORD)
                    DOMAIN_ID = self.idm.getDomainId(ADMIN_TOKEN,
                                                     DOMAIN_NAME)

                else:
                    ADMIN_TOKEN = self.idm.getToken2(DOMAIN_ID,
                                                     ADMIN_USER,
                                                     ADMIN_PASSWORD)
            self.logger.debug("ADMIN_TOKEN=%s" % ADMIN_TOKEN)

            # Ensure DOMAIN_NAME and PROJECT_NAME
            DOMAIN_NAME = self.ensure_service_name(ADMIN_TOKEN,
                                                   DOMAIN_ID,
                                                   DOMAIN_NAME)
            self.logger.addFilter(ContextFilterService(DOMAIN_NAME))

            PROJECTS = self.idm.getDomainProjects(ADMIN_TOKEN,
                                                  DOMAIN_ID)

            self.logger.debug("PROJECTS=%s" % json.dumps(PROJECTS, indent=3))

        except Exception, ex:
            self.logger.error(ex)
            return self.composeErrorCode(ex)

        data_log = {
            "PROJECTS": PROJECTS
        }
        self.logger.info("Summary report : %s" % json.dumps(data_log, indent=3))

        # Consolidate opetions metrics into flow metrics
        self.collectComponentMetrics()

        return PROJECTS, DOMAIN_NAME, None

    def get_project(self,
                    DOMAIN_ID,
                    DOMAIN_NAME,
                    PROJECT_ID,
                    ADMIN_USER,
                    ADMIN_PASSWORD,
                    ADMIN_TOKEN):

        '''Ge Project detail of a domain

        In case of HTTP error, return HTTP error

        Params:
        - DOMAIN_ID: id of domain
        - DOMAIN_NAME: name of domain
        - PROJECT_ID: id of project
        - SERVICE_ADMIN_USER: Service admin username
        - SERVICE_ADMIN_PASSWORD: Service admin password
        - SERVICE_ADMIN_TOKEN: Service admin token
        Return:
        - project detail
        '''
        data_log = {
            "DOMAIN_ID": "%s" % DOMAIN_ID,
            "DOMAIN_NAME": "%s" % DOMAIN_NAME,
            "PROJECT_ID": "%s" % PROJECT_ID,
            "ADMIN_USER": "%s" % ADMIN_USER,
            "ADMIN_PASSWORD": "%s" % ADMIN_PASSWORD,
            "ADMIN_TOKEN": self.get_extended_token(ADMIN_TOKEN)
        }
        self.logger.debug("FLOW get_project invoked with: %s" % json.dumps(
            data_log,
            indent=3)
        )
        try:
            if not ADMIN_TOKEN:
                ADMIN_TOKEN = self.idm.getToken2(DOMAIN_ID,
                                                 ADMIN_USER,
                                                 ADMIN_PASSWORD)
            self.logger.debug("ADMIN_TOKEN=%s" % ADMIN_TOKEN)

            # Ensure DOMAIN_NAME and PROJECT_NAME
            DOMAIN_NAME = self.ensure_service_name(ADMIN_TOKEN,
                                                   DOMAIN_ID,
                                                   DOMAIN_NAME)
            self.logger.addFilter(ContextFilterService(DOMAIN_NAME))

            PROJECT_NAME = self.ensure_subservice_name(ADMIN_TOKEN,
                                                       DOMAIN_ID,
                                                       PROJECT_ID,
                                                       None)
            self.logger.addFilter(ContextFilterSubService(PROJECT_NAME))

            # PROJECTS = self.idm.getDomainProjects(ADMIN_TOKEN,
            #                                       DOMAIN_ID)
            # for project in PROJECTS:
            #     if project['id'] == PROJECT_ID:
            #         PROJECT = project

            try:
                PROJECT = self.idm.getProject(ADMIN_TOKEN, PROJECT_ID)
            except Exception, ex:
                PROJECT = {
                    'project': {
                        'description': PROJECT_NAME,
                        'domain_id': DOMAIN_ID,
                        'id': PROJECT_ID,
                        'name': '/' + PROJECT_NAME
                    }
                }
            self.logger.debug("PROJECT=%s" % PROJECT)

        except Exception, ex:
            self.logger.error(ex)
            return self.composeErrorCode(ex)

        data_log = {
            "PROJECT": PROJECT
        }
        self.logger.info("Summary report : %s" % json.dumps(data_log, indent=3))

        # Consolidate opetions metrics into flow metrics
        self.collectComponentMetrics()

        return PROJECT, DOMAIN_NAME, PROJECT_NAME

    def update_project(self,
                       DOMAIN_ID,
                       DOMAIN_NAME,
                       PROJECT_ID,
                       PROJECT_NAME,
                       ADMIN_USER,
                       ADMIN_PASSWORD,
                       ADMIN_TOKEN,
                       NEW_SUBSERVICE_DESCRIPTION):

        '''Update Project detail of a domain

        In case of HTTP error, return HTTP error

        Params:
        - DOMAIN_ID: id of domain
        - DOMAIN_NAME: name of domain
        - PROJECT_ID: id of project
        - PROJECT_NAME: name of project
        - SERVICE_ADMIN_USER: Service admin username
        - SERVICE_ADMIN_PASSWORD: Service admin password
        - SERVICE_ADMIN_TOKEN: Service admin token
        - NEW_SUBSERVICE_DESCRIPTION: New subservice description
        Return:
        - project detail
        '''
        data_log = {
            "DOMAIN_ID": "%s" % DOMAIN_ID,
            "DOMAIN_NAME": "%s" % DOMAIN_NAME,
            "PROJECT_ID": "%s" % PROJECT_ID,
            "PROJECT_NAME": "%s" % PROJECT_NAME,
            "ADMIN_USER": "%s" % ADMIN_USER,
            "ADMIN_PASSWORD": "%s" % ADMIN_PASSWORD,
            "ADMIN_TOKEN": self.get_extended_token(ADMIN_TOKEN),
            "NEW_SUBSERVICE_DESCRIPTION": "%s" % NEW_SUBSERVICE_DESCRIPTION,
        }
        self.logger.debug("FLOW update_project invoked with: %s" % json.dumps(
            data_log,
            indent=3)
        )
        try:
            if not ADMIN_TOKEN:
                if not DOMAIN_ID:
                    ADMIN_TOKEN = self.idm.getToken(DOMAIN_NAME,
                                                    ADMIN_USER,
                                                    ADMIN_PASSWORD)
                    DOMAIN_ID = self.idm.getDomainId(ADMIN_TOKEN,
                                                     DOMAIN_NAME)
                else:
                    ADMIN_TOKEN = self.idm.getToken2(DOMAIN_ID,
                                                     ADMIN_USER,
                                                     ADMIN_PASSWORD)
            self.logger.debug("ADMIN_TOKEN=%s" % ADMIN_TOKEN)

            # Ensure DOMAIN_NAME and PROJECT_NAME
            DOMAIN_NAME = self.ensure_service_name(ADMIN_TOKEN,
                                                   DOMAIN_ID,
                                                   DOMAIN_NAME)
            self.logger.addFilter(ContextFilterService(DOMAIN_NAME))

            if not PROJECT_ID:
                PROJECT_ID = self.idm.getProjectId(ADMIN_TOKEN,
                                                   DOMAIN_NAME,
                                                   PROJECT_NAME)
            PROJECT_NAME = self.ensure_subservice_name(ADMIN_TOKEN,
                                                       DOMAIN_ID,
                                                       PROJECT_ID,
                                                       PROJECT_NAME)
            self.logger.addFilter(ContextFilterSubService(PROJECT_NAME))

            PROJECT = self.idm.updateProject(ADMIN_TOKEN,
                                             DOMAIN_ID,
                                             PROJECT_ID,
                                             NEW_SUBSERVICE_DESCRIPTION)

            self.logger.debug("PROJECT=%s" % PROJECT)

        except Exception, ex:
            self.logger.error(ex)
            return self.composeErrorCode(ex)

        data_log = {
            "PROJECT": PROJECT
        }
        self.logger.info("Summary report : %s" % json.dumps(data_log, indent=3))

        # Consolidate opetions metrics into flow metrics
        self.collectComponentMetrics()

        return PROJECT, DOMAIN_NAME, PROJECT_NAME

    def delete_project(self,
                       DOMAIN_ID,
                       DOMAIN_NAME,
                       PROJECT_ID,
                       PROJECT_NAME,
                       ADMIN_USER,
                       ADMIN_PASSWORD,
                       ADMIN_TOKEN):

        '''Delete Project of domain

        In case of HTTP error, return HTTP error

        Params:
        - DOMAIN_ID: id of domain
        - DOMAIN_NAME: name of domain
        - PROJECT_ID: id of project
        - PROJECT_NAME: name of project
        - SERVICE_ADMIN_USER: Service admin username
        - SERVICE_ADMIN_PASSWORD: Service admin password
        - SERVICE_ADMIN_TOKEN: Service admin token
        '''
        data_log = {
            "DOMAIN_ID": "%s" % DOMAIN_ID,
            "DOMAIN_NAME": "%s" % DOMAIN_NAME,
            "PROJECT_ID": "%s" % PROJECT_ID,
            "PROJECT_NAME": "%s" % PROJECT_NAME,
            "ADMIN_USER": "%s" % ADMIN_USER,
            "ADMIN_PASSWORD": "%s" % ADMIN_PASSWORD,
            "ADMIN_TOKEN": self.get_extended_token(ADMIN_TOKEN)
        }
        self.logger.debug("FLOW get_project invoked with: %s" % json.dumps(
            data_log,
            indent=3)
        )
        try:

            if not ADMIN_TOKEN:
                if not DOMAIN_ID:
                    ADMIN_TOKEN = self.idm.getToken(DOMAIN_NAME,
                                                    ADMIN_USER,
                                                    ADMIN_PASSWORD)
                    DOMAIN_ID = self.idm.getDomainId(ADMIN_TOKEN,
                                                     DOMAIN_NAME)
                else:
                    ADMIN_TOKEN = self.idm.getToken2(DOMAIN_ID,
                                                     ADMIN_USER,
                                                     ADMIN_PASSWORD)

            # Ensure DOMAIN_NAME and PROJECT_NAME
            DOMAIN_NAME = self.ensure_service_name(ADMIN_TOKEN,
                                                   DOMAIN_ID,
                                                   DOMAIN_NAME)
            self.logger.addFilter(ContextFilterService(DOMAIN_NAME))

            if not PROJECT_ID:
                PROJECT_ID = self.idm.getProjectId(ADMIN_TOKEN,
                                                   DOMAIN_NAME,
                                                   PROJECT_NAME)

            PROJECT_NAME = self.ensure_subservice_name(ADMIN_TOKEN,
                                                       DOMAIN_ID,
                                                       PROJECT_ID,
                                                       PROJECT_NAME)
            self.logger.addFilter(ContextFilterSubService(PROJECT_NAME))

            self.logger.debug("DOMAIN_NAME=%s" % DOMAIN_NAME)
            self.logger.debug("PROJECT_NAME=%s" % PROJECT_NAME)
            self.logger.debug("ADMIN_TOKEN=%s" % ADMIN_TOKEN)

            #
            # Delete all devices
            #
            devices_deleted = self.iota.deleteAllDevices(ADMIN_TOKEN,
                                                         DOMAIN_NAME,
                                                         PROJECT_NAME)
            if (len(devices_deleted) > 0):
                self.logger.info("devices deleted %s", devices_deleted)


            #
            # Delete all subscriptions
            #
            subscriptions_deleted = self.cb.deleteAllSubscriptions(
                                                              ADMIN_TOKEN,
                                                              DOMAIN_NAME,
                                                              PROJECT_NAME)
            if (len(subscriptions_deleted) > 0):
                self.logger.info("subscriptions deleted %s",
                                 subscriptions_deleted)

            #
            # Delete all rules in a subservice
            #
            rules_deleted = self.perseo.deleteAllRules(ADMIN_TOKEN,
                                                       DOMAIN_NAME,
                                                       PROJECT_NAME)
            if (len(rules_deleted) > 0):
                self.logger.info("rules deleted %s",
                                 rules_deleted)

            PROJECT = self.idm.disableProject(ADMIN_TOKEN,
                                              DOMAIN_ID,
                                              PROJECT_ID)

            self.idm.deleteProject(ADMIN_TOKEN,
                                   PROJECT_ID)

            self.logger.debug("PROJECT=%s" % PROJECT)

        except Exception, ex:
            self.logger.error(ex)
            return self.composeErrorCode(ex)

        data_log = {
            "PROJECT": PROJECT
        }
        self.logger.info("Summary report : %s" % json.dumps(data_log,
                                                       indent=3))

        # Consolidate opetions metrics into flow metrics
        self.collectComponentMetrics()

        return PROJECT, DOMAIN_NAME, PROJECT_NAME


    def register_service(self,
                         DOMAIN_NAME,
                         DOMAIN_ID,
                         PROJECT_NAME,
                         PROJECT_ID,
                         SERVICE_USER_NAME,
                         SERVICE_USER_PASSWORD,
                         SERVICE_USER_TOKEN,
                         ENTITY_TYPE,
                         ENTITY_ID,
                         PROTOCOL,
                         ATT_NAME,
                         ATT_PROVIDER,
                         ATT_ENDPOINT,
                         ATT_METHOD,
                         ATT_AUTHENTICATION,
                         ATT_INTERACTION_TYPE,
                         ATT_MAPPING,
                         ATT_TIMEOUT
                       ):

        '''Register entity Service (in CB)

        In case of HTTP error, return HTTP error

        Params:
        - DOMAIN_ID: id of domain
        - DOMAIN_NAME: name of domain
        - PROJECT_ID: id of project
        - PROJECT_NAME: name of project
        - SERVICE_USER_NAME: Service admin username
        - SERVICE_USER_PASSWORD: Service admin password
        - SERVICE_USER_TOKEN: Service admin token
        - ENTITY_TYPE:   (optional, just for Device configuration)
        - ENTITY_ID:
        - PROTOCOL:
        - ATT_NAME
        - ATT_PROVIDER
        - ATT_ENDPOINT
        - ATT_METHOD
        - ATT_AUTHENTICATION
        - ATT_INTERACTION_TYPE
        - ATT_MAPPING
        - ATT_TIMEOUT
        '''
        data_log = {
            "DOMAIN_ID": "%s" % DOMAIN_ID,
            "DOMAIN_NAME": "%s" % DOMAIN_NAME,
            "PROJECT_ID": "%s" % PROJECT_ID,
            "PROJECT_NAME": "%s" % PROJECT_NAME,
            "SERVICE_USER_NAME": "%s" % SERVICE_USER_NAME,
            "SERVICE_USER_PASSWORD": "%s" % SERVICE_USER_PASSWORD,
            "SERVICE_USER_TOKEN": self.get_extended_token(SERVICE_USER_TOKEN),
            "ENTITY_TYPE": "%s" % ENTITY_TYPE,
            "ENTITY_ID": "%s" % ENTITY_ID,
            "PROTOCOL": "%s" % PROTOCOL,
            "ATT_NAME": "%s" % ATT_NAME,
            "ATT_PROVIDER": "%s" % ATT_PROVIDER,
            "ATT_ENDPOINT": "%s" % ATT_ENDPOINT,
            "ATT_METHOD": "%s" % ATT_METHOD,
            "ATT_AUTHENTICATION": "%s" % ATT_AUTHENTICATION,
            "ATT_INTERACTION_TYPE": "%s" % ATT_INTERACTION_TYPE,
            "ATT_MAPPING": "%s" % ATT_MAPPING,
            "ATT_TIMEOUT": "%s" % ATT_TIMEOUT
        }
        self.logger.debug("FLOW register_service invoked with: %s" % json.dumps(
            data_log,
            indent=3)
        )
        try:
            if not SERVICE_USER_TOKEN:
                if not DOMAIN_ID:
                    SERVICE_USER_TOKEN = self.idm.getScopedProjectToken(
                        DOMAIN_NAME,
                        PROJECT_NAME,
                        SERVICE_USER_NAME,
                        SERVICE_USER_PASSWORD)
                    DOMAIN_ID = self.idm.getDomainId(SERVICE_USER_TOKEN,
                                                     DOMAIN_NAME)
                    PROJECT_ID = self.idm.getProjectId(SERVICE_USER_TOKEN,
                                                        DOMAIN_NAME,
                                                        PROJECT_NAME)

                else:
                    SERVICE_USER_TOKEN = self.idm.getScopedProjectToken2(
                        DOMAIN_ID,
                        PROJECT_ID,
                        SERVICE_USER_NAME,
                        SERVICE_USER_PASSWORD)
            # Ensure DOMAIN_NAME and PROJECT_NAME
            DOMAIN_NAME = self.ensure_service_name(SERVICE_USER_TOKEN,
                                                   DOMAIN_ID,
                                                   DOMAIN_NAME)
            self.logger.addFilter(ContextFilterService(DOMAIN_NAME))

            PROJECT_NAME = self.ensure_subservice_name(SERVICE_USER_TOKEN,
                                                       DOMAIN_ID,
                                                       PROJECT_ID,
                                                       PROJECT_NAME)
            self.logger.addFilter(ContextFilterSubService(PROJECT_NAME))

            self.logger.debug("DOMAIN_NAME=%s" % DOMAIN_NAME)
            self.logger.debug("PROJECT_NAME=%s" % PROJECT_NAME)
            self.logger.debug("SERVICE_USER_TOKEN=%s" % SERVICE_USER_TOKEN)


            if not PROJECT_ID:
                PROJECT_ID = self.idm.getProjectId(SERVICE_USER_TOKEN,
                                                   DOMAIN_NAME,
                                                   PROJECT_NAME)
            #
            # 1. Subscribe Context Adapter in ContextBroker
            #
            DURATION="P1Y"
            REFERENCE_URL="http://localhost"
            ENTITIES=[]
            ATTRIBUTES = []
            NOTIFY_CONDITIONS = []

            if PROTOCOL == "TT_BLACKBUTTON":
                DEVICE_ENTITY_TYPE="BlackButton"
                REFERENCE_URL = self.ca_endpoint  #"http://<ip_ca>:<port_ca>/v1/notify"
                ENTITIES = [
                    {
                        "type": DEVICE_ENTITY_TYPE,
                        "isPattern": "true",
                        "id": ".*"
                    }
                ]
                ATTRIBUTES=[
                    "op_action",
                    "op_extra",
                    "op_status",
                    "interaction_type",
                    "service_id",
                    "TimeInstant"
                ]
                NOTIFY_CONDITIONS = [
                    {
                        "type": "ONCHANGE",
                        "condValues": [
                            "op_action"
                        ]
                    }
                ]
            self.logger.debug("Trying to subscribe CA in CB...")
            cb_res = self.cb.subscribeContext(
                SERVICE_USER_TOKEN,
                DOMAIN_NAME,
                PROJECT_NAME,
                REFERENCE_URL,
                DURATION,
                ENTITIES,
                ATTRIBUTES,
                NOTIFY_CONDITIONS
            )
            self.logger.debug("subscribeContext res=%s" % json.dumps(cb_res,
                                                                     indent=3))
            subscriptionid_ca = cb_res['subscribeResponse']['subscriptionId']
            self.logger.debug("subscription id ca=%s" % subscriptionid_ca)

            #
            # 2. Register Entity Service in CB
            #
            IS_PATTERN="false"
            ACTION="APPEND"
            ATTRIBUTES=[]
            STATIC_ATTRIBUTES=[]

            if ATT_NAME and ATT_NAME != "":
                STATIC_ATTRIBUTES.append(
                    {
                        "name": "name",
                        "type": "string",
                        "value": ATT_NAME
                    })
            if ATT_PROVIDER and ATT_PROVIDER != "":
                STATIC_ATTRIBUTES.append(
                    {
                        "name": "provider",
                        "type": "string",
                        "value": ATT_PROVIDER
                    })
            if ATT_ENDPOINT and ATT_ENDPOINT != "":
                STATIC_ATTRIBUTES.append(
                    {
                        "name": "endpoint",
                        "type": "string",
                        "value": ATT_ENDPOINT
                    })
            if ATT_METHOD and ATT_METHOD != "":
                STATIC_ATTRIBUTES.append(
                    {
                        "name": "method",
                        "type": "string",
                        "value": ATT_METHOD
                    })
            if ATT_AUTHENTICATION and ATT_AUTHENTICATION != "":
                STATIC_ATTRIBUTES.append(
                    {
                        "name": "authentication",
                        "type": "string",
                        "value": ATT_AUTHENTICATION
                    })
            if ATT_INTERACTION_TYPE and ATT_INTERACTION_TYPE != "":
                STATIC_ATTRIBUTES.append(
                    {
                        "name": "interaction_type",
                        "type": "string",
                        "value": ATT_INTERACTION_TYPE
                    })
            if ATT_MAPPING and ATT_MAPPING != "":
                STATIC_ATTRIBUTES.append(
                    {
                        "name": "mapping",
                        "type": "string",
                        "value": ATT_MAPPING
                    })
            if ATT_TIMEOUT and ATT_TIMEOUT != "":
                STATIC_ATTRIBUTES.append(
                    {
                        "name": "timeout",
                        "type": "integer",
                        "value": ATT_TIMEOUT
                    })

            # call CB
            self.logger.debug("Trying to register service entity in CB...")
            cb_res = self.cb.updateContext(SERVICE_USER_TOKEN,
                                           DOMAIN_NAME,
                                           PROJECT_NAME,
                                           ENTITY_TYPE,
                                           ENTITY_ID,
                                           ACTION,
                                           IS_PATTERN,
                                           STATIC_ATTRIBUTES
                                        )

            self.logger.debug("updateContext res=%s" % json.dumps(cb_res,
                                                                  indent=3))

            for r in cb_res['contextResponses']:
                # Check ContextBroker status response
                if r['statusCode']['code'] != '200':
                    raise Exception(r['statusCode']['reasonPhrase'])

            self.logger.debug("ENTITY_ID=%s" % ENTITY_ID)


            #
            # Subscribe commons
            #
            DURATION="P1Y"
            ENTITIES=[]
            ATTRIBUTES=[]
            NOTIFY_CONDITIONS=[]
            REFERENCE_URL="http://localhost"
            if PROTOCOL == "TT_BLACKBUTTON":
                ENTITY_TYPE="BlackButton"
                ENTITIES = [
                    {
                        "type": ENTITY_TYPE,
                        "isPattern": "true",
                        "id": ".*"
                    }
                ]
                ATTRIBUTES=[
                        "internal_id",
                        "last_operation",
                        "op_status",
                        "op_result",
                        "op_action",
                        "op_extra",
                        "sleepcondition",
                        "sleeptime",
                        "iccid",
                        "imei",
                        "imsi",
                        "interaction_type",
                        "service_id",
                        "geolocation"

                ]
                NOTIFY_CONDITIONS = [
                    {
                        "type": "ONCHANGE",
                        "condValues": [
                            "op_status",  # reduntant?
                            "TimeInstant"
                        ]
                    }
                ]

            if PROTOCOL == "PDI-IoTA-ThinkingThings":
                ENTITY_TYPE="Thing"
                ENTITIES = [
                    {
                        "type": ENTITY_TYPE,
                        "isPattern": "true",
                        "id": ".*"
                    }
                ]
                ATTRIBUTES=[
                    "mcc",
                    "mnc"
                    "lac"
                    "cellid",
                    "dbm",
                    "temperature",
                    "humidity",
                    "luminance",
                    "voltage",
                    "state",
                    "charger"
                    "charging",
                    "mode",
                    "desconnection",
                    "sleepcondition",
                    "color",
                    "melody",
                    "sleeptime",
                ]
                NOTIFY_CONDITIONS = [
                    {
                        "type": "ONCHANGE",
                        "condValues": [
                            "humidity",
                            "temperature",
                            "state"
                        ]
                    }
                ]

            #
            # 3.2 Subscribe Short Term Historic (STH)
            #
            REFERENCE_URL = "http://localhost"
            if PROTOCOL == "TT_BLACKBUTTON":
                REFERENCE_URL = self.get_endpoint_iot_module('STH')

            if PROTOCOL == "PDI-IoTA-ThinkingThings":
                REFERENCE_URL = self.get_endpoint_iot_module('STH')

            self.logger.debug("Trying to subscribe STH...")
            if len(ENTITIES) > 0:
                cb_res = self.cb.subscribeContext(
                    SERVICE_USER_TOKEN,
                    DOMAIN_NAME,
                    PROJECT_NAME,
                    REFERENCE_URL,
                    DURATION,
                    ENTITIES,
                    ATTRIBUTES,
                    NOTIFY_CONDITIONS
                    )
                self.logger.debug("subscribeContext res=%s" % json.dumps(cb_res,
                                                                         indent=3))
                subscriptionid_sth = cb_res['subscribeResponse']['subscriptionId']
                self.logger.debug("registration id sth=%s" % subscriptionid_sth)


            #
            # 3.3 Perseo
            #
            REFERENCE_URL = "http://localhost"
            if PROTOCOL == "TT_BLACKBUTTON":
                REFERENCE_URL = self.get_endpoint_iot_module('PERSEO')


            if PROTOCOL == "PDI-IoTA-ThinkingThings":
                REFERENCE_URL = self.get_endpoint_iot_module('PERSEO')

            self.logger.debug("Trying to subscribe PERSEO...")
            if len(ENTITIES) > 0:
                cb_res = self.cb.subscribeContext(
                    SERVICE_USER_TOKEN,
                    DOMAIN_NAME,
                    PROJECT_NAME,
                    REFERENCE_URL,
                    DURATION,
                    ENTITIES,
                    ATTRIBUTES,
                    NOTIFY_CONDITIONS
                    )
                self.logger.debug("subscribeContext res=%s" % json.dumps(cb_res, indent=3))
                subscriptionid_perseo = cb_res['subscribeResponse']['subscriptionId']
                self.logger.debug("registration id perseo=%s" % subscriptionid_perseo)


        except Exception, ex:
            self.logger.error(ex)
            return self.composeErrorCode(ex)

        data_log = {
            "ENTITY_ID": ENTITY_ID,
            "subscriptionid_ca": subscriptionid_ca,
            "subscriptionid_sth": subscriptionid_sth,
            "subscriptionid_perseo": subscriptionid_perseo
        }
        self.logger.info("Summary report : %s" % json.dumps(data_log,
                                                       indent=3))
        result = {
            "subscriptionid_ca": subscriptionid_ca,
            "subscriptionid_sth": subscriptionid_sth,
            "subscriptionid_perseo": subscriptionid_perseo
        }

        # Consolidate opetions metrics into flow metrics
        self.collectComponentMetrics()

        return result, DOMAIN_NAME, PROJECT_NAME


    def register_device(self,
                        DOMAIN_NAME,
                        DOMAIN_ID,
                        PROJECT_NAME,
                        PROJECT_ID,
                        SERVICE_USER_NAME,
                        SERVICE_USER_PASSWORD,
                        SERVICE_USER_TOKEN,
                        DEVICE_ID,
                        ENTITY_TYPE,
                        ENTITY_NAME,
                        PROTOCOL,
                        ATT_ICCID,
                        ATT_IMEI,
                        ATT_IMSI,
                        ATT_INTERACTION_TYPE,
                        ATT_SERVICE_ID,
                        ATT_GEOLOCATION
                        ):

        '''Register Device in IOTA

        In case of HTTP error, return HTTP error

        Params:
        - DOMAIN_NAME: Service name
        - DOMAIN_ID: Service id
        - PROJECT_NAME: SubService name
        - PROJECT_ID: SubService name
        - SERVICE_USER_NAME: Service admin username
        - SERVICE_USER_PASSWORD: Service admin password
        - SERVICE_USER_TOKEN: Service admin token
        - DEVICE_ID: Device ID
        - ENTITY_TYPE: Entity Type
        - ENTITY_NAME: Entity Name
        - PROTOCOL: Protocol of the device
        - ATT_ICCID: device attribute iccid
        - ATT_IMEI: device attribute imei
        - ATT_IMSI: device attribute imsi
        - ATT_INTERACTION_TYPE: device attribute interaction_type
        - ATT_SERVICE_ID: device attribute service_id
        - ATT_GEOLOCATION: device attribute geolocation
        '''
        data_log = {
            "DOMAIN_NAME": "%s" % DOMAIN_NAME,
            "DOMAIN_ID": "%s" % DOMAIN_ID,
            "PROJECT_NAME": "%s" % PROJECT_NAME,
            "PROJECT_ID": "%s" % PROJECT_ID,
            "SERVICE_USER_NAME": "%s" % SERVICE_USER_NAME,
            "SERVICE_USER_PASSWORD": "%s" % SERVICE_USER_PASSWORD,
            "SERVICE_USER_TOKEN": self.get_extended_token(SERVICE_USER_TOKEN),
            "DEVICE_ID": "%s" % DEVICE_ID,
            "ENTITY_TYPE": "%s" % ENTITY_TYPE,
            "ENTITY_NAME": "%s" % ENTITY_NAME,
            "PROTOCOL": "%s" % PROTOCOL,
            "ATT_ICCID": "%s" % ATT_ICCID,
            "ATT_IMEI": "%s" % ATT_IMEI,
            "ATT_IMSI": "%s" % ATT_IMSI,
            "ATT_INTERACTION_TYPE": "%s" % ATT_INTERACTION_TYPE,
            "ATT_SERVICE_ID": "%s" % ATT_SERVICE_ID,
            "ATT_GEOLOCATION": "%s" % ATT_GEOLOCATION
        }
        self.logger.debug("FLOW register_device with: %s" % json.dumps(
            data_log,
            indent=3)
        )
        try:
            if not SERVICE_USER_TOKEN:
                if not DOMAIN_ID:
                    SERVICE_USER_TOKEN = self.idm.getScopedProjectToken(
                        DOMAIN_NAME,
                        PROJECT_NAME,
                        SERVICE_USER_NAME,
                        SERVICE_USER_PASSWORD)
                    DOMAIN_ID = self.idm.getDomainId(SERVICE_USER_TOKEN,
                                                     DOMAIN_NAME)

                    PROJECT_ID = self.idm.getProjectId(SERVICE_USER_TOKEN,
                                                       DOMAIN_NAME,
                                                       PROJECT_NAME)
                else:
                    SERVICE_USER_TOKEN = self.idm.getScopedProjectToken2(
                        DOMAIN_ID,
                        PROJECT_ID,
                        SERVICE_USER_NAME,
                        SERVICE_USER_PASSWORD)
            self.logger.debug("SERVICE_USER_TOKEN=%s" % SERVICE_USER_TOKEN)


            # Ensure DOMAIN_NAME and PROJECT_NAME
            DOMAIN_NAME = self.ensure_service_name(SERVICE_USER_TOKEN,
                                                   DOMAIN_ID,
                                                   DOMAIN_NAME)
            self.logger.addFilter(ContextFilterService(DOMAIN_NAME))

            PROJECT_NAME = self.ensure_subservice_name(SERVICE_USER_TOKEN,
                                                       DOMAIN_ID,
                                                       PROJECT_ID,
                                                       PROJECT_NAME)
            self.logger.addFilter(ContextFilterSubService(PROJECT_NAME))

            self.logger.debug("DOMAIN_NAME=%s" % DOMAIN_NAME)
            self.logger.debug("PROJECT_NAME=%s" % PROJECT_NAME)


            #
            # 1. Call IOTA for register button
            #
            TIMEZONE = "Europe/Madrid" # TODO: get from django conf
            LAZY=[]
            ATTRIBUTES=[]
            STATIC_ATTRIBUTES = []
            INTERNAL_ATTRIBUTES = []
            COMMANDS = []

            if PROTOCOL == "TT_BLACKBUTTON":
                if ATT_INTERACTION_TYPE == None:
                    ATT_INTERACTION_TYPE = "synchronous"
                ATTRIBUTES = [
                    {
                        "name": "internal_id",
                        "type": "string"
                    },
                    {
                        "name": "last_operation",
                        "type": "string"
                    },
                    {
                        "name": "op_status",
                        "type": "string"
                    },
                    {
                        "name": "op_action",
                        "type": "string"
                    },
                    {
                        "name": "op_extra",
                        "type": "string"
                    },
                    {
                        "name": "sleepcondition",
                        "type": "string"
                    },
                    {
                        "name": "sleeptime",
                        "type": "string"
                    },
                    {
                        "name": "TimeInstant",
                        "type": "string"
                    }
                    ]

                # Ensure attributes are not empty
                if ATT_ICCID and ATT_ICCID != "":
                    STATIC_ATTRIBUTES.append(
                        {
                            "name": "iccid",
                            "type": "string",
                            "value": ATT_ICCID
                        })

                if ATT_IMEI and ATT_IMEI != "":
                    STATIC_ATTRIBUTES.append(
                        {
                            "name": "imei",
                            "type": "string",
                            "value": ATT_IMEI
                        })


                if ATT_IMSI and ATT_IMSI != "":
                    STATIC_ATTRIBUTES.append(
                        {
                            "name": "imsi",
                            "type": "string",
                            "value": ATT_IMSI
                        })

                if ATT_INTERACTION_TYPE and ATT_INTERACTION_TYPE != "":
                    STATIC_ATTRIBUTES.append(
                        {
                            "name": "interaction_type",
                            "type": "string",
                            "value": ATT_INTERACTION_TYPE
                        })

                if ATT_SERVICE_ID and ATT_SERVICE_ID != "":
                    STATIC_ATTRIBUTES.append(
                        {
                            "name": "service_id",
                            "type": "string",
                            "value": ATT_SERVICE_ID
                        })

                if ATT_GEOLOCATION and ATT_GEOLOCATION != "":
                    STATIC_ATTRIBUTES.append(
                        {
                            "name": "geolocation",
                            "type": "string",
                            "value": ATT_GEOLOCATION
                        })

                if ATT_INTERACTION_TYPE == "synchronous":
                    LAZY = [
                        {
                            "name": "op_result",
                            "type": "string"
                        }
                    ]
                if ATT_INTERACTION_TYPE == "asynchronous":
                    ATTRIBUTES.append(
                        {
                            "name": "op_result",
                            "type": "string"
                        })
                    ATTRIBUTES.append(
                        {
                            "name": "req_internal_id",
                            "type": "string"
                        })


            if PROTOCOL == "PDI-IoTA-ThinkingThings":
                if ATT_INTERACTION_TYPE == None:
                    ATT_INTERACTION_TYPE = "synchronous"
                ATTRIBUTES = [
                    {
                        "name": "mcc",
                        "type": "integer"
                    },
                    {
                        "name": "mnc",
                        "type": "integer"
                    },
                    {
                        "name": "lac",
                        "type": "integer"
                    },
                    {
                        "name": "cellid",
                        "type": "string"
                    },
                    {
                        "name": "dbm",
                        "type": "integer"
                    },
                    {
                        "name": "temperature",
                        "type": "float"
                    },
                    {
                        "name": "humidity",
                        "type": "float"
                    },
                    {
                        "name": "luminance",
                        "type": "float"
                    },
                    {
                        "name": "voltage",
                        "type": "float"
                    },
                    {
                        "name": "state",
                        "type": "integer"
                    },
                    {
                        "name": "charger",
                        "type": "integer"
                    },
                    {
                        "name": "charging",
                        "type": "integer"
                    },
                    {
                        "name": "mode",
                        "type": "integer"
                    },
                    {
                        "name": "desconnection",
                        "type": "integer"
                    },
                    {
                        "name": "sleepcondition",
                        "type": "string"
                    },
                    {
                        "name": "color",
                        "type": "string"
                    },
                    {
                        "name": "melody",
                        "type": "string"
                    },
                    {
                        "name": "sleeptime",
                        "type": "string"
                    }
                ]


            iota_res = self.iota.registerDevice(SERVICE_USER_TOKEN,
                                                DOMAIN_NAME,
                                                PROJECT_NAME,
                                                DEVICE_ID,
                                                PROTOCOL,
                                                ENTITY_NAME,
                                                ENTITY_TYPE,
                                                TIMEZONE,
                                                ATTRIBUTES,
                                                STATIC_ATTRIBUTES,
                                                COMMANDS,
                                                INTERNAL_ATTRIBUTES,
                                                LAZY
                                        )
            self.logger.debug("registerDevice res=%s" % iota_res)


        except Exception, ex:
            self.logger.error(ex)
            return self.composeErrorCode(ex)

        data_log = {

        }
        self.logger.info("Summary report : %s" % json.dumps(data_log, indent=3))

        # Consolidate opetions metrics into flow metrics
        self.collectComponentMetrics()

        return DEVICE_ID, DOMAIN_NAME, PROJECT_NAME


    def register_devices(self,
                        DOMAIN_NAME,
                        DOMAIN_ID,
                        PROJECT_NAME,
                        PROJECT_ID,
                        SERVICE_USER_NAME,
                        SERVICE_USER_PASSWORD,
                        SERVICE_USER_TOKEN,
                        CSV_DEVICES):

        '''Register Device in IOTA

        In case of HTTP error, return HTTP error

        Params:
        - DOMAIN_NAME: Service name
        - DOMAIN_ID: Service id
        - PROJECT_NAME: SubService name
        - PROJECT_ID: SubService name
        - SERVICE_USER_NAME: Service admin username
        - SERVICE_USER_PASSWORD: Service admin password
        - SERVICE_USER_TOKEN: Service admin token
        - CSV_DEVICES: CSV content

        '''
        data_log = {
            "DOMAIN_NAME": "%s" % DOMAIN_NAME,
            "DOMAIN_ID": "%s" % DOMAIN_ID,
            "PROJECT_NAME": "%s" % PROJECT_NAME,
            "PROJECT_ID": "%s" % PROJECT_ID,
            "SERVICE_USER_NAME": "%s" % SERVICE_USER_NAME,
            "SERVICE_USER_PASSWORD": "%s" % SERVICE_USER_PASSWORD,
            "SERVICE_USER_TOKEN": self.get_extended_token(SERVICE_USER_TOKEN),
            "CSV_DEVICES": "%s" % CSV_DEVICES
        }
        self.logger.debug("FLOW register_devices with: %s" % json.dumps(
            data_log,
            indent=3)
        )
        try:
            if not SERVICE_USER_TOKEN:
                if not DOMAIN_ID:
                    SERVICE_USER_TOKEN = self.idm.getScopedProjectToken(
                        DOMAIN_NAME,
                        PROJECT_NAME,
                        SERVICE_USER_NAME,
                        SERVICE_USER_PASSWORD)
                    DOMAIN_ID = self.idm.getDomainId(SERVICE_USER_TOKEN,
                                                     DOMAIN_NAME)

                    PROJECT_ID = self.idm.getProjectId(SERVICE_USER_TOKEN,
                                                       DOMAIN_NAME,
                                                       PROJECT_NAME)
                else:
                    SERVICE_USER_TOKEN = self.idm.getScopedProjectToken2(
                        DOMAIN_ID,
                        PROJECT_ID,
                        SERVICE_USER_NAME,
                        SERVICE_USER_PASSWORD)
            self.logger.debug("SERVICE_USER_TOKEN=%s" % SERVICE_USER_TOKEN)


            # Ensure DOMAIN_NAME and PROJECT_NAME
            DOMAIN_NAME = self.ensure_service_name(SERVICE_USER_TOKEN,
                                                   DOMAIN_ID,
                                                   DOMAIN_NAME)
            self.logger.addFilter(ContextFilterService(DOMAIN_NAME))

            PROJECT_NAME = self.ensure_subservice_name(SERVICE_USER_TOKEN,
                                                       DOMAIN_ID,
                                                       PROJECT_ID,
                                                       PROJECT_NAME)
            self.logger.addFilter(ContextFilterSubService(PROJECT_NAME))

            self.logger.debug("DOMAIN_NAME=%s" % DOMAIN_NAME)
            self.logger.debug("PROJECT_NAME=%s" % PROJECT_NAME)


            # Read CSV
            i, header, devices = CSVOperations.read_devices(CSV_DEVICES)
            DEVICES_ID = []
            num_devices = len(devices[header[i]])
            for n in range(num_devices):

                data_log = {
                    "DEVICE_ID" : devices['DEVICE_ID'][n],
                    "ENTITY_TYPE" : devices['ENTITY_TYPE'][n],
                    "ENTITY_NAME" : devices['ENTITY_NAME'][n],
                    "PROTOCOL": devices['PROTOCOL'][n],
                    "ATT_ICCID" : devices['ATT_ICCID'][n],
                    "ATT_IMEI" : devices['ATT_IMEI'][n],
                    "ATT_IMSI" : devices['ATT_IMSI'][n],
                    "ATT_INTERACTION_TYPE" : devices['ATT_INTERACTION_TYPE'][n],
                    "ATT_SERVICE_ID" : devices['ATT_SERVICE_ID'][n],
                    "ATT_GEOLOCATION" : devices['ATT_GEOLOCATION'][n]
                }
                self.logger.debug("data%s" % data_log)
                # TODO: use IOTA bulk API
                res = self.register_device(
                    DOMAIN_NAME,
                    DOMAIN_ID,
                    PROJECT_NAME,
                    PROJECT_ID,
                    SERVICE_USER_NAME,
                    SERVICE_USER_PASSWORD,
                    SERVICE_USER_TOKEN,
                    devices['DEVICE_ID'][n],
                    devices['ENTITY_TYPE'][n],
                    devices['ENTITY_NAME'][n],
                    devices['PROTOCOL'][n],
                    devices['ATT_ICCID'][n],
                    devices['ATT_IMEI'][n],
                    devices['ATT_IMSI'][n],
                    devices['ATT_INTERACTION_TYPE'][n],
                    devices['ATT_SERVICE_ID'][n],
                    devices['ATT_GEOLOCATION'][n]
                )
                DEVICES_ID.append(res)

        except Exception, ex:
            self.logger.error(ex)
            return self.composeErrorCode(ex)

        data_log = {
            "devices": DEVICES_ID
        }
        self.logger.info("Summary report : %s" % json.dumps(data_log, indent=3))

        # Consolidate opetions metrics into flow metrics
        self.collectComponentMetrics()

        return DEVICES_ID, DOMAIN_NAME, PROJECT_NAME

    def unregister_device(self,
                        DOMAIN_NAME,
                        DOMAIN_ID,
                        PROJECT_NAME,
                        PROJECT_ID,
                        SERVICE_USER_NAME,
                        SERVICE_USER_PASSWORD,
                        SERVICE_USER_TOKEN,
                        DEVICE_ID,
                        ):

        '''Unregister Device in IOTA

        In case of HTTP error, return HTTP error

        Params:
        - DOMAIN_NAME: Service name
        - DOMAIN_ID: Service id
        - PROJECT_NAME: SubService name
        - PROJECT_ID: SubService name
        - SERVICE_USER_NAME: Service admin username
        - SERVICE_USER_PASSWORD: Service admin password
        - SERVICE_USER_TOKEN: Service admin token
        - DEVICE_ID: Device ID
        '''
        data_log = {
            "DOMAIN_NAME": "%s" % DOMAIN_NAME,
            "DOMAIN_ID": "%s" % DOMAIN_ID,
            "PROJECT_NAME": "%s" % PROJECT_NAME,
            "PROJECT_ID": "%s" % PROJECT_ID,
            "SERVICE_USER_NAME": "%s" % SERVICE_USER_NAME,
            "SERVICE_USER_PASSWORD": "%s" % SERVICE_USER_PASSWORD,
            "SERVICE_USER_TOKEN": self.get_extended_token(SERVICE_USER_TOKEN),
            "DEVICE_ID": "%s" % DEVICE_ID,
        }
        self.logger.debug("FLOW unregister_device with: %s" % json.dumps(
            data_log,
            indent=3)
        )
        try:
            if not SERVICE_USER_TOKEN:
                if not DOMAIN_ID:
                    SERVICE_USER_TOKEN = self.idm.getScopedProjectToken(
                        DOMAIN_NAME,
                        PROJECT_NAME,
                        SERVICE_USER_NAME,
                        SERVICE_USER_PASSWORD)
                    DOMAIN_ID = self.idm.getDomainId(SERVICE_USER_TOKEN,
                                                     DOMAIN_NAME)

                    PROJECT_ID = self.idm.getProjectId(SERVICE_USER_TOKEN,
                                                       DOMAIN_NAME,
                                                       PROJECT_NAME)
                else:
                    SERVICE_USER_TOKEN = self.idm.getScopedProjectToken2(
                        DOMAIN_ID,
                        PROJECT_ID,
                        SERVICE_USER_NAME,
                        SERVICE_USER_PASSWORD)
            self.logger.debug("SERVICE_USER_TOKEN=%s" % SERVICE_USER_TOKEN)


            # Ensure DOMAIN_NAME and PROJECT_NAME
            DOMAIN_NAME = self.ensure_service_name(SERVICE_USER_TOKEN,
                                                   DOMAIN_ID,
                                                   DOMAIN_NAME)
            self.logger.addFilter(ContextFilterService(DOMAIN_NAME))

            PROJECT_NAME = self.ensure_subservice_name(SERVICE_USER_TOKEN,
                                                       DOMAIN_ID,
                                                       PROJECT_ID,
                                                       PROJECT_NAME)
            self.logger.addFilter(ContextFilterSubService(PROJECT_NAME))

            self.logger.debug("DOMAIN_NAME=%s" % DOMAIN_NAME)
            self.logger.debug("PROJECT_NAME=%s" % PROJECT_NAME)

            iota_res = self.iota.unregisterDevice(
                                                SERVICE_USER_TOKEN,
                                                DOMAIN_NAME,
                                                PROJECT_NAME,
                                                DEVICE_ID)
            self.logger.debug("unregisterDevice res=%s" % iota_res)


        except Exception, ex:
            self.logger.error(ex)
            return self.composeErrorCode(ex)

        data_log = {

        }
        self.logger.info("Summary report : %s" % json.dumps(data_log, indent=3))

        # Consolidate opetions metrics into flow metrics
        self.collectComponentMetrics()

        return {}, DOMAIN_NAME, PROJECT_NAME


    def activate_module(self,
                        DOMAIN_NAME,
                        DOMAIN_ID,
                        PROJECT_NAME,
                        PROJECT_ID,
                        SERVICE_USER_NAME,
                        SERVICE_USER_PASSWORD,
                        SERVICE_USER_TOKEN,
                        IOTMODULE):

        '''Activate Module

        In case of HTTP error, return HTTP error

        Params:
        - DOMAIN_ID: id of domain
        - DOMAIN_NAME: name of domain
        - PROJECT_ID: id of project
        - PROJECT_NAME: name of project
        - SERVICE_USER_NAME: Service admin username
        - SERVICE_USER_PASSWORD: Service admin password
        - SERVICE_USER_TOKEN: Service admin token
        - IOTMODULE: IoT Module to activate: STH, PERSEO
        '''
        data_log = {
            "DOMAIN_ID": "%s" % DOMAIN_ID,
            "DOMAIN_NAME": "%s" % DOMAIN_NAME,
            "PROJECT_ID": "%s" % PROJECT_ID,
            "PROJECT_NAME": "%s" % PROJECT_NAME,
            "SERVICE_USER_NAME": "%s" % SERVICE_USER_NAME,
            "SERVICE_USER_PASSWORD": "%s" % SERVICE_USER_PASSWORD,
            "SERVICE_USER_TOKEN": self.get_extended_token(SERVICE_USER_TOKEN),
            "IOTMODULE": "%s" % IOTMODULE,
        }
        self.logger.debug("FLOW activate_module invoked with: %s" % json.dumps(
            data_log,
            indent=3)
        )
        try:

            if not SERVICE_USER_TOKEN:
                if not DOMAIN_ID:
                    SERVICE_USER_TOKEN = self.idm.getScopedProjectToken(
                        DOMAIN_NAME,
                        PROJECT_NAME,
                        SERVICE_USER_NAME,
                        SERVICE_USER_PASSWORD)
                    DOMAIN_ID = self.idm.getDomainId(SERVICE_USER_TOKEN,
                                                     DOMAIN_NAME)
                    PROJECT_ID = self.idm.getProjectId(SERVICE_USER_TOKEN,
                                                        DOMAIN_NAME,
                                                        PROJECT_NAME)

                else:
                    SERVICE_USER_TOKEN = self.idm.getScopedProjectToken2(
                        DOMAIN_ID,
                        PROJECT_ID,
                        SERVICE_USER_NAME,
                        SERVICE_USER_PASSWORD)
            # Ensure DOMAIN_NAME and PROJECT_NAME
            DOMAIN_NAME = self.ensure_service_name(SERVICE_USER_TOKEN,
                                                   DOMAIN_ID,
                                                   DOMAIN_NAME)
            self.logger.addFilter(ContextFilterService(DOMAIN_NAME))

            PROJECT_NAME = self.ensure_subservice_name(SERVICE_USER_TOKEN,
                                                       DOMAIN_ID,
                                                       PROJECT_ID,
                                                       PROJECT_NAME)
            self.logger.addFilter(ContextFilterSubService(PROJECT_NAME))

            self.logger.debug("DOMAIN_NAME=%s" % DOMAIN_NAME)
            self.logger.debug("PROJECT_NAME=%s" % PROJECT_NAME)
            self.logger.debug("SERVICE_USER_TOKEN=%s" % SERVICE_USER_TOKEN)


            if not PROJECT_ID:
                PROJECT_ID = self.idm.getProjectId(SERVICE_USER_TOKEN,
                                                   DOMAIN_NAME,
                                                   PROJECT_NAME)

            REFERENCE_URL = self.get_endpoint_iot_module(IOTMODULE)

            #if not REFERENCE_URL:
            #    return self.composeErrorCode(ex)
            DURATION="P1Y"

            # Set default ATTRIBUTES for subscription
            ATTRIBUTES = []
            # self.logger.debug("Trying to getContextTypes...")
            # cb_res = self.cb.getContextTypes(
            #     SERVICE_USER_TOKEN,
            #     DOMAIN_NAME,
            #     PROJECT_NAME,
            #     None)
            # self.logger.debug("getContextTypes res=%s" % cb_res)
            # for entity_type in cb_res['types']:
            #     for att in entity_type["attributes"] :
            #         ATTRIBUTES.append(att)

            # Set default ENTITIES for subscription
            ENTITIES = [ {
                "isPattern": "true",
                "id": ".*"
            } ]

            # Set default Notify conditions
            NOTIFY_ATTRIBUTES = []
            NOTIFY_ATTRIBUTES.append("TimeInstant")
            NOTIFY_CONDITIONS = [ {
                "type": "ONCHANGE",
                "condValues": NOTIFY_ATTRIBUTES
            } ]

            self.logger.debug("Trying to subscribe moduleiot in CB...")
            cb_res = self.cb.subscribeContext(
                SERVICE_USER_TOKEN,
                DOMAIN_NAME,
                PROJECT_NAME,
                REFERENCE_URL,
                DURATION,
                ENTITIES,
                ATTRIBUTES,
                NOTIFY_CONDITIONS
            )
            self.logger.debug("subscribeContext res=%s" % json.dumps(cb_res,
                                                                     indent=3))
            subscriptionid = cb_res['subscribeResponse']['subscriptionId']
            self.logger.debug("subscription id=%s" % subscriptionid)

        except Exception, ex:
            self.logger.error(ex)
            return self.composeErrorCode(ex)

        data_log = {
            "subscriptionid": subscriptionid
        }
        self.logger.info("Summary report : %s" % json.dumps(data_log, indent=3))

        # Consolidate opetions metrics into flow metrics
        self.collectComponentMetrics()

        return subscriptionid, DOMAIN_NAME, PROJECT_NAME

    def deactivate_module(self,
                          DOMAIN_NAME,
                          DOMAIN_ID,
                          PROJECT_NAME,
                          PROJECT_ID,
                          SERVICE_USER_NAME,
                          SERVICE_USER_PASSWORD,
                          SERVICE_USER_TOKEN,
                          IOTMODULE):

        ''' Deactivate IoT Module

        In case of HTTP error, return HTTP error

        Params:
        - DOMAIN_ID: id of domain
        - DOMAIN_NAME: name of domain
        - PROJECT_ID: id of project
        - PROJECT_NAME: name of project
        - SERVICE_USER_NAME: Service admin username
        - SERVICE_USER_PASSWORD: Service admin password
        - SERVICE_USER_TOKEN: Service admin token
        - IOTMODULE: IoT Module to activate: STH, PERSEO
        '''
        data_log = {
            "DOMAIN_ID": "%s" % DOMAIN_ID,
            "DOMAIN_NAME": "%s" % DOMAIN_NAME,
            "PROJECT_ID": "%s" % PROJECT_ID,
            "PROJECT_NAME": "%s" % PROJECT_NAME,
            "SERVICE_USER_NAME": "%s" % SERVICE_USER_NAME,
            "SERVICE_USER_PASSWORD": "%s" % SERVICE_USER_PASSWORD,
            "SERVICE_USER_TOKEN": self.get_extended_token(SERVICE_USER_TOKEN),
            "IOTMODULE": "%s" % IOTMODULE,
        }
        self.logger.debug("FLOW deactivate_module invoked with: %s" % json.dumps(
            data_log,
            indent=3)
        )
        try:

            if not SERVICE_USER_TOKEN:
                if not DOMAIN_ID:
                    SERVICE_USER_TOKEN = self.idm.getScopedProjectToken(
                        DOMAIN_NAME,
                        PROJECT_NAME,
                        SERVICE_USER_NAME,
                        SERVICE_USER_PASSWORD)
                    DOMAIN_ID = self.idm.getDomainId(SERVICE_USER_TOKEN,
                                                     DOMAIN_NAME)
                    PROJECT_ID = self.idm.getProjectId(SERVICE_USER_TOKEN,
                                                        DOMAIN_NAME,
                                                        PROJECT_NAME)

                else:
                    SERVICE_USER_TOKEN = self.idm.getScopedProjectToken2(
                        DOMAIN_ID,
                        PROJECT_ID,
                        SERVICE_USER_NAME,
                        SERVICE_USER_PASSWORD)

            # Ensure DOMAIN_NAME and PROJECT_NAME
            DOMAIN_NAME = self.ensure_service_name(SERVICE_USER_TOKEN,
                                                   DOMAIN_ID,
                                                   DOMAIN_NAME)
            self.logger.addFilter(ContextFilterService(DOMAIN_NAME))

            PROJECT_NAME = self.ensure_subservice_name(SERVICE_USER_TOKEN,
                                                       DOMAIN_ID,
                                                       PROJECT_ID,
                                                       PROJECT_NAME)
            self.logger.addFilter(ContextFilterSubService(PROJECT_NAME))

            self.logger.debug("DOMAIN_NAME=%s" % DOMAIN_NAME)
            self.logger.debug("PROJECT_NAME=%s" % PROJECT_NAME)
            self.logger.debug("SERVICE_USER_TOKEN=%s" % SERVICE_USER_TOKEN)

            if not PROJECT_ID:
                PROJECT_ID = self.idm.getProjectId(SERVICE_USER_TOKEN,
                                                   DOMAIN_NAME,
                                                   PROJECT_NAME)

            REFERENCE_URL = self.get_endpoint_iot_module(IOTMODULE)

            self.logger.debug("Trying to get list subscriptions from CB...")
            cb_res = self.cb.getListSubscriptions(
                SERVICE_USER_TOKEN,
                DOMAIN_NAME,
                PROJECT_NAME
            )
            self.logger.debug("getListSubscriptions res=%s" % json.dumps(cb_res,
                                                                         indent=3))

            for sub in cb_res:
                subs_url = self.cb.get_subscription_callback_endpoint(sub)
                subscriptionid = sub['id']
                if subs_url.startswith(REFERENCE_URL):

                    self.cb.unsubscribeContext(SERVICE_USER_TOKEN,
                                               DOMAIN_NAME,
                                               PROJECT_NAME,
                                               sub['id'])
                    break

        except Exception, ex:
            self.logger.error(ex)
            return self.composeErrorCode(ex)

        data_log = {
            "subscriptionid": subscriptionid
        }
        self.logger.info("Summary report : %s" % json.dumps(data_log, indent=3))

        # Consolidate opetions metrics into flow metrics
        self.collectComponentMetrics()

        return subscriptionid, DOMAIN_NAME, PROJECT_NAME


    def list_activated_modules(self,
                               DOMAIN_NAME,
                               DOMAIN_ID,
                               PROJECT_NAME,
                               PROJECT_ID,
                               SERVICE_USER_NAME,
                               SERVICE_USER_PASSWORD,
                               SERVICE_USER_TOKEN):

        '''List Activated IoT Modules

        In case of HTTP error, return HTTP error

        Params:
        - DOMAIN_ID: id of domain
        - DOMAIN_NAME: name of domain
        - PROJECT_ID: id of project
        - PROJECT_NAME: name of project
        - SERVICE_USER_NAME: Service admin username
        - SERVICE_USER_PASSWORD: Service admin password
        - SERVICE_USER_TOKEN: Service admin token
        '''
        data_log = {
            "DOMAIN_ID": "%s" % DOMAIN_ID,
            "DOMAIN_NAME": "%s" % DOMAIN_NAME,
            "PROJECT_ID": "%s" % PROJECT_ID,
            "PROJECT_NAME": "%s" % PROJECT_NAME,
            "SERVICE_USER_NAME": "%s" % SERVICE_USER_NAME,
            "SERVICE_USER_PASSWORD": "%s" % SERVICE_USER_PASSWORD,
            "SERVICE_USER_TOKEN": self.get_extended_token(SERVICE_USER_TOKEN),
        }
        self.logger.debug("FLOW list_activated_modules invoked with: %s" % json.dumps(
            data_log,
            indent=3)
        )
        try:
            if not SERVICE_USER_TOKEN:
                if not DOMAIN_ID:
                    SERVICE_USER_TOKEN = self.idm.getScopedProjectToken(
                        DOMAIN_NAME,
                        PROJECT_NAME,
                        SERVICE_USER_NAME,
                        SERVICE_USER_PASSWORD)
                    DOMAIN_ID = self.idm.getDomainId(SERVICE_USER_TOKEN,
                                                     DOMAIN_NAME)
                    PROJECT_ID = self.idm.getProjectId(SERVICE_USER_TOKEN,
                                                        DOMAIN_NAME,
                                                        PROJECT_NAME)

                else:
                    SERVICE_USER_TOKEN = self.idm.getScopedProjectToken2(
                        DOMAIN_ID,
                        PROJECT_ID,
                        SERVICE_USER_NAME,
                        SERVICE_USER_PASSWORD)

            # Ensure DOMAIN_NAME and PROJECT_NAME
            DOMAIN_NAME = self.ensure_service_name(SERVICE_USER_TOKEN,
                                                   DOMAIN_ID,
                                                   DOMAIN_NAME)
            self.logger.addFilter(ContextFilterService(DOMAIN_NAME))

            PROJECT_NAME = self.ensure_subservice_name(SERVICE_USER_TOKEN,
                                                       DOMAIN_ID,
                                                       PROJECT_ID,
                                                       PROJECT_NAME)
            self.logger.addFilter(ContextFilterSubService(PROJECT_NAME))

            self.logger.debug("DOMAIN_NAME=%s" % DOMAIN_NAME)
            self.logger.debug("PROJECT_NAME=%s" % PROJECT_NAME)
            self.logger.debug("SERVICE_USER_TOKEN=%s" % SERVICE_USER_TOKEN)

            if not PROJECT_ID:
                PROJECT_ID = self.idm.getProjectId(SERVICE_USER_TOKEN,
                                                   DOMAIN_NAME,
                                                   PROJECT_NAME)

            self.logger.debug("Trying to get list subscriptions from CB...")
            cb_res = self.cb.getListSubscriptions(
                SERVICE_USER_TOKEN,
                DOMAIN_NAME,
                PROJECT_NAME
            )
            self.logger.debug("getListSubscriptions res=%s" % json.dumps(cb_res, indent=3))
            modules = self.cb.extract_modules_from_subscriptions(self, IOTMODULES, cb_res)
            self.logger.debug("modules=%s" % json.dumps(modules, indent=3))

        except Exception, ex:
            self.logger.error(ex)
            return self.composeErrorCode(ex)

        data_log = {
            "modules": modules
        }
        self.logger.info("Summary report : %s" % json.dumps(data_log, indent=3))

        # Consolidate opetions metrics into flow metrics
        self.collectComponentMetrics()

        return modules, DOMAIN_NAME, PROJECT_NAME
