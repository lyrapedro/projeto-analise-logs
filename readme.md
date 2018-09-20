Projeto-Analise-Logs
Gerar uma resposta, com os dados analisados no banco de dados newsdata.sql, para as seguintes consultas. 

Quais os artigos mais populares?
Quais os autores mais populares?
Em quais dias mais de 1% das requisi��es resultaram em erro? #Arquivos necess�rios
Virtualbox
Vigrant
fullstack-nanodegree-vm
newsdata.zip

A m�quina virtual (virtual machine)
Este projeto faz uso da mesma m�quina virtual (VM) co base no Linux, como as aulas anteriores.

Se voc� pulou essas aulas e veio direto para este projeto, n�o tem problema! No entanto, voc� precisar� voltar para essas instru��es para instalar a m�quina virtual. Isto lhe dar� o banco de dados PostgreSQL e software de suporte necess�rio para este projeto. Se voc� usou uma vers�o antiga dessa VM, ela precisar� ser instalada em um novo diret�rio.

Se voc� precisa trazer a m�quina virtual de volta online (com vagrant up), fa�a isso agora. Ent�o fa�a login com vagrant ssh.

Copie e cole os views criado abaixo

#1: Quais os artigos mais populares?
create view topposts as select articles.title, count(*) as views from articles join log on log.path = CONCAT('/article/', articles.slug) group by title order by views desc;

#2: Quais os autores mais populares?
create view topauthors as select authors.name, count(*) as views from authors join articles on authors.id = articles.author join log on log.path = CONCAT('/article/', articles.slug) group by name order by views desc;

#3: Em quais dias mais de 1% das requisi��es resultaram em erro?

3.1:
create view error_requests as select time::date, count(*) as failed_requests from log where status != '200 OK' group by time::date order by failed_requests desc;

3.2:
create view total_requests as select time::date, count(*) as tot_requests from log group by time::date order by tot_requests desc;

3.3:
create view percent_error as select total_requests.time::date, Round((error_requests.failed_requests*100)/total_requests.tot_requests, 2) as percentage from total_requests, error_requests where total_requests.time::date = error_requests.time::date order by total_requests.time::date;

3.4:
create view error_per_day as select percent_error.time::date, percent_error.percentage as errors from percent_error where percent_error.percentage > 1.0;
