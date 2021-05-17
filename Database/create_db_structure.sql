CREATE TABLE admin ( ad_id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, ad_usname varchar(30) NOT NULL, ad_pass varchar(20) NOT NULL, ad_name varchar(50) NOT NULL, ad_phn decimal(10,0) NOT NULL, ad_email varchar(50));


CREATE TABLE supplier (sup_id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, sup_agency varchar(30) NOT NULL, sup_name varchar(20) NOT NULL, sup_phn decimal(10,0) NOT NULL, sup_email varchar(20), sup_addr varchar(50));


CREATE TABLE customer ( cust_id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, cust_name varchar(10) NOT NULL, cust_city varchar(20), cust_phn decimal(10,0), cust_email varchar(50));


CREATE TABLE med_details ( med_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, med_name varchar(60) NOT NULL, med_comp varchar(60) NOT NULL, med_price int(11) NOT NULL);


CREATE TABLE med_batch_details ( med_id int NOT NULL , batch_id INT NOT NULL , med_mfg date NOT NULL, med_exp date NOT NULL, med_status varchar(15), curr_qty INT NOT NULL, PRIMARY KEY(med_id,batch_id));
ALTER TABLE med_batch_details ADD FOREIGN KEY (med_id) REFERENCES med_details(med_id);



CREATE TABLE purchase_details ( p_id int NOT NULL AUTO_INCREMENT , p_med_id INT NOT NULL, p_sup_id INT NOT NULL, p_date date NOT NULL, p_price int(11), p_qty INT NOT NULL, p_totalamt int(15) NOT NULL, PRIMARY KEY(p_id,p_med_id));
ALTER TABLE purchase_details ADD FOREIGN KEY (p_sup_id) REFERENCES supplier(sup_id);
ALTER TABLE purchase_details ADD FOREIGN KEY (p_med_id) REFERENCES med_details(med_id);


CREATE TABLE sale_details ( s_id int NOT NULL , s_med_id INT NOT NULL, s_cust_id INT NOT NULL, s_date date NOT NULL, s_qty INT NOT NULL, s_totalamt int(11) NOT NULL, PRIMARY KEY(s_id,s_med_id));
ALTER TABLE sale_details ADD FOREIGN KEY (s_cust_id) REFERENCES customer(cust_id);
ALTER TABLE sale_details ADD FOREIGN KEY (s_med_id) REFERENCES med_details(med_id);



