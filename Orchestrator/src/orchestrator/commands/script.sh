#!/bin/bash

KEYSTONE_PROTOCOL=http
KEYSTONE_HOST=orchestrator_keystone_1
KEYSTONE_PORT=5001
KEYPASS_PROTOCOL=http
KEYPASS_HOST=orchestrator_keypass_1
KEYPASS_PORT=7070

DEFAULT_PWD=4pass1w0rd

function checkResult() {
    if [ $1 -eq 0 ]; then
        echo -n
        echo -e "- $2 ....... OK"
    else
        echo -e "Error found while $2. Code: $1. Aborting"
        exit $1
    fi
}

python ./createNewService.py $KEYSTONE_PROTOCOL				\
                                 $KEYSTONE_HOST			 	\
                                 $KEYSTONE_PORT				\
                                 admin_domain   			\
                                 cloud_admin    			\
                                 $DEFAULT_PWD     			\
                                 smartcity      			\
                                 smartcity      			\
                                 adm1           			\
                                 $DEFAULT_PWD       		\
                                 $KEYPASS_PROTOCOL  		\
                                 $KEYPASS_HOST  			\
                                 $KEYPASS_PORT
checkResult $? "Creating service"

python ./assignInheritRoleServiceUser.py $KEYSTONE_PROTOCOL \
                                    $KEYSTONE_HOST   \
                                    $KEYSTONE_PORT   \
                                    smartcity        \
                                    adm1             \
                                    $DEFAULT_PWD     \
                                    adm1             \
                                    SubServiceAdmin
checkResult $? "assignInheritRole to admin"

python ./createNewSubService.py  $KEYSTONE_PROTOCOL  \
                                      $KEYSTONE_HOST \
                                      $KEYSTONE_PORT \
                                      smartcity      \
                                      adm1           \
                                      $DEFAULT_PWD   \
                                      Electricity    \
                                      electricity
checkResult $? "Creating sub service Electricidad"

python ./createNewServiceUser.py  $KEYSTONE_PROTOCOL \
                                      $KEYSTONE_HOST \
                                      $KEYSTONE_PORT \
                                      smartcity      \
                                      adm1           \
                                      $DEFAULT_PWD       \
                                      Alice          \
                                      $DEFAULT_PWD
checkResult $? "Creating user Alice"

python ./assignRoleSubServiceUser.py $KEYSTONE_PROTOCOL  \
                                       $KEYSTONE_HOST \
                                       $KEYSTONE_PORT \
                                       smartcity      \
                                       Electricity   \
                                       adm1           \
                                       $DEFAULT_PWD       \
                                       SubServiceAdmin\
                                       Alice
checkResult $? "Assing role SubServiceAdmin to user Alice"

python ./createNewSubService.py  $KEYSTONE_PROTOCOL  \
                                      $KEYSTONE_HOST \
                                      $KEYSTONE_PORT \
                                      smartcity      \
                                      adm1           \
                                      $DEFAULT_PWD       \
                                      Trash        \
                                      trash
checkResult $? "Creating subservice Basuras"

python ./createNewServiceUser.py  $KEYSTONE_PROTOCOL  \
                                       $KEYSTONE_HOST \
                                       $KEYSTONE_PORT \
                                       smartcity      \
                                       adm1           \
                                       $DEFAULT_PWD       \
                                       bob            \
                                       $DEFAULT_PWD
checkResult $? "Creating user bob"

python ./assignRoleSubServiceUser.py $KEYSTONE_PROTOCOL  \
                                       $KEYSTONE_HOST \
                                       $KEYSTONE_PORT \
                                       smartcity      \
                                       Trash        \
                                       adm1           \
                                       $DEFAULT_PWD       \
                                       SubServiceAdmin\
                                       bob
checkResult $? "Assign subServiceAdmin role to user bob"

python ./createNewServiceUser.py  $KEYSTONE_PROTOCOL \
                                      $KEYSTONE_HOST \
                                      $KEYSTONE_PORT \
                                      smartcity      \
                                      adm1           \
                                      $DEFAULT_PWD       \
                                      Carl           \
                                      $DEFAULT_PWD
checkResult $? "Creating user Carl"

python ./assignRoleServiceUser.py $KEYSTONE_PROTOCOL  \
                                       $KEYSTONE_HOST \
                                       $KEYSTONE_PORT \
                                       smartcity      \
                                       adm1           \
                                       $DEFAULT_PWD       \
                                       ServiceCustomer\
                                       Carl
checkResult $? "Assign ServiceCustomer role to user Carl"

python ./assignInheritRoleServiceUser.py $KEYSTONE_PROTOCOL \
                                    $KEYSTONE_HOST    \
                                    $KEYSTONE_PORT    \
                                    smartcity         \
                                    adm1              \
                                    $DEFAULT_PWD          \
                                    Carl              \
                                    SubServiceCustomer
checkResult $? "Assign subServiceCustomer role to user Carl"