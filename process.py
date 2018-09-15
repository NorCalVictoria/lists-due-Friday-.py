log_file = open("um-server-01.txt") #a variable for contents of the log file


def sales_reports(log_file):      # name the function passing in log_file parameter 
    for line in log_file:         # begin iterating over each item in log_file
        line = line.rstrip()      # remove whitspace chars at end of line (.rstrip) and store the result in line variable
        day = line[0:3]        # access the key : value of current line inspected (in interation)
        if day == "Mon":  # sales info from Tues to Mon    Is 3 value the sales info we are looking to display ?
            print(line)    # display info retrieved from line that in Monday and output it to console .


sales_reports(log_file) 
                            # review latest log file 

                                  #reminder to run this in Vagrant !






There is a file called process.py that seems to
display sales information for Tuesday. It would help if you could step
through this file and make any necessary adjustments for it to display
what Mel wants instead of the information it currently displays.

Also take a look at the latest log file, which has the week's sales                                                                                     
information in it.