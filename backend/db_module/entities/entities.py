from backend.db_module.entities import db_entities
from backend.db_module import db


class User(db_entities.User):
    def __repr__(self):
        return 'User<id {}>'.format(self.id)

    def to_dict(self):
        return {
            "id": self.id,
            "login": self.login,
            "password": self.password,
            "access_level": self.access_level,
        }


class Patient(db_entities.Patient):
    user = db.relationship('entities.User',
                           primaryjoin="foreign(entities.Patient.user_id) == entities.User.id",
                           uselist=False, passive_deletes=True)

    def __repr__(self):
        return 'Patient<id {}>'.format(self.id)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "policy_num": self.policy_num,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "middle_name": self.middle_name,
            "gender": self.gender,
            "age": self.age,
            "weight": self.weight,
            "height": self.height,
            "has_nuo": self.has_nuo,
            "prob_log_reg": self.prob_log_reg,
            "prob_rnd_forest": self.prob_rnd_forest,
            "prob_log_svm": self.prob_log_svm,
        }


class Doctor(db_entities.Doctor):
    user = db.relationship('entities.User',
                           primaryjoin="foreign(entities.Doctor.user_id) == entities.User.id",
                           uselist=False, passive_deletes=True)

    def __repr__(self):
        return 'Doctor<id {}>'.format(self.id)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "full_name": self.full_name,
            "cabinet": self.cabinet,
            "telephone": self.telephone,
        }


class EKG(db_entities.EKG):
    patient = db.relationship('entities.Patient',
                              primaryjoin="foreign(entities.EKG.user_id) == entities.Patient.id",
                              passive_deletes=True)

    def __repr__(self):
        return 'EKG<id {}>'.format(self.id)

    def to_dict(self):
        return {
            "id": self.id,
            "patient_id": self.patient_id,
            "date": self.date,
            "sdnn": self.sdnn,
            "skewness": self.skewness,
            "amo": self.amo,
            "swai": self.swai,
            "mo": self.mo,
            "drr": self.drr,
            "rrnn": self.rrnn,
            "pnn50": self.pnn50,
            "si": self.si,
            "sati": self.sati,
            "rmi": self.rmi,
            "kurtosis": self.kurtosis,
            "cv": self.cv,
            "rmssd": self.rmssd,
            "nn50": self.nn50,
            "lf": self.lf,
            "lfhf": self.lfhf,
            "hfp": self.hfp,
            "ulf": self.ulf,
            "tp": self.tp,
            "vlf": self.vlf,
            "vlfp": self.vlfp,
            "lfp": self.lfp,
            "br": self.br,
            "ulfp": self.ulfp,
            "ic": self.ic,
            "hf": self.hf,
            "tpfull": self.tpfull,
            "p_left_slopes": self.p_left_slopes,
            "p_right_slopes": self.p_right_slopes,
            "q_left_slopes": self.q_left_slopes,
            "q_right_slopes": self.q_right_slopes,
            "t_left_slopes": self.t_left_slopes,
            "t_right_slopes": self.t_right_slopes,
            "qt": self.qt,
            "st": self.st,
            "p": self.p,
            "pq": self.pq,
            "qrs": self.qrs,
            "pulse": self.pulse,
        }
