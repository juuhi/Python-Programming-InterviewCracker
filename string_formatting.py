#"""string formatting"""
#"""dynamically assign values to string (ideally used for logging or reporting"""
#"""can also be used for debugging"""
#"""best resource to learn this: https://pyformat.info/ """

#""" {} {} used in new styled formaating whereas %s %d used in old style formatting"""

"""defining some variable that we will use in string formatting"""
some_id = 9999
some_msg = "Infinite world"
some_other_message = "What else you need?"
e="Error! What the Hack! you can get this from Exception e"

# formatting with {}
str1 = "Job ID with sub message: {}{}: Error processing config file".format(some_id, some_msg)
print str1
str2 = "Job ID {}{}: Error trying to retrieve S3 file {} - {}".format(some_id, some_msg, some_other_message, e)
print str2

# use of index positions within {}
str2_1 = "Job ID {2}{1}: Error trying to retrieve S3 file {3} - {0}".format(e, some_msg, some_id, some_other_message)
print str2_1

#formatting string with %s and %d
some_file = "/test_dir/File_name.demo"
str3 = "For Example: output file, %s, already exists!" % some_file
print str3

str4 = "my int value in this string : %d" % some_id
print str4
