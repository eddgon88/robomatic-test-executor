from . import db
from datetime import datetime
from sqlalchemy import text, null

class EvidenceFile(db.Model):
    __tablename__ = 'evidence_file'
    __table_args__ = {'schema':'test_executor'}

    id = db.Column(db.Integer, primary_key=True)
    evidence_id = db.Column(db.String(100), unique=True)
    file_name = db.Column(db.String(100))
    evidence_uri = db.Column(db.String(100))
    test_execution_id = db.Column(db.String(100))

    def get_file(name, test_execution_id):
        print("---------------------getting file: " + test_execution_id + "-------------------------")
        count = db.session.query(EvidenceFile).filter_by(file_name="test.txt", test_execution_id="te456468574").count()
        print("------------" + str(count))
        result = db.session.query(EvidenceFile).filter_by(file_name=name, test_execution_id=test_execution_id).first()
        print(result)
        return result

class CaseEvidence(db.Model):
    __tablename__ = 'case_evidence'
    __table_args__ = {'schema':'test_executor'}

    id = db.Column(db.Integer, primary_key=True)
    evidence_id = db.Column(db.String(100))
    evidence_text = db.Column(db.Text)
    creation_date = db.Column(db.TIMESTAMP, default=datetime.today())