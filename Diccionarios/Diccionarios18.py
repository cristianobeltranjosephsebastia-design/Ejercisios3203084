jobs = {'Doctor': 'Hospital', 'Teacher': 'School', 'Pilot': 'Airplane'}
job = input("Enter a job: ")
print("Works at:", jobs.get(job.title(), "Not available"))

