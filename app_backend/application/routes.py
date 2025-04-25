from flask import jsonify, request,make_response,render_template
from application.model import *
from application.database import db
import uuid
from flask_security import auth_token_required, current_user
from flask_security.utils import verify_password, login_user

from datetime import datetime
import csv, os
def register_routes(app):
    @app.after_request
    def add_cors_headers(response):
        response.headers["Access-Control-Allow-Origin"] = "*"  # Allow frontend
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS,PUT"  # Allowed methods
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"  # Allowed headers
        return response

    @app.route("/add_data",methods=['POST'])
    def adder():
        data=request.get_json()
        type=data.get('type')
        if type=="Subject":
            sub=Subject(
                subject=data.get('title'),
                description=data.get('description')
            )
            db.session.add(sub)
            db.session.commit()
            return jsonify({'msg':"Added Successfully"}),200
        elif type=="Chapter":
            chapt=Chapter(
                subject_id=data.get('subject_id'),
                chapter=data.get('chapter')
            )
            db.session.add(chapt)
            db.session.commit()
            return jsonify({'msg':"Added Successfully"}),200
        elif type=="Question":
            question=Question(
                chapter_id=data.get('chapter_id'),
                question=data.get('question'),
                options=data.get('options'),
                correct=data.get('correct'),

            )
            db.session.add(question)
            db.session.commit()
            return jsonify({'msg':"Added Successfully"}),200
        else:
            return jsonify({'msg':'BAD Request'}) , 401
    @app.route("/get", methods=['GET'])
    def info():
        return jsonify({'id': str(uuid.uuid4())})
    @app.route('/signup',methods=['POST'])
    def signup():
        data=request.get_json()
        email=data.get('email')
        password=data.get('password')
        username=data.get('username')
        user=User(
            email=email,
            password=password,
            username=username,
            active=1,
            confirmed_at=datetime.utcnow(),
            fs_uniquifier=str(uuid.uuid4()),
        )
        db.session.add(user)
        db.session.commit()
        default_role = Role.query.get(2)
        if default_role:
            user.roles.append(default_role)
            db.session.commit()
        return jsonify({"msg":"User created Successfully"})
    @app.route("/post", methods=['POST'])
    def get_data():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        user = app.extensions['security'].datastore.find_user(email=email)
        if user and verify_password(password, user.password):
            login_user(user)
            token = user.get_auth_token()
            print(token)
            roles = [role.name for role in user.roles]
            return jsonify({'token': token,'name':user.username,'id':user.id,'role':roles[0]}), 200
        else:
            return jsonify({"msg": "Bad email or password"}), 401
    @app.route('/get_sub', methods=['GET'])
    def send_sub():
        subjects = Subject.query.all()
        sub_data = []
        for subject in subjects:
            chapters = Chapter.query.filter_by(subject_id=subject.id).all()
            chapter_data = [{"id": chapter.id, "chapter": chapter.chapter} for chapter in chapters]
            sub_data.append({
                "id": subject.id,
                "title": subject.subject,
                "description": subject.description,
                "chapters": chapter_data
            })
        return jsonify(sub_data)
    @app.route('/get_question',methods=['GET','POST'])
    def send_quest():
        data = request.get_json()
        chapter = data.get('chapter')
        questions = Question.query.filter_by(chapter_id=chapter).all()
        question_list = [{"id": question.id, "question": question.question, "options":question.options} for question in questions]
        return jsonify(question_list)
    @app.route('/score', methods=['POST'])
    def check():
        data = request.get_json()
        score = 0
        subject_name = None
        chapter_name = None
        for qid, answer in data.items():
            question = Question.query.filter_by(id=qid).first()
            if question:
                subject_name = question.chapter_ref.subject_ref.subject
                chapter_name = question.chapter_ref.chapter
                if question.correct == answer:
                    score += 1
        if subject_name and chapter_name:
            new_score = Score(
                user_id=data.get('id'),
                subject=subject_name,
                chapter=chapter_name,
                score=score,
                date=datetime.utcnow()
            )
            db.session.add(new_score)
            db.session.commit()
        return jsonify({"score": score})
    @app.route('/delete',methods=['GET','POST'])
    def delete():
        data=request.get_json()
        type=data.get('type')
        id=data.get('id')
        if type=="Subject":
            to_del=Subject.query.filter_by(id=id).first()
            db.session.delete(to_del)
            db.session.commit()
            return jsonify({'msg':"Added Successfully"}),200
        elif type=="Chapter":
            to_del=Chapter.query.filter_by(id=id).first()
            db.session.delete(to_del)
            db.session.commit()
            return jsonify({'msg':"Added Successfully"}),200
        elif type=="Question":
            to_del=Question.query.filter_by(id=id).first()
            db.session.delete(to_del)
            db.session.commit()
            return jsonify({'msg':"Added Successfully"}),200
        else:
            return jsonify({'msg':'BAD Request'}) , 401
    @app.route('/get_score',methods=['POST'])
    def scorecard():
        score_data=[]
        data=request.get_json()
        user_id=data.get('user_id')
        scores=Score.query.filter_by(user_id=user_id).order_by(Score.date.desc()).all()
        for row in scores:
            chapt=Chapter.query.filter_by(chapter=row.chapter).first()
            if chapt:
                outof= Question.query.filter_by(chapter_id=chapt.id).count()
            else:
                outof="Not available"
            score_data.append({"date":row.date,"subject":row.subject,"chapter":row.chapter,"score":row.score,"outof":outof})
        return jsonify(score_data)
    @app.route('/stat',methods=['POST'])
    def stat():
        data=request.get_json()
        user_id=data.get('id')
        user = User.query.get(user_id)
        subjects = Subject.query.all()
        scores = Score.query.filter_by(user_id=user_id).all()

        row = {
            'name': user.username,
            'user_id': user.id,
            'current_date': datetime.now().strftime('%Y-%m-%d'),
            'subjects': []
        }

        for subject in subjects:
            subject_scores = [score for score in scores if score.subject == subject.subject]
            total_chapters = len(subject.chapters)
            attempted_chapters = len(subject_scores)
            total_score = sum(score.score for score in subject_scores)
            outof=sum(len(chapter.questions) for chapter in subject.chapters)
            row['subjects'].append({
                'name': subject.subject,
                'total_chapters': total_chapters,
                'attempted_chapters': attempted_chapters,
                'score': total_score,
                'outof':outof
            })

        return jsonify(row)
    @app.route('/update', methods=['PUT'])
    def update():
        data = request.get_json()
        print(data)
        type = data.get('type')

        if type == "Subject":
            subject_id = data.get('id')
            subject = Subject.query.get(subject_id)
            if not subject:
                return jsonify({'msg': 'Subject not found'}), 404

            # Update fields if provided
            subject.subject = data.get('title', subject.subject)
            subject.description = data.get('description', subject.description)
            db.session.commit()
            return jsonify({'msg': 'Subject updated successfully'}), 200

        elif type == "Chapter":
            chapter_id = data.get('chapter_id')
            chapter = Chapter.query.get(chapter_id)
            if not chapter:
                return jsonify({'msg': 'Chapter not found'}), 404
            chapter.chapter = data.get('chapter', chapter.chapter)
            db.session.commit()
            return jsonify({'msg': 'Chapter updated successfully'}), 200

        elif type == "Question":
            question_id = data.get('id')
            question = Question.query.get(question_id)
            if not question:
                return jsonify({'msg': 'Question not found'}), 404
            question.question = data.get('question', question.question)
            question.options = data.get('options', question.options)
            question.correct = data.get('correct', question.correct)
            db.session.commit()
            return jsonify({'msg': 'Question updated successfully'}), 200

        else:
            return jsonify({'msg': 'Invalid type provided'}), 400
    @app.route('/admin_summary', methods=['GET'])
    def admin_summary():
        user_count = User.query.count()  # Total number of users
        subjects = Subject.query.all()  # List of subjects

        data = {
            "user_count": user_count,
            "subjects": [
                {"name": subject.subject, "chapter_count": len(subject.chapters)}
                for subject in subjects
            ]
        }
        return jsonify(data)
    @app.route('/protected', methods=['GET'])
    @auth_token_required
    def protected():
        return jsonify(logged_in_as=current_user.email), 200