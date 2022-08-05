load data local infile '/mnt/mydata/patient_data.csv'
into table openemr.patient_data
fields terminated by ',' enclosed by '\"'
lines terminated by '\r\n'
ignore 1 lines
(title,language,financial,fname,lname,mname,DOB,street,postal_code,city,state,country_code,drivers_license,ss,occupation,phone_home,phone_biz,phone_contact,phone_cell,pharmacy_id,status,contact_relationship,date,sex,referrer,referrerID,providerID,ref_providerID,email,email_direct,ethnoracial,race,ethnicity,religion,interpretter,migrantseasonal,family_size,monthly_income,billing_note,homeless,financial_review,pubpid,pid,hipaa_mail,hipaa_voice,hipaa_notice,hipaa_message,hipaa_allowsms,hipaa_allowemail);