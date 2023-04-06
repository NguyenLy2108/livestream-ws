from services.activity_logs.route import router as ActivityLogs

ROUTE_LIST = [
    {'route': ActivityLogs, 'tags': ["Activity Logs"], 'prefix': '/logs'},
]