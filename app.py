from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data structure to store house rules and jobs
house_rules = {}
jobs = []


@app.route('/')
def index():
    return render_template('index.html', house_rules=house_rules, jobs=jobs)


@app.route('/post_job', methods=['GET', 'POST'])
def post_job():
    if request.method == 'POST':
        house_number = request.form['house_number']
        street = request.form['street']
        city = request.form['city']
        caregiving_type = request.form['caregiving_type']
        job = {
            'house_number': house_number,
            'street': street,
            'city': city,
            'caregiving_type': caregiving_type,
        }
        jobs.append(job)
        return redirect(url_for('index'))
    return render_template('post_job.html')


@app.route('/search_job')
def search_job():
    return render_template('search_job.html', jobs=jobs)


@app.route('/apply_to_job/<int:job_index>')
def apply_to_job(job_index):
    job = jobs[job_index]
    return render_template('apply_to_job.html', job=job)


# Other routes and functions for appointment, logout, etc. can be added similarly

if __name__ == '__main__':
    app.run(debug=True)
