#!/usr/bin/env ruby
# puts ARGV[0].scan(/from\:(\+?.{11})|to\:(\+?.{11})|flags:(\-?.{11})/).join(',')
# puts ARGV[0].scan(/from\:(\+?.{11})\]\s\[to\:(\+?.{11})\]\s\[flags\:(\-?.{12})/).join(',')
# puts ARGV[0].scan(/from\:(\+?.\w*)\]\s\[to\:(\+?.\w*)\]\s\[flags\:(\-?\S*)\]/).join(',')
# puts ARGV[0].scan(/(?:from|to|flags)([+\-]?\d{11})/).join(',')
# puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(',')
puts ARGV[0].scan(/\[(?:from|to|flags):(.\S*)\]/).join(',')


#using it with text losg file as input
# if ARGV.empty?
#     puts "Usage: ruby script_name.rb log_file_name"
#     exit 1
#   end

#   # Read the content of the log file
#   log_file_path = ARGV[0]
#   log_file_content = File.read(log_file_path)

#   # Apply the regular expression to extract the desired patterns
#   matches = log_file_content.scan(/\[(?:from:|to:|flags:)(.*?)\]/)

#   # Join the matches with commas and print the result
#   puts matches.join(',')
