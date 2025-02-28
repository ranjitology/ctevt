import csv
from jinja2 import Template

# Load the HTML template
html_template = """ 
<div class="container">
    <div class="header_1">
        <img src="https://itms.ctevt.org.np:5580/itmsAdmin/public/img/logo.gif" width="120px">
    </div>
    <div class="header_2">
        <span class="sub_head"><br> COUNCIL FOR TECHNICAL EDUCATION AND VOCATIONAL TRAINING</span><br>
        <span class="sub_head">OFFICE OF THE CONTROLLER OF EXAMINATIONS</span><br>
        <span class="sub_head">SANOTHIMI, BHAKTAPUR</span><br>
        <span class="sub_head">Diploma/PCL Level Regular Exam</span><br>
        <span class="sub_head"><strong>Exam Admit Card - 2081</strong></span>
    </div>

    <div style="border-top:2px solid #000;margin-top:10px;margin-bottom: 10px;"></div> 

    <div>
        <div style="float:left; width:600px;">
            <span>Symbol Number: <strong>{{ symbol }}</strong></span><br>
            <span>Registration Number: <strong>{{ registration }}</strong></span><br>
            <span>Name of Student: <strong>{{ name }}</strong></span><br>
            <span>Program: {{ program }}</span><br>
            <span>Semester: {{ semester }}</span><br>
            <span>Institution: {{ institution }}</span><br>
            <span>Exam Center: {{ exam_center }}</span><br>
            <span>Exam Time: {{ exam_time }}</span><br>
        </div>

        <div class="layered-image">
            <img src="https://itms.ctevt.org.np:5580/itmsAdmin/public/img/entrance/{{ name.replace(' ', '_') }}.jpeg" class="image-base img-responsive" width="120px" height="120px">
        </div>

        <table width="100%" border="1" style="margin-top:10px;">
            <tr>
                <td align="center">S.N.</td>
                <td>Subjects Code</td>
                <td>Subjects</td>
                <td align="center">Exam Date (B.S.)</td>
            </tr>
            {% for subject in subjects %}
            <tr>
                <td align="center">{{ loop.index }}</td>
                <td>{{ subject[0] }}</td>
                <td>{{ subject[1] }}</td>
                <td>{{ subject[2] }}</td>
            </tr>
            {% endfor %}
        </table>
    </div>
</div>
"""

# Read CSV and generate admit cards
with open('students.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Parse subjects
        subjects = [s.split('|') for s in row["Subjects"].split(";")]

        # Render HTML
        template = Template(html_template)
        html_content = template.render(
            symbol=row["Symbol Number"],
            registration=row["Registration Number"],
            name=row["Name"],
            program=row["Program"],
            semester=row["Semester"],
            institution=row["Institution"],
            exam_center=row["Exam Center"],
            exam_time=row["Exam Time"],
            subjects=subjects
        )

        # Save to an HTML file
        filename = f"admit_card_{row['Symbol Number']}.html"
        with open(filename, "w", encoding="utf-8") as output_file:
            output_file.write(html_content)

        print(f"Generated: {filename}")
