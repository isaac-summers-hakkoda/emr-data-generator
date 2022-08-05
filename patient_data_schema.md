+----------------------+--------------+------+-----+----------+----------------+
| Field                | Type         | Null | Key | Default  | Extra          |
+----------------------+--------------+------+-----+----------+----------------+
| id                   | bigint(20)   | NO   | MUL | NULL     | auto_increment |
| uuid                 | binary(16)   | YES  | UNI | NULL     |                |
| title                | varchar(255) | NO   |     |          |                |
| language             | varchar(255) | NO   |     |          |                |
| financial            | varchar(255) | NO   |     |          |                |
| fname                | varchar(255) | NO   |     |          |                |
| lname                | varchar(255) | NO   |     |          |                |
| mname                | varchar(255) | NO   |     |          |                |
| DOB                  | date         | YES  |     | NULL     |                |
| street               | varchar(255) | NO   |     |          |                |
| postal_code          | varchar(255) | NO   |     |          |                |
| city                 | varchar(255) | NO   |     |          |                |
| state                | varchar(255) | NO   |     |          |                |
| country_code         | varchar(255) | NO   |     |          |                |
| drivers_license      | varchar(255) | NO   |     |          |                |
| ss                   | varchar(255) | NO   |     |          |                |
| occupation           | longtext     | YES  |     | NULL     |                |
| phone_home           | varchar(255) | NO   |     |          |                |
| phone_biz            | varchar(255) | NO   |     |          |                |
| phone_contact        | varchar(255) | NO   |     |          |                |
| phone_cell           | varchar(255) | NO   |     |          |                |
| pharmacy_id          | int(11)      | NO   |     | 0        |                |
| status               | varchar(255) | NO   |     |          |                |
| contact_relationship | varchar(255) | NO   |     |          |                |
| date                 | datetime     | YES  |     | NULL     |                |
| sex                  | varchar(255) | NO   |     |          |                |
| referrer             | varchar(255) | NO   |     |          |                |
| referrerID           | varchar(255) | NO   |     |          |                |
| providerID           | int(11)      | YES  |     | NULL     |                |
| ref_providerID       | int(11)      | YES  |     | NULL     |                |
| email                | varchar(255) | NO   |     |          |                |
| email_direct         | varchar(255) | NO   |     |          |                |
| ethnoracial          | varchar(255) | NO   |     |          |                |
| race                 | varchar(255) | NO   |     |          |                |
| ethnicity            | varchar(255) | NO   |     |          |                |
| religion             | varchar(40)  | NO   |     |          |                |
| interpretter         | varchar(255) | NO   |     |          |                |
| migrantseasonal      | varchar(255) | NO   |     |          |                |
| family_size          | varchar(255) | NO   |     |          |                |
| monthly_income       | varchar(255) | NO   |     |          |                |
| billing_note         | text         | YES  |     | NULL     |                |
| homeless             | varchar(255) | NO   |     |          |                |
| financial_review     | datetime     | YES  |     | NULL     |                |
| pubpid               | varchar(255) | NO   |     |          |                |
| pid                  | bigint(20)   | NO   | PRI | 0        |                |
| genericname1         | varchar(255) | NO   |     |          |                |
| genericval1          | varchar(255) | NO   |     |          |                |
| genericname2         | varchar(255) | NO   |     |          |                |
| genericval2          | varchar(255) | NO   |     |          |                |
| hipaa_mail           | varchar(3)   | NO   |     |          |                |
| hipaa_voice          | varchar(3)   | NO   |     |          |                |
| hipaa_notice         | varchar(3)   | NO   |     |          |                |
| hipaa_message        | varchar(20)  | NO   |     |          |                |
| hipaa_allowsms       | varchar(3)   | NO   |     | NO       |                |
| hipaa_allowemail     | varchar(3)   | NO   |     | NO       |                |
| squad                | varchar(32)  | NO   |     |          |                |
| fitness              | int(11)      | NO   |     | 0        |                |
| referral_source      | varchar(30)  | NO   |     |          |                |
| usertext1            | varchar(255) | NO   |     |          |                |
| usertext2            | varchar(255) | NO   |     |          |                |
| usertext3            | varchar(255) | NO   |     |          |                |
| usertext4            | varchar(255) | NO   |     |          |                |
| usertext5            | varchar(255) | NO   |     |          |                |
| usertext6            | varchar(255) | NO   |     |          |                |
| usertext7            | varchar(255) | NO   |     |          |                |
| usertext8            | varchar(255) | NO   |     |          |                |
| userlist1            | varchar(255) | NO   |     |          |                |
| userlist2            | varchar(255) | NO   |     |          |                |
| userlist3            | varchar(255) | NO   |     |          |                |
| userlist4            | varchar(255) | NO   |     |          |                |
| userlist5            | varchar(255) | NO   |     |          |                |
| userlist6            | varchar(255) | NO   |     |          |                |
| userlist7            | varchar(255) | NO   |     |          |                |
| pricelevel           | varchar(255) | NO   |     | standard |                |
| regdate              | datetime     | YES  |     | NULL     |                |
| contrastart          | date         | YES  |     | NULL     |                |
| completed_ad         | varchar(3)   | NO   |     | NO       |                |
| ad_reviewed          | date         | YES  |     | NULL     |                |
| vfc                  | varchar(255) | NO   |     |          |                |
| mothersname          | varchar(255) | NO   |     |          |                |
| guardiansname        | text         | YES  |     | NULL     |                |
| allow_imm_reg_use    | varchar(255) | NO   |     |          |                |
| allow_imm_info_share | varchar(255) | NO   |     |          |                |
| allow_health_info_ex | varchar(255) | NO   |     |          |                |
| allow_patient_portal | varchar(31)  | NO   |     |          |                |
| deceased_date        | datetime     | YES  |     | NULL     |                |
| deceased_reason      | varchar(255) | NO   |     |          |                |
| soap_import_status   | tinyint(4)   | YES  |     | NULL     |                |
| cmsportal_login      | varchar(60)  | NO   |     |          |                |
| care_team_provider   | text         | YES  |     | NULL     |                |
| care_team_facility   | text         | YES  |     | NULL     |                |
| care_team_status     | text         | YES  |     | NULL     |                |
| county               | varchar(40)  | NO   |     |          |                |
| industry             | text         | YES  |     | NULL     |                |
| imm_reg_status       | text         | YES  |     | NULL     |                |
| imm_reg_stat_effdate | text         | YES  |     | NULL     |                |
| publicity_code       | text         | YES  |     | NULL     |                |
| publ_code_eff_date   | text         | YES  |     | NULL     |                |
| protect_indicator    | text         | YES  |     | NULL     |                |
| prot_indi_effdate    | text         | YES  |     | NULL     |                |
| guardianrelationship | text         | YES  |     | NULL     |                |
| guardiansex          | text         | YES  |     | NULL     |                |
| guardianaddress      | text         | YES  |     | NULL     |                |
| guardiancity         | text         | YES  |     | NULL     |                |
| guardianstate        | text         | YES  |     | NULL     |                |
| guardianpostalcode   | text         | YES  |     | NULL     |                |
| guardiancountry      | text         | YES  |     | NULL     |                |
| guardianphone        | text         | YES  |     | NULL     |                |
| guardianworkphone    | text         | YES  |     | NULL     |                |
| guardianemail        | text         | YES  |     | NULL     |                |
| sexual_orientation   | text         | YES  |     | NULL     |                |
| gender_identity      | text         | YES  |     | NULL     |                |
| birth_fname          | text         | YES  |     | NULL     |                |
| birth_lname          | text         | YES  |     | NULL     |                |
| birth_mname          | text         | YES  |     | NULL     |                |
| dupscore             | int(11)      | NO   |     | -9       |                |
| name_history         | tinytext     | YES  |     | NULL     |                |
| suffix               | tinytext     | YES  |     | NULL     |                |
| street_line_2        | tinytext     | YES  |     | NULL     |                |
| patient_groups       | text         | YES  |     | NULL     |                |
| prevent_portal_apps  | text         | YES  |     | NULL     |                |
| provider_since_date  | tinytext     | YES  |     | NULL     |                |
| created_by           | bigint(20)   | YES  |     | NULL     |                |
| updated_by           | bigint(20)   | YES  |     | NULL     |                |
+----------------------+--------------+------+-----+----------+----------------+