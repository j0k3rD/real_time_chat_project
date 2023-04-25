from ..repositories.database import Database
from repositories import Create, Delete, Read, Update 
from ..models import Message as MessageModel


class MessageRepository(Create, Read, Update, Delete):
    '''
    Clase que representa el repositorio de la entidad Message
    param:
        - Create: Clase que hereda de la interfaz Create
        - Read: Clase que hereda de la interfaz Read
        - Update: Clase que hereda de la interfaz Update
        - Delete: Clase que hereda de la interfaz Delete
    '''
    def __init__(self):
        self.__type_model = MessageModel

    @property
    def type_model(self):
        return self.__type_model
    
    def create(self, message):
        query = "INSERT INTO messages (content, author) VALUES (%s, %s)"
        values = (message.content, message.author)
        cursor = self.cnx.cursor()
        cursor.execute(query, values)
        self.cnx.commit()
        cursor.close()

    def update(self, message):
        query = "UPDATE messages SET content = %s, author = %s WHERE id = %s"
        values = (message.content, message.author, message.id)
        cursor = self.cnx.cursor()
        cursor.execute(query, values)
        self.cnx.commit()
        cursor.close()

    def find_all(self):
        query = "SELECT * FROM messages"
        cursor = self.cnx.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return [MessageModel(*row) for row in rows]

    def find_by_id(self, id):
        query = "SELECT * FROM messages WHERE id = %s"
        values = (id,)
        cursor = self.cnx.cursor()
        cursor.execute(query, values)
        row = cursor.fetchone()
        cursor.close()
        return MessageModel(*row) if row is not None else None

    def delete(self, id):
        query = "DELETE FROM messages WHERE id = %s"
        values = (id,)
        cursor = self.cnx.cursor()
        cursor.execute(query, values)
        self.cnx.commit()
        cursor.close()