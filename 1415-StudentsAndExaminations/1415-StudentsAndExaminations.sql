-- Last updated: 6/25/2026, 9:11:11 AM
select Students.student_id, student_name, Subjects.subject_name,  coalesce(c.attended_exams,0) as attended_exams  from Students 
cross join Subjects
left join (select *,count(*) as attended_exams from Examinations group by student_id,subject_name) c on 
Students.student_id=c.student_id
and 
Subjects.subject_name=c.subject_name
order by student_id,subject_name