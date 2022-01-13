#!/bin/bash
# This script is designed to be run by Github Actions workflow
# to trigger the RMG-tests at 
# https://github.com/reactionmechanismgenerator/rmg-tests

set -e # exit with nonzero exit code if anything fails

git config --global user.name "RMG Bot"
git config --global user.email "rmg_dev@mit.edu"

BRANCH=${GITHUB_REF#refs/heads/}

echo "GITHUB_WORKSPACE: $GITHUB_WORKSPACE"
echo "BRANCH: $BRANCH"
echo "RMG_PY_BRANCH: $RMG_PY_BRANCH"

# URL for the official RMG-tests repository
REPO=https://${GH_TOKEN}@github.com/ReactionMechanismGenerator/RMG-tests.git

# create a temporary folder:
REPO_NAME=$(basename $REPO)
TARGET_DIR=$(mktemp -d /tmp/$REPO_NAME.XXXX)
REV=$(git rev-parse HEAD)

# clone RMG-tests repo in the newly created folder:
git clone ${REPO} ${TARGET_DIR}

# go inside the newly created folder:
cd $TARGET_DIR

# create a new branch in RMG-tests with the name equal to
# the branch name of the tested RMG-database branch:
if [ "$RMG_PY_BRANCH" == "main" ]
then
  RMGTESTSBRANCH=rmgdb-$BRANCH
else
  RMGTESTSBRANCH=rmgdbpy-$BRANCH
fi

git checkout -b $RMGTESTSBRANCH || true
git checkout $RMGTESTSBRANCH

# create an empty commit with the SHA-ID of the
# tested commit of the RMG-database branch:
if [ "$RMG_PY_BRANCH" == "main" ]
then
  git commit --allow-empty -m rmgdb-$REV
else
  git commit --allow-empty -m rmgdbpy-$REV-${RMG_PY_BRANCH}
fi

# push to the branch to the RMG/RMG-tests repo:
git push -f $REPO $RMGTESTSBRANCH > /dev/null
