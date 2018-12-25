# Install scripts in bin folder
$PYTHON setup.py install

# Copy database files to shared directory
cd ${PREFIX}/share/
mkdir rmgdatabase
cp -R ${SRC_DIR}/input/* rmgdatabase/

# Create rmgrc file that points to this folder in site-packages/rmgpy directory
cd ${SP_DIR}
mkdir rmgpy
echo 'database.directory: ' ${PREFIX}/share/rmgdatabase > ${SP_DIR}/rmgpy/rmgrc