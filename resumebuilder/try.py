from weasyprint import HTML

name = "Madhav Gupta"
contact_num = "+91 7845458887"
email = "madhav.gupta@email.com"
linkedIn = "linkedin.com/in/madhavgupta"

profile_sum = (
    "Highly skilled full-stack software engineer with over 5 years of professional "
    "experience designing, developing, and deploying scalable web applications. "
    "Proven expertise in backend architecture, RESTful API development, database "
    "optimization, and cloud deployment. Adept at collaborating with cross-functional "
    "teams, mentoring junior engineers, and translating complex business requirements "
    "into efficient technical solutions. Strong advocate of clean code, system design "
    "best practices, and continuous learning."
)

education_list = [
    "Bachelor of Science in Computer Science, Stanford University (2015–2019) | "
    "GPA: 3.8/4.0 | Coursework: Data Structures, Algorithms, Operating Systems, "
    "Database Systems, Computer Networks",

    "Master of Science in Software Engineering, Massachusetts Institute of Technology (MIT) "
    "(2019–2021) | Specialization: Distributed Systems & Cloud Computing | "
    "Thesis: Scalable Microservices Architecture for High-Traffic Applications"
]

work_exp_list = [
    "Senior Software Engineer, Tech Corp (2021–Present) – "
    "Architected and led development of cloud-based, microservices-driven applications "
    "serving over 500k monthly users. Designed REST and GraphQL APIs, improved backend "
    "performance by 30%, implemented CI/CD pipelines using GitHub Actions, and reduced "
    "production incidents by 40%. Mentored a team of 5 junior engineers and conducted "
    "code reviews to maintain high engineering standards.",

    "Software Developer, StartUp Inc (2019–2021) – "
    "Developed scalable backend services using Python and Django, integrated modern "
    "frontend interfaces using React, and collaborated closely with product and design "
    "teams. Optimized database queries resulting in a 25% reduction in response time "
    "and played a key role in deploying applications on AWS infrastructure."
]

skills_list = [
    "Python",
    "JavaScript",
    "TypeScript",
    "React",
    "Django",
    "FastAPI",
    "REST APIs",
    "SQL",
    "PostgreSQL",
    "MySQL",
    "AWS",
    "Docker",
    "Kubernetes",
    "Git",
    "CI/CD",
    "System Design",
    "Microservices Architecture"
]

projects_list = [
    "Scalable E-commerce Platform – Designed and implemented a full-stack e-commerce "
    "application supporting 10k+ active users, featuring secure payment processing, "
    "role-based access control, order management, and real-time inventory updates.",

    "Collaborative Task Management System – Built a web-based project tracking tool "
    "with real-time collaboration, user roles, and notification services using WebSockets "
    "and REST APIs. Improved team productivity by streamlining task workflows.",

    "Resume Builder Application – Developed a dynamic resume generation system capable "
    "of producing ATS-friendly PDFs from structured user input using Python and ReportLab."
]

achievements_list = [
    "Employee of the Year 2023 at Tech Corp for outstanding technical leadership and "
    "project delivery excellence",

    "Published 3 in-depth technical articles on Medium with over 50,000 cumulative views, "
    "covering backend scalability, API design, and cloud best practices",

    "Active contributor to 5+ open-source projects on GitHub, including bug fixes, "
    "feature enhancements, and documentation improvements",

    "Speaker at internal tech talks and developer meetups on system design and backend "
    "performance optimization"
]

# name=input("Enter your name: ")
# contact_num=input("Enter your contact number: ")
# email=input("Enter your email address: ")
# linkedIn=input("Enter your linkeIn profile:")
# profile_sum=input("Enter a brief profile summary: ")
# education_num=input("Enter number of educational qualifications: ")
# education_list=[]
# for i in range(int(education_num)):
#     education=input("Enter your educational qualifications: ")
#     education_list.append(education)
# work_exp_num=input("Enter number of work experiences: ")
# work_exp_list=[]
# for i in range(int(work_exp_num)):
#     work_exp=input("Enter your work experience: ")
#     work_exp_list.append(work_exp)
# skills_num=input("Enter number of skills: ")
# skills_list=[]
# for i in range(int(skills_num)):
#     skill=input("Enter your skill: ")
#     skills_list.append(skill)
# projects_num=input("Enter number of projects: ")
# projects_list=[]
# for i in range(int(projects_num)):
#     project=input("Enter your project: ")
#     projects_list.append(project)
# achievements_num=input("Enter number of achievements: ")
# achievements_list=[]
# for i in range(int(achievements_num)):
#     achievement=input("Enter your achievement: ")
#     achievements_list.append(achievement)

def create_html_list(ele_list):
    final=""
    for ele in ele_list:
        final+="<li>"+ele+"</li><br>"
    return final

html=f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resume</title>
    <link rel="stylesheet" href="styles.css">
</head>
<style>
@page {{
    size: A4;
    margin: 40px;
}}

h1{{
    text-align: center;
}}
.contact-section{{

    list-style-type:none;
    display: flex;
    justify-content: space-around;
}}
</style>
<body>
    <section class="resume-layout">
        <header>
            <h1 class="name" >{name}</h1>

            <hr>
            <div class="contact-section">
                <li >
                    {contact_num}
                </li>
                <li>|</li>
                <li>
                    {email}
                </li>
                <li>|</li>
                
                <li>
                    {linkedIn}
                </li>
                <br>
            </div>
            <hr>
        </header>
        <section class="profile-section">
            <h2>Profile Summary</h2>
            <hr>
            <p>{profile_sum}</p>
        </section>
        <section class="education-section">
            <h2>Education</h2>
            <hr>
            <ul>
            {create_html_list(education_list)}
            </ul>
        </section>
        
        <section class="education-section">
            <h2>Experience</h2>
            <hr>
            <ul>
            {create_html_list(work_exp_list)}
            </ul>
        </section>
        <section class="project-section">
            <h2>Project</h2>
            <hr>
            <ul>
            {create_html_list(projects_list)}
            </ul>
        </section>
        <section class="skills">
            <h2>Skills</h2>
            <hr>
            <ul>
            <span class="skill-list">
            {create_html_list(skills_list)}
            </span>
            </ul>
        </section>
        <section class="skills">
            <h2>Achievements</h2>
            <hr>
            <ul>
            <span class="skill-list">
            {create_html_list(achievements_list)}
            </span>
            </ul>
        </section>

    </section>

</body>
</html>"""
HTML(string=html,).write_pdf(f"resume_{name}.pdf")

