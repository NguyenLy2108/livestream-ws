from datetime import datetime
from enum import Enum
import pytz
import config
from connection.database import PostgresqlStorage


cfg = config.Settings()

class Status(Enum):
    CREATED = 'CREATED'
    RUNNING = 'RUNNING'
    STOPPED = 'STOPPED'

class LivestreamStatusService():  
    def __init__(self) -> None:
        self.postgresql = PostgresqlStorage()

    def query(self, query_sql):
        return self.postgresql.query(query_sql)
    
    def livestreams_of_currentday(self):  
        current_time = datetime.now(tz=pytz.timezone('Asia/Ho_Chi_Minh'))
        start_time = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
        end_time = current_time.replace(hour=23, minute=59, second=59, microsecond=999999)
        print(current_time, start_time, end_time, start_time.astimezone(pytz.utc), end_time.astimezone(pytz.utc))  
         
        query_sql = '''
            SELECT ls.id, ls.title, ls.thumbnail, ls.platform_type, ls.livestream_url,
            ls.channel_id, ls.banner_url, ls.detail_image_url, ls.started_at, ls.ended_at,
            s.name,s.avatar, s.platforms
            FROM reviewtydev.livestream_schedule ls 
                inner join reviewtydev.streamer s on ls.channel_id = s.id
            WHERE started_at >= '{0}' and ended_at <= '{1}'
        '''.format(start_time.astimezone(pytz.utc), end_time.astimezone(pytz.utc))
        
        data = self.query(query_sql)

        if len(data) > 0:
            for r in data:
                if r['started_at'] > current_time.astimezone(pytz.utc):
                    r['status'] = Status.CREATED.value
                elif r['ended_at'] < current_time.astimezone(pytz.utc):
                    r['status'] = Status.STOPPED.value
                else:
                    r['status'] = Status.RUNNING.value   

        print(data)

        return data   