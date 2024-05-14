tclsh
file delete "flash0:/ping.log"
puts [open "flash0:/ping.tcl" w] {
foreach ipaddr {
 192.168.1.193
 192.168.1.194
 192.168.1.195
 192.168.1.196
 192.168.1.197
 192.168.1.198
 192.168.1.199
 192.168.1.200
 192.168.1.254
 8.8.8.8
 8.8.4.4 
} { 
set now [clock seconds]
set timestr [clock format $now -format "%y-%m-%d %H:%M:%S"]
set output [exec "ping vrf MGMT $ipaddr"]
set filp [open "flash0:/ping.log" a]
puts $filp "\n\n\n$timestr: ping vrf MGMT $ipaddr "
puts $filp $output
close $filp
}
}
tclquit