#!/usr/bin/env ruby
# puts ARGV[0].scan(/from\:(\+?.{11})|to\:(\+?.{11})|flags:(\-?.{11})/).join(',')
# puts ARGV[0].scan(/from\:(\+?.{11})\]\s\[to\:(\+?.{11})\]\s\[flags\:(\-?.{12})/).join(',')
# puts ARGV[0].scan(/from\:(\+?.\w*)\]\s\[to\:(\+?.\w*)\]\s\[flags\:(\-?\S*)\]/).join(',')
# puts ARGV[0].scan(/(?:from|to|flags)([+\-]?\d{11})/).join(',')
puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(',')
