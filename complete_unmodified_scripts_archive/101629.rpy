label avg101629(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc008_01 5', 'p16', [mid(-18), light], 6)
$ update_narrator('c163')
window show
with trans
get_char('c163') '[convertstrid(1221606)]' (**arg(1, 1221606))
return "avg101629"