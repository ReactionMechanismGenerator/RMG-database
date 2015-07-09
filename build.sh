# Install scripts in bin folder
$PYTHON setup.py install

# Copy database files to shared directory
cd ${PREFIX}/share/
mkdir rmgdatabase
cp -R ${SRC_DIR}/input/* rmgdatabase/