from dotenv import load_dotenv
import psycopg2
import os



# 不上傳Passwordkey
load_dotenv()
# 取的行政區資料
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
    
# 取的該行政區所有站點資訊
def get_snaOfArea(area:str) -> list[tuple]:
    # 建立連線
    conn = psycopg2.connect(os.environ['POSTGRESQL_TOKEN'])
    
    with conn: #with conn會自動commit()
       with conn.cursor() as cursor: # as cursor自動close()
            sql='''
                SELECT sna AS 站點, total AS 總車輛數, rent_bikes AS 可借, return_bikes AS 可還, mday AS 時間, act AS 狀態
                FROM youbike
                where (updatetime, sna) IN(
                SELECT MAX (updatetime), sna
                FROM youbike
                where sarea = (%s)
                GROUP BY sna
                );      
            '''
            cursor.execute(sql, (area,))
            return cursor.fetchall()
    conn.close()