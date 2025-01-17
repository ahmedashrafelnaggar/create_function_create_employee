from odoo import models, fields, api
from odoo.exceptions import UserError


class IpmcApplicants(models.Model):
    _inherit = 'hr.applicant'
    contact_name = fields.Char('Contact Name', required=False)
    employment_id = fields.Many2one('employment.status')
    res_country_id = fields.Many2one('res.country', 'Country')
    res_country_state_id = fields.Many2one('res.country.state', 'Country State')
    res_bank_id = fields.Many2one('res.bank', 'Bank')
    hr_job_id = fields.Many2one('hr.job', 'Job')
    hr_department_id = fields.Many2one('hr.department', 'Department')

    ex_id = fields.Integer(string="External ID")
    # identifier = fields.Char(string="identifier")
    iqama_number = fields.Char(string="Residential Number")
    iqama_exp_date = fields.Date(string="Residential Expiry Date")
    iqama_src_id = fields.Many2one('res.country.state', string='Residential Source')
    nationality_id = fields.Many2one('res.country', string='Nationality')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    phone = fields.Char(string='Contact Phone')
    hr_recruitment_degree_id = fields.Many2one('hr.recruitment.degree', 'Degree')
    speciality = fields.Char(string="Speciality")
    birth_date = fields.Date(string="Date of Birth")
    address = fields.Char(string="Address")
    applicant_id = fields.Many2one('hr.applicant', string="Applicant ID")
    partner_mobile = fields.Char(readonly=0 , string=' Mobile')
    email_from = fields.Char(readonly=0, string='Email ')
    email_cc= fields.Char(string='Email cc')
    Employement_Status = fields.Many2one('employment.status', string="Employment Status")
    years_of_experience = fields.Integer(string="Years of Experience")
    employer = fields.Char(string="Employer")
    workplace = fields.Char(string="Work Place")
    years_of_experience_in_haj = fields.Integer(string="Years of Experience in HAJ")
    job_title_in_haj = fields.Many2one('hr.job',string="Job Title in HAJ")
    party_name_in_haj = fields.Char(string="Party Name")
    job_app_announcement_id = fields.Many2one('ipmc.application.announcement',string="Announcement")
    applied_job_workplace_id = fields.Many2one('res.country.state',string="chosen Work Place ")
    first_job_id_applied = fields.Many2one('hr.job',string="First Desired Job")
    first_job_sector_id = fields.Many2one('hr.department',string=" First Desired Department")
    second_job_id_applied = fields.Many2one('hr.job',string="Second Desired Job")
    second_job_sector_id = fields.Many2one('hr.department',string="Second Desired Department")
    third_job_id_applied = fields.Many2one('hr.job',string="Third Desired Job")
    third_job_sector_id = fields.Many2one('hr.department',string="Third Desired Department")
    bank_id = fields.Many2one('res.bank',string="Bank Name")
    iban = fields.Char(string="IBAN Number")
    authorized_iban = fields.Binary(string="IBAN Image URL")
    profile_image = fields.Binary(string="Person Picture URL")
    cv = fields.Binary(string="CV URL")
    instructionandcondition = fields.Text('Instructions and conditions')

    def create_employee_from_applicant(self):
        print('hashhhhhhhhh')
        employee_status_obj = self.env['employment.status']
        for applicant in self:
            # if not applicant.contact_name:
            #     raise UserError("You must define a Contact Name for this applicant.")

            # Create a record in the "employee.status" model
            employee_status = employee_status_obj.create({
                'name': applicant.partner_name,
                'email_from': applicant.email_from,
                'contact_name': applicant.contact_name,
                'phone': applicant.partner_phone,
                'partner_mobile': applicant.partner_mobile,
                # this mean this field hr_recruitment_degree_id in model employement.status = value this field type_id.id in model hr applicant
                # should the same type even if the name was different
                # and all field which contain on field many2one you should put .id
                'hr_recruitment_degree_id': applicant.hr_recruitment_degree_id.id,
                'iqama_number': applicant.iqama_number,
                'iqama_exp_date': applicant.iqama_exp_date,
                'iqama_src_id': applicant.iqama_src_id.id,
                'nationality_id': applicant.nationality_id.id,
                'gender': applicant.gender,
                'speciality': applicant.speciality,
                'birth_date': applicant.birth_date,
                'email_cc': applicant.email_cc,
                'address': applicant.address,
                # any field relationfield you should put .id
                'Employement_Status': applicant.Employement_Status.id,
                'years_of_experience': applicant.years_of_experience,
                'employer': applicant.employer,
                'workplace': applicant.workplace,
                'years_of_experience_in_haj': applicant.years_of_experience_in_haj,
                'job_title_in_haj': applicant.job_title_in_haj.id,
                'party_name_in_haj': applicant.party_name_in_haj,
                'job_app_announcement_id': applicant.job_app_announcement_id.id,
                'applied_job_workplace_id': applicant.applied_job_workplace_id.id,
                'first_job_id_applied': applicant.first_job_id_applied.id,
                'first_job_sector_id': applicant.first_job_sector_id.id,
                'second_job_id_applied': applicant.second_job_id_applied.id,
                'second_job_sector_id': applicant.second_job_sector_id.id,
                'third_job_id_applied': applicant.third_job_id_applied.id,
                'third_job_sector_id': applicant.third_job_sector_id.id,
                'bank_id': applicant.bank_id.id,
                'iban': applicant.iban,
                'cv': applicant.cv,
                'profile_image': applicant.profile_image,
                'authorized_iban': applicant.authorized_iban,
                'instructionandcondition': applicant.instructionandcondition,
            })

            # applicant.employment_id = employee_status.id









