COURSES = {

    "Python Developer":[
        "Advanced Python",
        "Flask Development",
        "Docker Essentials",
        "REST API Design"
    ],

    "Data Science":[
        "Machine Learning",
        "Deep Learning",
        "Power BI",
        "SQL for Data Science"
    ],

    "Java Developer":[
        "Spring Boot",
        "Hibernate",
        "Microservices",
        "Docker"
    ],

    "DevOps Engineer":[
        "AWS",
        "Kubernetes",
        "Terraform",
        "CI/CD"
    ]
}


def get_recommendations(role):

    return COURSES.get(role, [])