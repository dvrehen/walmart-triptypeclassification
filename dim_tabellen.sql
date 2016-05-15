select distinct Weekday from test_train
select count(distinct [Weekday]) from test_train

select distinct [DepartmentDescription] from test_train
select count(distinct [DepartmentDescription]) from test_train

--select distinct [UPC] from test_train
select count(distinct [UPC]) from test_train

--select distinct [FinelineNumber] from test_train
select count(distinct [FinelineNumber]) from test_train

select count(distinct [DepartmentDescription]) from test_train


truncate table dim_department
insert into dim_department select 'NULL'
insert into dim_department select distinct [DepartmentDescription] from test_train where [DepartmentDescription] <> 'NULL' order by [DepartmentDescription]

select count(*) from dim_department -- 69


-- Process finelinenumber
truncate table dim_finelinenumber_tmp
insert into dim_finelinenumber_tmp select 'NULL', null
insert into dim_finelinenumber_tmp select distinct [DepartmentDescription], FinelineNumber from test_train where [DepartmentDescription] <> 'NULL' order by [DepartmentDescription], FinelineNumber

truncate table dim_finelinenumber
insert into dim_finelinenumber select 'NULL', null
insert into dim_finelinenumber
select f.DepartmentDescription, f.FinelineNumber from test_train t
inner join dim_finelinenumber_tmp f ON f.FinelineNumber = t.FinelineNumber AND t.DepartmentDescription = f.DepartmentDescription
group by f.DepartmentDescription, f.FinelineNumber, f.ID order by abs(sum(t.ScanCount)) desc

select count(*) from dim_finelinenumber -- 11149


truncate table dim_triptype
insert into dim_triptype select distinct TripType from test_train where TripType is not null order by TripType

select count(*) from fact_data --1300700
select count(*) from lineitem_sales --1268804 klopt
select count(*) from lineitem_sales --1268804 klopt


--select distinct RIGHT('000000000000'+ISNULL(CAST(UPC AS VARCHAR(12)),''),12) from test_train where upc = 2000019963
insert into dim_upc_company select distinct SUBSTRING(RIGHT('000000000000'+ISNULL(CAST(UPC AS VARCHAR(12)),''),12), 1, 6) from test_train

truncate table dim_upc_prefix_tmp
insert into dim_upc_prefix_tmp select 1
insert into dim_upc_prefix_tmp
select c.upc_companycode from test_train t
inner join dim_upc_company c ON SUBSTRING(RIGHT('000000000000'+ISNULL(CAST(t.UPC AS VARCHAR(12)),''),12), 1, 6) = c.upc_companycode
group by c.upc_companycode order by sum(t.ScanCount) desc


select sum(t.ScanCount) from test_train t -- 1.442.218

select c.upc_companycode, sum(t.ScanCount) from test_train t
inner join dim_upc_company c ON SUBSTRING(RIGHT('000000000000'+ISNULL(CAST(t.UPC AS VARCHAR(12)),''),12), 1, 6) = c.upc_companycode
group by c.upc_companycode order by sum(t.ScanCount)) desc