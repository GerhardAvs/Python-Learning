
pylint = linter (Herramienta que checa errores en el codigo)

Pylint es un verificador de código, errores y calidad para
Python, siguiendo el estilo recomendado por PEP 8, la guía de
estilo de Python. Es de gran utilidad en el trabajo en equipo.

pip install pylint

Al ejecutarse, Pylint devuelve un reporte con las
características que fueron evaluadas, errores y
puntuaciones parciales

A mayor puntaje, mayor será la calidad de tu código.
Un umbral aceptable será >= 7.00/10

cd C:\...
pylint File.py -ry

C0304 - Los que iniciancon c son errores de estilo

E0602 - Errores graves

Pylint.py:28:0: C0304: Final newline missing (missing-final-newline)
Pylint.py:28:0: C0304: Final newline missing (missing-final-newline)
Pylint.py:22:5: W1401: Anomalous backslash in string: '\.'. String constant might be missing an r prefix. (anomalous-backslash-in-string)
Pylint.py:1:0: C0103: Module name "Pylint" doesn't conform to snake_case naming style (invalid-name)
Pylint.py:21:0: W0105: String statement has no effect (pointless-string-statement)


Report
======
3 statements analysed.

Statistics by type
------------------

+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |1      |1          |=          |100.00      |100.00   |
+---------+-------+-----------+-----------+------------+---------+
|class    |0      |NC         |NC         |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|method   |0      |NC         |NC         |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|function |0      |NC         |NC         |0           |0        |
+---------+-------+-----------+-----------+------------+---------+



30 lines have been analyzed

Raw metrics
-----------

+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |3      |10.00 |3        |=          |
+----------+-------+------+---------+-----------+
|docstring |24     |80.00 |20       |+4.00      |
+----------+-------+------+---------+-----------+
|comment   |0      |0.00  |NC       |NC         |
+----------+-------+------+---------+-----------+
|empty     |3      |10.00 |3        |=          |
+----------+-------+------+---------+-----------+



Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |0        |0          |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |0.000    |=          |
+-------------------------+------+---------+-----------+



Messages by category
--------------------

+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |3      |4        |4          |
+-----------+-------+---------+-----------+
|refactor   |0      |0        |0          |
+-----------+-------+---------+-----------+
|warning    |2      |2        |2          |
+-----------+-------+---------+-----------+
|error      |0      |0        |0          |
+-----------+-------+---------+-----------+



% errors / warnings by module
-----------------------------

+-------+------+--------+---------+-----------+
|module |error |warning |refactor |convention |
+=======+======+========+=========+===========+
|Pylint |0.00  |100.00  |0.00     |100.00     |
+-------+------+--------+---------+-----------+



Messages
--------

+------------------------------+------------+
|message id                    |occurrences |
+==============================+============+
|missing-final-newline         |2           |
+------------------------------+------------+
|pointless-string-statement    |1           |
+------------------------------+------------+
|invalid-name                  |1           |
+------------------------------+------------+
|anomalous-backslash-in-string |1           |
+------------------------------+------------+




------------------------------------------------------------------
Your code has been rated at 0.00/10 (previous run: 0.00/10, +0.00)

