#!/bin/bash

FOLDER_SYNC_FUNC_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"   

function fsync {

   $FOLDER_SYNC_FUNC_DIR/foldersync.py "$PWD" "$@"
   local FOLDER_SYNC_RETURN_CODE=$?   

   if [ "$FOLDER_SYNC_RETURN_CODE" == "33" ]
   then   
      bash ~/.foldersync
      rm ~/.foldersync
      return
   fi
}

complete -W "remote pull push" fsync
