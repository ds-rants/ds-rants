#!/bin/bash

# Designated author name
DESIGNATED_AUTHOR="Data Science Rants"
DESIGNATED_EMAIL="data.science.rants@proton.me"

# Get the current commit author
CURRENT_AUTHOR=$(git config --local user.name)
CURRENT_EMAIL=$(git config --local user.email)


if [ "$CURRENT_AUTHOR" != "$DESIGNATED_AUTHOR" ] && [ "$CURRENT_EMAIL" != "$DESIGNATED_EMAIL" ]; then
  echo "Error: Commit author must be $DESIGNATED_AUTHOR. Current author is $CURRENT_AUTHOR."
  echo "Error: Commit email must be $DESIGNATED_EMAIL. Current email is $CURRENT_EMAIL."
  exit 1
fi

exit 0
