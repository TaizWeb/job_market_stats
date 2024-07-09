"""Big boy library of popular search terms"""

TECHS = {
    "languages": [
        {"name": "Python", "case_sensitive": False, "aliases": []},
        {"name": "JavaScript", "case_sensitive": False, "aliases": []},
        {"name": "Java", "case_sensitive": False, "aliases": []},
        {"name": "C#", "case_sensitive": False, "aliases": []},
        {"name": "C++", "case_sensitive": False, "aliases": []},
        {"name": "Go", "case_sensitive": True, "aliases": []},
        {"name": "Kotlin", "case_sensitive": False, "aliases": []},
        {"name": "Swift", "case_sensitive": True, "aliases": []},
        {"name": "TypeScript", "case_sensitive": False, "aliases": []},
        {"name": "Ruby", "case_sensitive": False, "aliases": []},
        {"name": "PHP", "case_sensitive": False, "aliases": []},
        {"name": "Rust", "case_sensitive": False, "aliases": []},
        {"name": "Lua", "case_sensitive": False, "aliases": []},
        {"name": "Matlab", "case_sensitive": False, "aliases": []},
        {"name": "C", "case_sensitive": True, "aliases": []},
    ],
    "frameworks": [
        {"name": "Django", "case_sensitive": False, "aliases": []},
        {"name": "Flask", "case_sensitive": False, "aliases": []},
        {"name": "React", "case_sensitive": False, "aliases": []},
        {"name": "Angular", "case_sensitive": False, "aliases": []},
        {"name": "Vue", "case_sensitive": False, "aliases": []},
        {"name": "Node", "case_sensitive": False, "aliases": []},
        {"name": "Spring Boot", "case_sensitive": False, "aliases": []},
        {"name": "Express", "case_sensitive": False, "aliases": []},
        {"name": "Laravel", "case_sensitive": False, "aliases": []},
        {"name": "Ruby on Rails", "case_sensitive": False, "aliases": []},
        {"name": "Swing", "case_sensitive": False, "aliases": []},
        {"name": "ASP.NET", "case_sensitive": False, "aliases": []},
        {"name": "TensorFlow", "case_sensitive": False, "aliases": []},
        {"name": "PyTorch", "case_sensitive": False, "aliases": []},
        {"name": "Electron", "case_sensitive": False, "aliases": []},
        {"name": "Ember", "case_sensitive": False, "aliases": []},
    ],
    "databases": [
        {"name": "Postgres", "case_sensitive": False, "aliases": []},
        {"name": "MySQL", "case_sensitive": False, "aliases": []},
        {"name": "SQLite", "case_sensitive": False, "aliases": []},
        {"name": "MongoDB", "case_sensitive": False, "aliases": []},
        {"name": "Redis", "case_sensitive": False, "aliases": []},
        {"name": "Oracle", "case_sensitive": False, "aliases": []},
        {"name": "Microsoft SQL Server", "case_sensitive": False, "aliases": []},
        {"name": "Cassandra", "case_sensitive": False, "aliases": []},
        {"name": "Elasticsearch", "case_sensitive": False, "aliases": []},
        {"name": "Firebase", "case_sensitive": False, "aliases": []},
        {"name": "MariaDB", "case_sensitive": False, "aliases": []},
        {"name": "DynamoDB", "case_sensitive": False, "aliases": []},
        {"name": "Couchbase", "case_sensitive": False, "aliases": []},
        {"name": "Neo4j", "case_sensitive": False, "aliases": []},
    ],
    "web": [
        "HTML",
        {"name": "CSS", "case_sensitive": False, "aliases": []},
        {"name": "Sass", "case_sensitive": False, "aliases": []},
        {"name": "Less", "case_sensitive": False, "aliases": []},
        {"name": "Svelte", "case_sensitive": False, "aliases": []},
        {"name": "Bootstrap", "case_sensitive": False, "aliases": []},
        {"name": "Tailwind", "case_sensitive": False, "aliases": []},
        {"name": "Webpack", "case_sensitive": False, "aliases": []},
        {"name": "Babel", "case_sensitive": False, "aliases": []},
        {"name": "Gulp", "case_sensitive": False, "aliases": []},
        {"name": "npm", "case_sensitive": False, "aliases": []},
        {"name": "Yarn", "case_sensitive": False, "aliases": []},
        {"name": "Next.js", "case_sensitive": False, "aliases": []},
        {"name": "Nuxt.js", "case_sensitive": False, "aliases": []},
        {"name": "Gatsby", "case_sensitive": False, "aliases": []},
    ],
    "old_js_frameworks": [
        {"name": "Ember.js", "case_sensitive": False, "aliases": []},
        {"name": "Backbone.js", "case_sensitive": False, "aliases": []},
        {"name": "Knockout.js", "case_sensitive": False, "aliases": []},
        {"name": "Aurelia", "case_sensitive": False, "aliases": []},
        {"name": "Meteor", "case_sensitive": False, "aliases": []},
        {"name": "Durandal", "case_sensitive": False, "aliases": []},
        {"name": "Ractive.js", "case_sensitive": False, "aliases": []},
        {"name": "CanJS", "case_sensitive": False, "aliases": []},
        {"name": "Marionette.js", "case_sensitive": False, "aliases": []},
        {"name": "Spine.js", "case_sensitive": False, "aliases": []},
    ],
    "mobile": [
        {"name": "Flutter", "case_sensitive": False, "aliases": []},
        {"name": "React Native", "case_sensitive": False, "aliases": []},
        {"name": "Swift", "case_sensitive": False, "aliases": []},
        {"name": "Android", "case_sensitive": False, "aliases": []},
        {"name": "Kotlin", "case_sensitive": False, "aliases": []},
    ],
    "misc": [
        {"name": "Jenkins", "case_sensitive": False, "aliases": []},
        {"name": "Docker", "case_sensitive": False, "aliases": []},
        {"name": "Kubernetes", "case_sensitive": False, "aliases": []},
        {"name": "Ansible", "case_sensitive": False, "aliases": []},
        {"name": "Terraform", "case_sensitive": False, "aliases": []},
        {"name": "GitLab CI", "case_sensitive": False, "aliases": []},
        {"name": "Travis CI", "case_sensitive": False, "aliases": []},
        {"name": "AWS", "case_sensitive": False, "aliases": []},
        {"name": "Azure", "case_sensitive": False, "aliases": []},
        {"name": "Google Cloud Platform", "case_sensitive": False, "aliases": []},
        {"name": "IBM Cloud", "case_sensitive": False, "aliases": []},
        {"name": "Git", "case_sensitive": False, "aliases": []},
        {"name": "GitHub", "case_sensitive": False, "aliases": []},
        {"name": "GitLab", "case_sensitive": False, "aliases": []},
        {"name": "Bitbucket", "case_sensitive": False, "aliases": []},
        {"name": "JUnit", "case_sensitive": False, "aliases": []},
        {"name": "PyTest", "case_sensitive": False, "aliases": []},
        {"name": "Selenium", "case_sensitive": False, "aliases": []},
        {"name": "Mocha", "case_sensitive": False, "aliases": []},
        {"name": "Jasmine", "case_sensitive": False, "aliases": []},
        {"name": "Jest", "case_sensitive": False, "aliases": []},
        {"name": "RSpec", "case_sensitive": False, "aliases": []},
        {"name": "Xamarin", "case_sensitive": False, "aliases": []},
        {"name": "Pandas", "case_sensitive": False, "aliases": []},
        {"name": "NumPy", "case_sensitive": False, "aliases": []},
        {"name": "Scikit-Learn", "case_sensitive": False, "aliases": []},
        {"name": "TensorFlow", "case_sensitive": False, "aliases": []},
        {"name": "PyTorch", "case_sensitive": False, "aliases": []},
        {"name": "Keras", "case_sensitive": False, "aliases": []},
        {"name": "REST", "case_sensitive": False, "aliases": []},
        {"name": "GraphQL", "case_sensitive": False, "aliases": []},
        {"name": "SOAP", "case_sensitive": False, "aliases": []},
        {"name": "Wordpress", "case_sensitive": False, "aliases": []},
    ],
}
