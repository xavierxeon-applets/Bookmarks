#!/bin/bash

BOOKMARK_FUNC_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"   

function bmk {

   mkdir -p ~/.bookmarks

   $BOOKMARK_FUNC_DIR/bookmark.py "$PWD" "$@"
   local BOOKMARK_RETURN_CODE=$?

   if [ "$BOOKMARK_RETURN_CODE" == "22" ]
   then   
      source ~/.bookmarks/complete.sh
      return
   fi   

   if [ "$BOOKMARK_RETURN_CODE" == "33" ]
   then   
      local JUMP_DIR=$(cat ~/.bookmarks/jump)
      cd "$JUMP_DIR"
      return
   fi

   if [ "$BOOKMARK_RETURN_CODE" == "44" ]
   then   
      local TARGET=$(cat ~/.bookmarks/repo)
      git clone "$TARGET"
      return
   fi

   if [ "$BOOKMARK_RETURN_CODE" == "55" ]
   then   
      local TARGET=$(cat ~/.bookmarks/sync)
      fsync init "$TARGET"
      fsync pull
      return
   fi
}

alias jump="bmk jump"
alias store="bmk store"
alias reclone="bmk reclone"

# init completion
bmk init
source ~/.bookmarks/complete.sh
