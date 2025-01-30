from flask import Flask, render_template
import requests

app = Flask(__name__)

API_BASE_URL = "http://127.0.0.1:8000//api"  # Replace with the actual API base URL

@app.route('/')
def dashboard():
    # Fetch data from Django API
    students = requests.get(f"{API_BASE_URL}/students/").json()
    subjects = requests.get(f"{API_BASE_URL}/subjects/").json()
    grades = requests.get(f"{API_BASE_URL}/grades/").json()

    # Organize grades by student
    student_grades = {student['id']: [] for student in students}
    for grade in grades:
        student_grades[grade['student']].append(grade['grade'])

    # Calculate averages
    averages = {
        student_id: sum(grades) / len(grades) if grades else 0
        for student_id, grades in student_grades.items()
    }

    # Prepare student data for the dashboard
    student_data = [
        {
            "name": next(student['name'] for student in students if student['id'] == student_id),
            "average": average
        }
        for student_id, average in averages.items()
    ]

    return render_template("dash.html", students=student_data, subjects=subjects)

if __name__ == "__main__":
    app.run(debug=True)
