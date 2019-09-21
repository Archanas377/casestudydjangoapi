from mongoengine import Document, EmbeddedDocument, fields


class Projects(EmbeddedDocument):
    projectId = fields.StringField(max_length=10, required=True, null=False)
    projectName = fields.StringField(max_length=255, required=False)
    startDate = fields.DateTimeField()
    endDate = fields.DateTimeField()   


class Skills(EmbeddedDocument):
    technology = fields.StringField(max_length=255, required=False )
    experience = fields.IntField()
    level = fields.StringField(max_length=255, required=False )

class Employee(Document):
    employeeID = fields.StringField(max_length=10, required=True, null=False)
    employeeName = fields.StringField(max_length=100, required=True)
    workLocation= fields.StringField(max_length=255, required=True)
    # orders = fields.EmbeddedDocumentListField(Order)
    skills=fields.EmbeddedDocumentListField(Skills)
    projects=fields.EmbeddedDocumentListField(Projects)