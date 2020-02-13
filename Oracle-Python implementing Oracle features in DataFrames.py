import pandas as pa
dfa= pa.read_csv('C:\\PYTHONDATASCIENCE\\CompareFileA.csv')
dfa
dfb= pa.read_csv('C:\\PYTHONDATASCIENCE\\CompareFileB.csv')
dfb

#implementing a MINUS
df_concat_ab = pa.concat([dfa,dfb])
#df_diff = pd.concat([dfa,dfb]).drop_duplicates(keep=False)
df_concat_ab


# Date	Fruit	Num	Color
# 0	2013-11-24	Banana	22.1	Yellow
# 1	2013-11-24	Orange	8.6	Orange
# 2	2013-11-24	Apple	7.6	Green
# 3	2013-11-24	Celery	10.2	Green
# 0	2013-11-24	Banana	22.1	Yellow
# 1	2013-11-24	Orange	8.6	Orange
# 2	2013-11-24	Apple	7.6	Green
# 3	2013-11-24	Celery	10.2	Green
# 4	2013-11-25	Apple	22.1	Red
# 5	2013-11-25	Orange	8.6	Orange

df_minus=df_concat_ab.drop_duplicates(keep=False)
df_minus
	# Date	Fruit	Num	Color
# 4	2013-11-25	Apple	22.1	Red
# 5	2013-11-25	Orange	8.6	Orange