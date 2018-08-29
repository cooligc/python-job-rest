
from flask import Flask,jsonify
from flask_restful import Resource, Api,reqparse, fields, marshal_with
from data_store import init_db,session
from db_model import JobEntity
from job_datastore import start_job

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('id')
parser.add_argument('status')
parser.add_argument('initiated_by')

resource_fields = {
    'name':   fields.String,
    'id':    fields.String,
    'status': fields.String,
    'initiated_by': fields.String
}


class Job(Resource):
    def get(self):
        jobs = JobEntity.query.all()
        response=[]
        for job in jobs:
            response.append(job.as_dict())
        return response,200

    @marshal_with(resource_fields)
    def post(self):
        args = parser.parse_args()
        job = JobEntity(name=args['name'],job_id=args['id'],initiated_by=args['initiated_by'],status=args['status'])
        session.add(job)
        session.commit()
        return job.as_dict(),201

    def put(self,id):
        print(id)
        args = parser.parse_args()

        job = session.query(JobEntity).filter_by(job_id=args['id']).first()
        print(job)
        if(job is None):
            return self.post()

        job.status=args['status']
        job.initiated_by=args['initiated_by']
        session.add(job)
        session.commit()
        return job.as_dict(),200

    def delete(self,id):
        args = parser.parse_args()
        job = session.query(JobEntity).filter_by(job_id=args['id']).first()
        print(job)
        if(job is None):
            return 'Jobs Not Found',404
        session.delete(job)
        session.commit()
        return 'Job Deleted',200

api.add_resource(Job, '/api/jobs','/api/jobs/<string:id>')

def main():
    init_db();
    start_job()
    app.run(host='0.0.0.0',port=8080,debug=True)

if __name__ == '__main__':
    main()