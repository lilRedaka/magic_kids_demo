from flask import Flask, request, jsonify
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/magic"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

Base = declarative_base()
engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"], echo=True)
SessionLocal = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    gender = Column(String(10), nullable=False)


Base.metadata.create_all(engine)


@app.route("/get_user_list", methods=["GET"])
def get_user_list():
    session = SessionLocal()
    users = session.query(User).all()
    user_list = [{"id": u.id, "name": u.name, "gender": u.gender} for u in users]
    session.close()
    return jsonify(user_list)


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    new_user = User(name=data["name"], gender=data["gender"])
    session = SessionLocal()
    session.add(new_user)
    session.commit()
    session.close()
    return jsonify({"message": "User added successfully"}), 201


@app.route("/edit_user/<int:id>", methods=["PUT"])
def edit_user(id):
    data = request.get_json()
    session = SessionLocal()
    user = session.query(User).get(id)
    if not user:
        session.close()
        return jsonify({"message": "User not found"}), 404
    user.name = data["name"]
    user.gender = data["gender"]
    session.commit()
    session.close()
    return jsonify({"message": "User updated successfully"})


if __name__ == "__main__":
    app.run(debug=True)
