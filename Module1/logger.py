from time import strftime

log_file = open("program.log", "w")

log_file.write(strftime("%m/%d/%Y %H:%M:%S") + "\n")
log_file.write("\tProgram started\n\n")

log_file.close()

