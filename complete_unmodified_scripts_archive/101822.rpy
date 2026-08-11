label avg101822(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc010_01 4', 'p18', [l(-10), light, flip], 6)
$ update_narrator('c181')
window show
with trans
get_char('c181') '[convertstrid(1222221)]' (**arg(1, 1222221))
return "avg101822"