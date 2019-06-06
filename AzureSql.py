import pyodbc

server = 'xxxx.database.windows.net'
database = 'xxxx'
username = 'xxxx'
password = 'xxxx'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor1 = cnxn.cursor()
cursor2 = cnxn.cursor()

cursor2.execute(
    "select count(*) from information_schema.columns where table_catalog = 'tasks' and table_name = 'Tasks'"
)
i = cursor2.fetchone()
i = [x for x in i]
i = i[0]
temp = 0
string_row = ""

cursor1.execute("SELECT * FROM Tasks")
row = cursor1.fetchone()
while row:
    while temp != i:
        string_row = string_row + str(row[temp]) + ", "
        temp +=1
    string_row = string_row + "\n"
    row = cursor1.fetchone()
    temp = 0
print string_row
