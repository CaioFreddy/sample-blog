USE blog;

CREATE TABLE blog(
   uid text,
   title text,
   content text,
   created_at timestamp,
   PRIMARY KEY (uid, created_at)
   ) WITH CLUSTERING ORDER BY (created_at DESC);
