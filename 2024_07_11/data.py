from dotenv import load_dotenv
import psycopg2
import os



# 不上傳Passwordkey
load_dotenv()

def get_areas() -> list[tuple]:
    # 建立連線
    conn = psycopg2.connect(os.environ['POSTGRESQL_TOKEN'])
    
    with conn: #with conn會自動commit()
       with conn.cursor() as cursor: # as cursor自動close()
            sql='''
                SELECT DISTINCT sarea FROM youbike;
                
            '''
            cursor.execute(sql)
            return cursor.fetchall()


    conn.close()