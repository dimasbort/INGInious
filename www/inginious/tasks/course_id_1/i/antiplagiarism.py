import mosspy

userid = 74553754 # add your userid here

m = mosspy.Moss(userid, "python")

# Submission Files
m.addFile("submissions/s01-sample.py")

m.addFilesByWildcard("submissions/s01-*.py")

# progress function optional, run on every file uploaded
# result is submission URL
url = m.send(lambda file_path, display_name: print('*', end='', flush=True))
print()

print ("Report URL: " + url)

# Save report file
m.saveWebPage(url, "submissions/report.html")

mosspy.download_report(url, "submissions/report/", connections=8, log_level=10, on_read=lambda url: print('*', end='', flush=True)) 
# log_level=logging.DEBUG (20 to disable)
# on_read function run for every downloaded file
