from flask_sqlalchemy import SQLAlchemy

# 创建数据库对象
db = SQLAlchemy()


# 创建人员图片模型
class PersonImg(db.Model):
    __tablename__ = "person_img"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img_path = db.Column(db.String(255))
    # 外键
    person_id = db.Column(db.Integer)
    add_entrance_guard = db.Column(db.String(255))
    start_date = db.Column(db.String(255))
    end_date = db.Column(db.String(255))
    # 连接关系
    # person = db.relationship("PersonInfo", backref=db.backref("img_path", uselist=False))


# 创建角色ID绑定模型
class RoleId(db.Model):
    __tablename__ = "role_id"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    local_role_id = db.Column(db.Integer)
    dahua_role_id = db.Column(db.Integer)


# 创建人员模型
class PersonInfo(db.Model):
    __tablename__ = "personinfo"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idno = db.Column(db.String(100))
    name = db.Column(db.String(255))
    sex = db.Column(db.Boolean)
    phone = db.Column(db.String(100))
    deptid = db.Column(db.Integer)
    dutyid = db.Column(db.Integer)
    deleted = db.Column(db.Boolean)


# 创建标签模型
class TagidInfo(db.Model):
    __tablename__ = "taginfo"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tagid = db.Column(db.String(8))
    kind = db.Column(db.SmallInteger)
    bindid = db.Column(db.Integer)
    status = db.Column(db.SmallInteger)
    used = db.Column(db.SmallInteger)
    remark = db.Column(db.String(255))
    deleted = db.Column(db.SmallInteger)


# 创建角色模型
class DutyInfo(db.Model):
    __tablename__ = "dutyinfo"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    level = db.Column(db.SmallInteger)


# 创建人员id绑定模型
class PersonId(db.Model):
    __tablename__ = "personid"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    local_id = db.Column(db.Integer)
    dahua_id = db.Column(db.String(255))
