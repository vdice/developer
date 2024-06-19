import re
import requests

# Function to fetch the content of a file from a GitHub repository
def fetch_file_from_github(repo, filepath):
    url = f"https://raw.githubusercontent.com/{repo}/main/{filepath}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch {filepath} from {repo}")

# Fetching the original Handlebars templates
repo = "fermyon/developer"
spin_sidebar_v2 = fetch_file_from_github(repo, "templates/spin_sidebar_v2.hbs")
cloud_sidebar = fetch_file_from_github(repo, "templates/cloud_sidebar.hbs")

# Parsing the original Handlebars templates to extract links
def extract_links(handlebars_template):
    links = re.findall(r'\{\{\s*#link\s+"(.*?)"\s*\}\}', handlebars_template)
    return links

spin_links = extract_links(spin_sidebar_v2)
cloud_links = extract_links(cloud_sidebar)

# Define the new sidebar structure based on the provided markdown hierarchy
sidebar_structure = {
    "Quick Start - Create Your First App With Spin": [],
    "Wasm Language Guides": [
        "Language Support Overview",
        "Rust",
        "Go",
        "Javascript",
        "Python",
        "Other Languages"
    ],
    "Creating Apps With Spin": {
        "Get Started": [
            "Introduction",
            "Install",
            "Upgrade",
            "Resources (Discord link etc.)"
        ],
        "Concepts": [
            "Learn About Spin App Fundamentals - Trigger, Components, and Application Manifest",
            "Learn About Spin Internal Data Layout",
            "Learn About Spin App Swappable Resources - Runtime configuration"
        ],
        "How To": {
            "Applications": [
                "Writing Applications",
                "Structuring Applications",
                "Compiling Applications",
                "Running Applications",
                "Publishing and Distribution",
                "Observing Applications",
                "Troubleshooting Application Development"
            ],
            "Triggers": [
                "Triggers",
                "The HTTP Trigger",
                "The Redis Trigger",
                "Building Custom Triggers - Extending and Embedding Spin"
            ],
            "API Guides": {
                "API Support Overview": [],
                "Storage": [
                    "Key Value Store",
                    "SQLite Storage",
                    "Redis Storage",
                    "Relational Database Storage"
                ],
                "Outbound connectivity": [
                    "Making HTTP Requests",
                    "MQTT Messaging"
                ],
                "Serverless AI": [],
                "Application Variables": []
            },
            "Tools": {
                "Templates": [
                    "Creating Spin Templates",
                    "Managing Templates"
                ],
                "Plugins": [
                    "Creating Spin Plugins",
                    "Managing Plugins"
                ],
                "Triggers": []
            }
        },
        "Tutorials": [
            "Build Your First Serverless AI App",
            "Sentiment Analysis With Serverless AI",
            "Building a URL Shortener With Spin",
            "Spin Apps in Registries",
            "Spin Key-Value Store"
        ]
    },
    "Deploying your Spin App": {
        "Fermyon Cloud": [
            "Quickstart",
            "Introduction",
            {
                "Applications": [
                    "Develop a Spin Application",
                    "Deploy an Application",
                    "Upgrade an Application",
                    "Delete an Application"
                ],
                "Concepts": [
                    "The Fermyon Cloud",
                    "Deployment Concepts",
                    "Custom Domain",
                    "Linking Apps To Resources Using Labels"
                ],
                "Tutorials": [
                    "Using VS Code Extension",
                    "Cloud Key-Value Store",
                    "Persisting Data With SQLite Database",
                    "Persisting Data With Redis",
                    "Persisting Data With PostgreSQL",
                    "Deploying Spin Apps Using GitHub Action",
                    "Apply Custom Fermyon Subdomain",
                    "Apply Custom Domain",
                    "Configuring App Variables and Secrets"
                ],
                "Support": [
                    "The User Settings Screen",
                    "Quotas, Limitations, and Technical FAQ",
                    "Pricing and Billing",
                    "How to Get Help?"
                ]
            }
        ],
        "Fermyon Platform For Kubernetes": [
            "Kubernetes",
            "Spin on Kubernetes",
            "Spin in Pods (Legacy)"
        ]
    },
    "References": [
        "CLI Reference",
        "Application Manifest (Version 1) Reference",
        "Application Manifest Reference"
    ],
    "Contributing": [
        "Contributing to Docs",
        "Contributing to Spin",
        "Spin Improvement Proposals",
        "Contributing to SpinKube"
    ],
    "Resources": []
}

# Function to generate Handlebars template using actual elements and attributes from the original templates
def generate_handlebars_template(structure, indent=0, idx=0):
    handlebars = ""
    for key, value in structure.items():
        current_id = f"rd{idx}"
        if isinstance(value, dict):
            handlebars += ' ' * indent + f'<div class="accordion-menu-item">\n'
            handlebars += ' ' * indent + f'  <input type="checkbox" id="{current_id}" name="rd">\n'
            handlebars += ' ' * indent + f'  <label for="{current_id}" class="accordion-menu-item-label menu-label">\n'
            handlebars += ' ' * indent + f'    {key}\n'
            handlebars += ' ' * indent + f'  </label>\n'
            handlebars += ' ' * indent + f'  <ul class="menu-list accordion-menu-item-content">\n'
            handlebars += generate_handlebars_template(value, indent + 4, idx + 1)
            handlebars += ' ' * indent + f'  </ul>\n'
            handlebars += ' ' * indent + f'</div>\n'
        elif isinstance(value, list):
            if len(value) > 0 and isinstance(value[0], dict):
                handlebars += ' ' * indent + f'<div class="accordion-menu-item">\n'
                handlebars += ' ' * indent + f'  <input type="checkbox" id="{current_id}" name="rd">\n'
                handlebars += ' ' * indent + f'  <label for="{current_id}" class="accordion-menu-item-label menu-label">\n'
                handlebars += ' ' * indent + f'    {key}\n'
                handlebars += ' ' * indent + f'  </label>\n'
                handlebars += ' ' * indent + f'  <ul class="menu-list accordion-menu-item-content">\n'
                for item in value:
                    handlebars += generate_handlebars_template(item, indent + 4, idx + 1)
                handlebars += ' ' * indent + f'  </ul>\n'
                handlebars += ' ' * indent + f'</div>\n'
            else:
                handlebars += ' ' * indent + f'<div class="accordion-menu-item">\n'
                handlebars += ' ' * indent + f'  <input type="checkbox" id="{current_id}" name="rd">\n'
                handlebars += ' ' * indent + f'  <label for="{current_id}" class="accordion-menu-item-label menu-label">\n'
                handlebars += ' ' * indent + f'    {key}\n'
                handlebars += ' ' * indent + f'  </label>\n'
                handlebars += ' ' * indent + f'  <ul class="menu-list accordion-menu-item-content">\n'
                for item in value:
                    link = spin_links.pop(0) if spin_links else "#"
                    handlebars += ' ' * (indent + 4) + f'    <li><a href="{link}" class="accordion-link">{item}</a></li>\n'
                handlebars += ' ' * indent + f'  </ul>\n'
                handlebars += ' ' * indent + f'</div>\n'
        else:
            handlebars += ' ' * indent + f'<div class="accordion-menu-item">\n'
            handlebars += ' ' * indent + f'  <input type="checkbox" id="{current_id}" name="rd">\n'
            handlebars += ' ' * indent + f'  <label for="{current_id}" class="accordion-menu-item-label menu-label">\n'
            handlebars += ' ' * indent + f'    {key}\n'
            handlebars += ' ' * indent + f'  </label>\n'
            handlebars += ' ' * indent + f'  <ul class="menu-list accordion-menu-item-content">\n'
            handlebars += ' ' * indent + f'  </ul>\n'
            handlebars += ' ' * indent + f'</div>\n'
        idx += 1
    return handlebars

# Generating the combined sidebar Handlebars template
handlebars_template = f"""
<div class="accordion-tabs">
    {generate_handlebars_template(sidebar_structure)}
</div>
"""

# Save the Handlebars template to a file
with open("latest_sidebar.hbs", "w") as file:
    file.write(handlebars_template)

print("Combined sidebar Handlebars template generated successfully.")