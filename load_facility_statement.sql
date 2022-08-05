load data local infile '/mnt/mydata/facilities.csv'
into table openemr.facility
fields terminated by ',' enclosed by '\"'
lines terminated by '\r\n'
ignore 1 lines
(name,street,city,state,country_code,postal_code,phone,fax,tax_id_type,federal_ein,facility_npi,website,email,billing_location,accepts_assignment,service_location,color,primary_business_entity,pos_code,attn,domain_identifier,weno_id);


name,
street,
city,
state,
country_code,
postal_code,
phone,
fax,
tax_id_type,
federal_ein,
facility_npi,
website,
email,
billing_location,
accepts_assignment,
service_location,
color,
primary_business_entity,
pos_code,
attn,
domain_identifier,
id