from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database
students_data = {
    1: {"id": 1, "name": "John", "section": "A", "marks": {"math": 90, "science": 85}},
    2: {"id": 2, "name": "Alice", "section": "B", "marks": {"math": 80, "science": 75}},
    # Add more student data as needed
}

# Authentication middleware
def authenticate(role):
    # Implement your authentication logic here
    # For simplicity, assume authentication is successful for all roles
    return True

# Authorization middleware
def authorize(role, college_id=None, section=None, student_id=None):
    if role == "super_admin":
        return True
    elif role == "admin" and college_id is not None:
        # Check if admin has access to specified college
        return True
    elif role == "teacher" and section is not None:
        # Check if teacher has access to specified section
        return True
    elif role == "student" and student_id is not None:
        # Check if student is accessing own data
        return True
    return False

# READ Data endpoints
@app.route("/api/students", methods=["GET"])
def get_all_students():
    if authenticate("super_admin"):
        return jsonify(list(students_data.values()))

@app.route("/api/colleges/<int:college_id>/students", methods=["GET"])
def get_college_students(college_id):
    if authenticate("admin") and authorize("admin", college_id=college_id):
        return jsonify([student for student in students_data.values() if student["college_id"] == college_id])

@app.route("/api/students/section/<section>", methods=["GET"])
def get_section_students(section):
    if authenticate("teacher") and authorize("teacher", section=section):
        return jsonify([student for student in students_data.values() if student["section"] == section])

@app.route("/api/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    if authenticate("student") and authorize("student", student_id=student_id):
        return jsonify(students_data.get(student_id))

# WRITE Data endpoint (Only available for super_admin and admin)
@app.route("/api/students", methods=["POST"])
def create_student():
    role = request.headers.get("Role")
    if authenticate(role) and (role == "super_admin" or role == "admin"):
        # Implement create student logic here
        return jsonify({"message": "Student created successfully"}), 201
    else:
        return jsonify({"error": "Unauthorized"}), 403

# UPDATE Data endpoint (Only available for super_admin and admin)
@app.route("/api/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    role = request.headers.get("Role")
    if authenticate(role) and (role == "super_admin" or role == "admin"):
        # Implement update student logic here
        return jsonify({"message": "Student updated successfully"})
    else:
        return jsonify({"error": "Unauthorized"}), 403

# DELETE Data endpoint (Only available for super_admin and admin)
@app.route("/api/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    role = request.headers.get("Role")
    if authenticate(role) and (role == "super_admin" or role == "admin"):
        # Implement delete student logic here
        return jsonify({"message": "Student deleted successfully"})
    else:
        return jsonify({"error": "Unauthorized"}), 403

if __name__ == "__main__":
    app.run(debug=True)
