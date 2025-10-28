GIT_CMD=git
BREW_CMD=brew
UV_CMD=uv
PRE_COMMIT_CMD=pre-commit
PIP_AUDIT_CMD=pip-audit


if ! command -v $GIT_CMD >/dev/null 2>&1; then
  echo "Error: mycommand not found. Please install it."
  exit 1
else
  echo "${GIT_CMD} is installed!"
fi

if ! command -v $BREW_CMD >/dev/null 2>&1; then
  echo "Error: mycommand not found. Please install it."
  exit 1
else
  echo "${BREW_CMD} is installed!"
fi

if ! command -v $UV_CMD >/dev/null 2>&1; then
  echo "Error: mycommand not found. Please install it."
  exit 1
else
  echo "${UV_CMD} is installed!"
fi

if ! command -v $PRE_COMMIT_CMD >/dev/null 2>&1; then
  echo "Error: mycommand not found. Please install it."
  exit 1
else
  echo "${PRE_COMMIT_CMD} is installed!"
fi

if ! command -v $PIP_AUDIT_CMD >/dev/null 2>&1; then
  echo "Error: mycommand not found. Please install it."
  exit 1
else
  echo "${PIP_AUDIT_CMD} is installed!"
fi

git init
pre-commit install
