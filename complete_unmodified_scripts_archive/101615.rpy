label avg101615(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc008_01 2', 'p16', [mid(-18), light], 6)
$ update_narrator('c163')
window show
with trans
get_char('c163') '[convertstrid(1221563)]' (**arg(1, 1221563))
return "avg101615"