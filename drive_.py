import win32api
import psutil
import pandas as pd
pd.options.display.float_format = '{:,.0f}'.format

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[::-1]

data = pd.DataFrame(columns=['drive', 'Total', 'Free', 'Used', 'Percent'])

for i, drive in enumerate(drives):
    if drive == '':
        continue
    data.loc[i] = [drive, psutil.disk_usage(drive).total, psutil.disk_usage(
        drive).used, psutil.disk_usage(drive).free, psutil.disk_usage(drive).percent]


data.Total = data.Total.astype(float).map(lambda x: x / 1073741824)
data.Used = data.Used.astype(float).map(lambda x: x / 1073741824)
data.Free = data.Free.astype(float).map(lambda x: x / 1073741824)


print(data)
