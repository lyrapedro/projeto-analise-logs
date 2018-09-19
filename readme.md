Projeto-Analise-Logs
Gerar uma resposta, com os dados analisados no banco de dados newsdata.sql, para as seguintes consultas. 

Quais os artigos mais populares?
Quais os autores mais populares?
Em quais dias mais de 1% das requisições resultaram em erro? #Arquivos necessários
Virtualbox
Vigrant
fullstack-nanodegree-vm
newsdata.zip

Copie e cole os views criado abaixo

#1: Quais os artigos mais populares?
create view topposts as select articles.title, count(*) as views from articles join log on log.path = CONCAT('/article/', articles.slug) group by title order by views desc;

#2: Quais os autores mais populares?
create view topauthors as select authors.name, count(*) as views from authors join articles on authors.id = articles.author join log on log.path = CONCAT('/article/', articles.slug) group by name order by views desc;

#3: Em quais dias mais de 1% das requisições resultaram em erro?

3.1:
create view error_requests as select time::date, count(*) as failed_requests from log where status != '200 OK' group by time::date order by failed_requests desc;

3.2:
create view total_requests as select time::date, count(*) as tot_requests from log group by time::date order by tot_requests desc;

3.3:
create view percent_error as select total_requests.time::date, Round((error_requests.failed_requests*100)/total_requests.tot_requests, 2) as percentage from total_requests, error_requests where total_requests.time::date = error_requests.time::date order by total_requests.time::date;

3.4:
create view error_per_day as select percent_error.time::date, percent_error.percentage as errors from percent_error where percent_error.percentage > 1.0;
