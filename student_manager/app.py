from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []


def calculate_grade(marks):
    marks = float(marks)

    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


@app.route("/", methods=["GET", "POST"])
def dashboard():
    global students

    if request.method == "POST":
        action = request.form.get("action")

        if action == "add":
            name = request.form.get("name")
            marks = request.form.get("marks")

            if name and marks:
                marks = float(marks)
                grade = calculate_grade(marks)

                students.append({
                    "id": len(students) + 1,
                    "name": name,
                    "marks": marks,
                    "grade": grade
                })

        elif action == "delete":
            student_id = int(request.form.get("id"))
            students[:] = [s for s in students if s["id"] != student_id]

        return redirect("/")

    # Search logic
    search_query = request.args.get("search", "")

    if search_query:
        filtered_students = [
            s for s in students
            if search_query.lower() in s["name"].lower()
        ]
    else:
        filtered_students = students

    return render_template("dashboard.html", students=filtered_students)


if __name__ == "__main__":
    app.run(debug=True)
