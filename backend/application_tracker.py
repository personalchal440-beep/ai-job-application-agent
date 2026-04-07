import datetime

class ApplicationTracker:
    def __init__(self):
        self.applications = []  # List to store application data

    def add_application(self, title, company, status):
        application = {
            'title': title,
            'company': company,
            'status': status,
            'date_added': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.applications.append(application)
        return application

    def update_application_status(self, title, new_status):
        for application in self.applications:
            if application['title'] == title:
                application['status'] = new_status
                return application
        return None  # Return None if application not found

    def get_applications(self):
        return self.applications  # Return the list of applications

    def __repr__(self):
        return f"ApplicationTracker({self.applications})"