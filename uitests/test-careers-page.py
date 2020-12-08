import pytest


class TestAboutPage:

    @pytest.fixture()
    def setup(self, request, fix_base):
        self.base = fix_base
        self.base.inst_pages()

        def teardown():
            self.base.teardown_ui()
        request.addfinalizer(teardown)

    def test_get_job_links(self, setup):
        self.base.driver.get('{}/about/'.format(self.base.get_config()['marketingurl'].replace('"', '')))
        self.base.basepage.click(self.base.aboutpage.ACCEPT_ALL_COOKIES_BTN)
        self.base.basepage.click(self.base.aboutpage.CAREERS_ARROW_BTN)
        self.base.basepage.click(self.base.aboutpage.SEE_OUR_JOB_OPENINGS_LINK)
        all_jobs_links = self.base.basepage.driver.find_elements_by_xpath(self.base.aboutpage.ALL_FULL_TIME_POSITIONS_LINKS_XPATH)

        all_jobs = []
        for each in all_jobs_links:
            all_jobs.append(each.text)

        expected_jobs = ['UX Content Strategist', 'Software Engineering Manager', 'Senior UX Designer', 'Senior Software Engineer (Telephony)', 'Senior Software Engineer', 'Senior Product Manager', 'Senior Communications and Advocacy Manager', 'QA Engineer', 'Lead Web Developer', 'Inbound Sales Development Representative', 'HR Coordinator', 'Fullstack Engineer', 'Financial Systems Manager', 'Engineering Support Team Lead', 'Content Marketing Writer']
        assert all_jobs == expected_jobs, 'Actual jobs - {}'.format(all_jobs)
