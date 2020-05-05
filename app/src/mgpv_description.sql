SELECT distinct cms_program_guid, cms_franchise_guid, program_description 
FROM "sb_mg_pv"."mgpv_extracts_all"
where lower(program_description) like '%alex smith%'