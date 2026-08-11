label avg103012(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc022_01 1', 'p30', [mid(-9), light], 6)
$ update_narrator('c303')
window show
with trans
get_char('c303') '[convertstrid(1222443)]' (**arg(1, 1222443))
return "avg103012"