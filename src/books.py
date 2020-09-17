class Books:
  def connect(self):
    # Connects to the database
    pass

  def create(self):
    # Creates `books` table, making the headers
    # in `books.csv` file the fields of the table
    pass

  def insert(self):
    # Inserts all data rows in `books.csv` file into
    # the `books` table created
    pass

  def select(self):
    # Select all rows from the `books` table
    pass

  def find(self, id):
    # Select a row with id supplied from the `books` table
    pass

  def update(self, id, params):
    # Update a row with id supplied in the `books` table with
    # data provided as `params`
    pass

  def delete(self, id):
    # Delete the row with id supplied from the `books` table
    pass
