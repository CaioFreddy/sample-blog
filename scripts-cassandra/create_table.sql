USE blog;

CREATE TABLE blog(
   uid uuid PRIMARY KEY,
   title text,
   content text,
   created_at timestamp,
   );
