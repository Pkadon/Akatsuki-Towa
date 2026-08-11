label avg101824(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc010_01 5', 'p18', [l(-10), light, flip], 6)
$ update_narrator('c181')
window show
with trans
get_char('c181') '[convertstrid(1222223)]' (**arg(1, 1222223))
$ update_portrait('sc010_01 5', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1222224)]' (**arg(2, 1222224))
return "avg101824"