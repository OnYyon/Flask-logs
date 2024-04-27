from flask import Flask, render_template

from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def log():
    jobs = Jobs()
    db_sess = db_session.create_session()
    lst = []
    for job in db_sess.query(Jobs).all():
        lst.append([job.team_leader, job.job, job.work_size, job.collaborators, job.start_date, job.end_date,
                job.is_finished])
    return render_template("logs.html", data=lst, columns=["team_leader", "job", "work_size", "collabarators", "start_date",
                                                           "end_date", "is_finished"])


def main():
    db_session.global_init("db/mars_explorer.db")
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
