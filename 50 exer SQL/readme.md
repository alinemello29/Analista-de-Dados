# 📊 Exercícios de SQL - 50 Consultas

Bem-vindo ao repositório de exercícios de SQL! Aqui você encontrará 50 consultas SQL que foram elaboradas para aprimorar habilidades em manipulação e consulta de dados.

## 📚 Conteúdo

Este repositório contém consultas SQL para diversas operações, incluindo seleção, filtragem, agregação e junção de dados em tabelas. Abaixo estão os detalhes dos exercícios realizados:

### 📝 Exercícios

1. **Selecionar todos os dados da tabela cliente**: `SELECT * FROM cliente;`
2. **Listar clientes em São Paulo**: `SELECT * FROM cliente WHERE cidade = 'São Paulo';`
3. **Estados diferentes na tabela cliente**: `SELECT DISTINCT estado FROM cliente;`
4. **Clientes ordenados por nome**: `SELECT * FROM cliente ORDER BY nome ASC;`
5. **Clientes femininos e solteiros**: `SELECT * FROM cliente WHERE sexo = 'Feminino' AND estado_civil = 'Solteiro';`
6. **Clientes cujo nome começa com 'A'**: `SELECT * FROM cliente WHERE nome LIKE 'A%';`
7. **Três primeiros registros da tabela cliente**: `SELECT * FROM cliente LIMIT 3;`
8. **Carros da marca 'Ford' ou 'Fiat'**: `SELECT * FROM carro WHERE marca IN ('Ford', 'Fiat');`
9. **Carros com valor entre 100 e 150**: `SELECT * FROM carro WHERE valor BETWEEN 100 AND 150;`
10. **Total de aluguéis realizados**: `SELECT COUNT(*) FROM aluguel;`
11. **Valor total de todos os carros**: `SELECT SUM(valor) FROM carro;`
12. **Valor médio dos carros**: `SELECT AVG(valor) FROM carro;`
13. **Menor e maior valor de aluguel de carros**: `SELECT MIN(valor), MAX(valor) FROM carro;`
14. **Clientes por estado**: `SELECT estado, COUNT(*) FROM cliente GROUP BY estado;`
15. **Clientes com mais de 2 aluguéis**: `SELECT cliente_id, COUNT(*) FROM aluguel GROUP BY cliente_id HAVING COUNT(*) > 2;`
16. **Nome do cliente e modelo do carro alugado**: `SELECT c.nome, car.modelo FROM aluguel a JOIN cliente c ON a.cliente_id = c.id JOIN carro car ON a.carro_id = car.id;`
17. **Carros e informações sobre aluguéis**: `SELECT car.*, a.data_aluguel FROM carro car LEFT JOIN aluguel a ON car.id = a.carro_id;`
18. **Aluguéis e informações sobre carros, mesmo que não estejam mais no banco**: `SELECT a.*, car.modelo FROM aluguel a LEFT JOIN carro car ON a.carro_id = car.id;`
19. **Clientes e carros alugados, incluindo aqueles que não alugaram**: `SELECT c.nome, car.modelo FROM cliente c LEFT JOIN aluguel a ON c.id = a.cliente_id LEFT JOIN carro car ON a.carro_id = car.id;`
20. **Clientes solteiros e casados**: `SELECT * FROM cliente WHERE estado_civil = 'Solteiro' UNION SELECT * FROM cliente WHERE estado_civil = 'Casado';`
21. **Clientes que alugaram o carro 'Onix'**: `SELECT c.* FROM cliente c JOIN aluguel a ON c.id = a.cliente_id JOIN carro car ON a.carro_id = car.id WHERE car.modelo = 'Onix';`
22. **Modelos de carros e número de aluguéis**: `SELECT car.modelo, COUNT(a.id) AS quantidade FROM carro car LEFT JOIN aluguel a ON car.id = a.carro_id GROUP BY car.modelo;`
23. **Nomes dos clientes e número de aluguéis**: `SELECT c.nome, COUNT(a.id) AS quantidade FROM cliente c LEFT JOIN aluguel a ON c.id = a.cliente_id GROUP BY c.nome;`
24. **Nome dos clientes e status civil**: `SELECT nome, estado_civil AS status_civil FROM cliente;`
25. **Clientes e datas de aluguel**: `SELECT c.nome, a.data_aluguel FROM cliente c JOIN aluguel a ON c.id = a.cliente_id;`
26. **Modelos e marcas de carros**: `SELECT modelo, marca FROM carro;`
27. **Aluguéis e nomes dos clientes**: `SELECT a.*, c.nome FROM aluguel a JOIN cliente c ON a.cliente_id = c.id;`
28. **Nomes dos clientes e modelos de carros alugados**: `SELECT c.nome, car.modelo FROM cliente c JOIN aluguel a ON c.id = a.cliente_id JOIN carro car ON a.carro_id = car.id;`
29. **Carros e datas em que foram alugados**: `SELECT car.*, a.data_aluguel FROM carro car LEFT JOIN aluguel a ON car.id = a.carro_id;`
30. **Clientes na mesma cidade e estado**: `SELECT c1.nome FROM cliente c1 JOIN aluguel a ON c1.id = a.cliente_id JOIN cliente c2 ON c1.cidade = c2.cidade AND c1.estado = c2.estado WHERE c1.id <> c2.id;`
31. **Clientes e carros alugados, incluindo não alugados**: `SELECT c.nome, car.modelo FROM cliente c LEFT JOIN aluguel a ON c.id = a.cliente_id LEFT JOIN carro car ON a.carro_id = car.id;`
32. **Marcas e modelos de carros**: `SELECT marca, modelo FROM carro;`
33. **Aluguéis e estado civil dos clientes**: `SELECT a.*, c.estado_civil FROM aluguel a JOIN cliente c ON a.cliente_id = c.id;`
34. **Clientes e cidades que alugaram carros**: `SELECT DISTINCT c.nome, c.cidade FROM cliente c JOIN aluguel a ON c.id = a.cliente_id;`
35. **Clientes, modelos de carros e valor gasto**: `SELECT c.nome, car.modelo, car.marca, SUM(car.valor) AS total_gasto FROM cliente c JOIN aluguel a ON c.id = a.cliente_id JOIN carro car ON a.carro_id = car.id GROUP BY c.nome;`
36. **Aluguéis em uma cidade específica**: `SELECT c.nome, car.modelo FROM aluguel a JOIN cliente c ON a.cliente_id = c.id JOIN carro car ON a.carro_id = car.id WHERE c.cidade = 'Cidade Específica';`
37. **Modelos de carros e quantidade de aluguéis**: `SELECT car.modelo, COUNT(a.id) AS quantidade FROM carro car LEFT JOIN aluguel a ON car.id = a.carro_id GROUP BY car.modelo;`
38. **Clientes que alugaram mais de um carro**: `SELECT c.nome FROM cliente c JOIN aluguel a ON c.id = a.cliente_id GROUP BY c.id HAVING COUNT(DISTINCT a.carro_id) > 1;`
39. **Clientes, datas de aluguel e valores dos carros**: `SELECT c.nome, a.data_aluguel, car.valor FROM cliente c JOIN aluguel a ON c.id = a.cliente_id JOIN carro car ON a.carro_id = car.id;`
40. **Modelos de carros nunca alugados**: `SELECT modelo FROM carro WHERE id NOT IN (SELECT carro_id FROM aluguel);`
41. **Total gasto pelos clientes em aluguéis**: `SELECT c.nome, SUM(car.valor) AS total_gasto FROM cliente c JOIN aluguel a ON c.id = a.cliente_id JOIN carro car ON a.carro_id = car.id GROUP BY c.nome;`
42. **Marcas de carros e total de aluguéis**: `SELECT car.marca, COUNT(a.id) AS total_alugueis FROM carro car LEFT JOIN aluguel a ON car.id = a.carro_id GROUP BY car.marca;`
43. **Aluguéis em um mês e ano específicos**: `SELECT c.nome, car.modelo, a.data_aluguel FROM cliente c JOIN aluguel a ON c.id = a.cliente_id JOIN carro car ON a.carro_id = car.id WHERE MONTH(a.data_aluguel) = 1 AND YEAR(a.data_aluguel) = 2023;`
44. **Clientes em estados diferentes com aluguéis**: `SELECT DISTINCT c1.nome, c1.estado, car.modelo FROM cliente c1 JOIN aluguel a ON c1.id = a.cliente_id JOIN carro car ON a.carro_id = car.id WHERE c1.estado <> (SELECT estado FROM cliente WHERE id = c1.id);`
45. **Clientes, modelos e marcas de carros alugados**: `SELECT c.nome, car.modelo, car.marca, SUM(car.valor) AS total_gasto FROM cliente c JOIN aluguel a ON c.id = a.cliente_id JOIN carro car ON a.carro_id = car.id GROUP BY c.nome, car.modelo, car.marca;`
46. **Clientes que alugaram carros mais de uma vez**: `SELECT c.nome, car.modelo, COUNT(a.id) AS quantidade FROM cliente c JOIN aluguel a ON c.id = a.cliente_id JOIN carro car ON a.carro_id = car.id GROUP BY c.nome, car.modelo HAVING COUNT(a.id) > 1;`
47. **Modelos de carros alugados em cidades específicas**: `SELECT DISTINCT car.modelo, car.marca FROM carro car JOIN aluguel a ON car.id = a.carro_id JOIN cliente c ON a.cliente_id = c.id WHERE c.cidade IN ('Cidade Específica 1', 'Cidade Específica 2');`
48. **Clientes, carros alugados e total gasto**: `SELECT c.nome, car.modelo, car.marca, SUM(car.valor) AS total_gasto FROM cliente c JOIN aluguel a ON c.id = a.cliente_id JOIN carro car ON a.carro_id = car.id GROUP BY c.nome, car.modelo, car.marca;`
49. **Carros alugados nos últimos 30 dias**: `SELECT car.modelo, c.nome FROM carro car JOIN aluguel a ON car.id = a.carro_id JOIN cliente c ON a.cliente_id = c.id WHERE a.data_aluguel >= CURDATE() - INTERVAL 30 DAY;`
50. **Clientes, carros alugados e total gasto em um intervalo específico**: `SELECT c.nome, car.modelo, car.marca, SUM(car.valor) AS total_gasto FROM cliente c JOIN aluguel a ON c.id = a.cliente_id JOIN carro car ON a.carro_id = car.id WHERE a.data_aluguel BETWEEN '2023-01-01' AND '2023-12-31' GROUP BY c.nome, car.modelo, car.marca;`

## 🚀 Contribuições

Sinta-se à vontade para contribuir com melhorias ou novos exercícios. Agradeço por qualquer feedback!

## 📧 Contato

Para mais informações, você pode me contatar em: [seu-email@example.com](mailto:seu-email@example.com)

---

Espero que você aproveite os exercícios e aprenda mais sobre SQL! 💻✨