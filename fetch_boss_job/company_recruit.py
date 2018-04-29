class RecruitInfo:
    """
        job_title =
        salary =
        site =
        experiences =
        education =
        company_name =
        company_type =
        financing =
        num_employee =
    """
    # Should I use  *args, **kwargs
    def __init__(self, job_title, salary, site, education,
                 company_name, financing, num_employee, release_date, experiences, tag, hr_name):
        self.job_title = job_title
        self.salary = salary
        self.site = site
        self.education = education
        self.company_name = company_name
        self.financing = financing
        self.num_employee = num_employee
        self.release_date = release_date
        self.experiences = experiences
        self.tag = tag
        self.hr_name = hr_name

    def get_all_attrs(self):
        return ";".join("{}={}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return "[{}:{}]".format(self.__class__.__name__, self.get_all_attrs())
