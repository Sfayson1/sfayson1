import json


def load_profile(filename):
    with open(filename, "r") as file:
        data = json.load(file)

    return data


def generate_header(profile):
    banner = """<p align="center">
  <img src="assets/FloridaDev-Sunset-Portfolio-Banner.png" alt="Sherika Fayson - Software Engineer" width="100%">
</p>
"""
    return banner


def generate_summary(profile):
    summary = profile["summary"]
    return f"{summary}\n"


def generate_profile_section(profile):
    section = profile["profile_section"]

    title = section["title"]
    role = section["role"]
    focus = section["focus"]
    status = section["status"]
    location = section["location"]

    focus_string = " · ".join(focus)

    profile_section = f"""<p align="center">
  <img src="assets/section-01-engineer-profile.png" alt="{title}" width="100%">
</p>

<p align="center">
  <strong>{role}</strong> | {focus_string}
  <br><br>
  {profile["summary"]}
  <br><br>
  📍 {location} · 🟢 {status}
</p>
"""

    return profile_section


def generate_links(profile):
    button_files = {
        "Portfolio": "assets/button-portfolio.png",
        "LinkedIn": "assets/button-linkedin.png",
        "Email": "assets/button-email.png",
    }

    links = []

    for label, details in profile["links"].items():
        url = details["url"]
        button_file = button_files[label]

        button = (
            f'<a href="{url}">'
            f'<img src="{button_file}" alt="{label}" height="34">'
            f"</a>"
        )

        links.append(button)

    return f'<p align="center">{" ".join(links)}</p>'


def generate_projects(profile):
    project_section = """<p align="center">
  <img src="assets/section-02-featured-build.png" alt="Featured Build" width="100%">
</p>

"""

    for project in profile["featured_projects"]:
        project_section += '<div align="center">\n\n'

        project_section += f"### {project['name']}\n\n"
        project_section += f"*{project['subtitle']}*\n\n"

        project_section += (
            f'<a href="{project["demo"]}">'
            f'<img src="assets/button-live-demo.png" alt="Live Demo" height="34">'
            f"</a> "
            f'<a href="{project["repository"]}">'
            f'<img src="assets/button-repository.png" alt="Repository" height="34">'
            f"</a>\n\n"
        )

        project_section += f"*{project['role']}*\n\n"
        project_section += "</div>\n\n"

        architecture = " → ".join(project["architecture"])
        engineering = " · ".join(project["engineering"])

        project_section += "<table>\n"
        project_section += "  <tr>\n"

        project_section += (
            f'    <td width="50%"><strong>Problem</strong><br>'
            f'{project["problem"]}</td>\n'
        )

        project_section += (
            f'    <td width="50%"><strong>Built</strong><br>'
            f'{project["built"]}</td>\n'
        )

        project_section += "  </tr>\n"
        project_section += "  <tr>\n"

        project_section += (
            f'    <td width="50%"><strong>Architecture</strong><br>'
            f"{architecture}</td>\n"
        )

        project_section += (
            f'    <td width="50%"><strong>Engineering</strong><br>'
            f"{engineering}</td>\n"
        )

        project_section += "  </tr>\n"
        project_section += "</table>\n"

    return project_section


def generate_skills(profile):
    skills_section = """<p align="center">
  <img src="assets/section-03-engineering-toolkit.png" alt="Engineering Toolkit" width="100%">
</p>

"""

    skills_section += "| **Layer** | **Tools** |\n"
    skills_section += "| ---------- | --------- |\n"

    for category, technologies in profile["skills"].items():
        tech_string = ", ".join(technologies)
        skills_section += f"| **{category}** | {tech_string} |\n"

    return skills_section


def generate_learning(profile):
    learning = """<p align="center">
  <img src="assets/section-04-currently-learning.png" alt="Currently Learning" width="100%">
</p>

"""

    for item in profile["currently_learning"]:
        learning += f"- {item}\n"

    return learning


def generate_education(profile):
    education_section = """<p align="center">
  <img src="assets/section-05-education.png" alt="Education" width="100%">
</p>

"""

    for education in profile["education"]:
        education_section += f"**{education['degree']}**  \n"
        education_section += f"{education['program']}  \n"
        education_section += (
            f"{education['school']} | {education['graduation']}\n\n"
        )

    return education_section


def generate_readme(profile):
    sections = [
        generate_header(profile),
        generate_profile_section(profile),
        generate_links(profile),
        generate_projects(profile),
        generate_skills(profile),
        generate_learning(profile),
        generate_education(profile),
    ]

    sections = [section.strip() for section in sections]

    return "\n\n".join(sections)


def save_readme(filename, content):
    with open(filename, "w") as file:
        file.write(content)


profile = load_profile("profile_data.json")
readme = generate_readme(profile)
save_readme("README.generated.md", readme)
print(readme)
