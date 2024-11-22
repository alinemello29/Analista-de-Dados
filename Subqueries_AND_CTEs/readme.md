# 📚 Aula de Subqueries e CTEs 📊

Bem-vindo à aula sobre **Subqueries** e **Common Table Expressions (CTEs)**! Nesta aula, vamos explorar como utilizar essas técnicas poderosas em SQL para otimizar e estruturar suas consultas de banco de dados. 🚀

## O que são Subqueries? 🤔

Uma **subquery** (ou consulta aninhada) é uma consulta SQL dentro de outra consulta. Elas são úteis para realizar operações complexas e podem ser usadas em cláusulas `SELECT`, `FROM`, `WHERE`, entre outras.

### Exemplo de Subquery

```sql
SELECT nome
FROM cliente
WHERE estado IN (SELECT estado FROM estado WHERE populacao > 1000000);
O que são CTEs? 📈
Uma Common Table Expression (CTE) é uma forma de definir uma consulta temporária que pode ser referenciada dentro de uma instrução SELECT, INSERT, UPDATE ou DELETE. CTEs ajudam a tornar o código mais legível e organizado.

Exemplo de CTE
sql

Copiar
WITH total_gasto AS (
    SELECT cliente_id, SUM(valor) AS total
    FROM aluguel
    GROUP BY cliente_id
)
SELECT c.nome, tg.total
FROM cliente c
JOIN total_gasto tg ON c.id = tg.cliente_id;
Por que usar Subqueries e CTEs? 💡
Organização: Torna o código mais legível e modular.
Reutilização: Permite reutilizar consultas complexas sem reescrevê-las.
Performance: Em alguns casos, pode melhorar a performance das consultas.
Conclusão 🎉
Nesta aula, você aprendeu sobre subqueries e CTEs, suas definições, exemplos práticos e benefícios. Agora, você pode aplicar esses conceitos em suas consultas SQL para torná-las mais eficientes e compreensíveis.