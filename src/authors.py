class Authors:
  def connect(self):
    # Connects to the database
    pass

  def create(self):
    # Creates `authors` table, making the headers
    # in `authors.csv` file the fields of the table
    pass

  def insert(self):
    # Inserts all data rows in `authors.csv` file into
    # the `authors` table created
    pass

  def select(self):
    # Select all rows from the `authors` table
    pass

  def find(self, id):
    # Select a row with id supplied from the `authors` table
    pass

  def update(self, id, params):
    # Update a row with id supplied in the `authors` table with
    # data provided as `params`
    pass

  def delete(self, id):
    # Delete the row with id supplied from the `authors` table
    pass
